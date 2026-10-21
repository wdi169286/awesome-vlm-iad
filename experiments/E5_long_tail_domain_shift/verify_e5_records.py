#!/usr/bin/env python3
"""Recompute and verify the compact E5 result bundle."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[2] / "results" / "E5"
TOLERANCE = 5e-10
BOOTSTRAP_SEED = 20261020
BOOTSTRAP_REPLICATES = 10_000


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def close(actual: float, expected: float, label: str) -> None:
    if not math.isclose(actual, expected, rel_tol=0.0, abs_tol=TOLERANCE):
        raise AssertionError(f"{label}: {actual} != {expected}")


def rounded(actual: float, expected: float, digits: int, label: str) -> None:
    if round(actual, digits) != expected:
        raise AssertionError(
            f"{label}: rounded {actual} to {round(actual, digits)}, expected {expected}"
        )


def hierarchical_ci(grouped_values: dict[str, list[float]]) -> tuple[float, float]:
    """Resample groups and one paired draw per sampled group."""
    groups = sorted(grouped_values)
    values = np.asarray([grouped_values[group] for group in groups], dtype=float)
    require(values.ndim == 2, "bootstrap values must form a rectangular matrix")
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    replicates = np.empty(BOOTSTRAP_REPLICATES, dtype=float)
    # Preserve the registered generator's per-replicate RNG call order so the
    # released confidence bounds are exactly reproducible.
    for index in range(BOOTSTRAP_REPLICATES):
        group_indices = rng.integers(0, len(groups), len(groups))
        draw_indices = rng.integers(0, values.shape[1], len(groups))
        replicates[index] = values[group_indices, draw_indices].mean()
    low, high = np.quantile(replicates, [0.025, 0.975])
    return float(low), float(high)


def group_means(rows: list[dict[str, str]], group: str, field: str) -> dict[str, float]:
    grouped: dict[str, list[float]] = {}
    for row in rows:
        grouped.setdefault(row[group], []).append(float(row[field]))
    return {key: mean(values) for key, values in grouped.items()}


def verify_ltad() -> None:
    root = ROOT / "ltad"
    completion = load_json(root / "completion_audit.json")
    require(completion["complete"], "LTAD completion flag is false")
    require(completion["expected_configurations"] == 300, "LTAD expected count")
    correction = load_json(root / "stratum_correction_audit.json")
    require(correction["cohort_unchanged"], "LTAD correction changed the cohort")
    require(correction["manifest_count"] == 300, "LTAD correction manifest count")
    require(
        correction["changes"]["step200"]["changed_categories"] == ["cable"],
        "LTAD corrected category",
    )
    with (root / "paired_category_draw.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    require(len(rows) == 150, "LTAD paired row count")
    require(
        len({(row["split"], row["category"], row["draw"]) for row in rows}) == 150,
        "LTAD duplicate split/category/draw rows",
    )
    for row in rows:
        require(int(row["limited_k"]) == min(16, int(row["official_train_count"])),
                "LTAD limited K")
        require(int(row["matched_rich_k"]) == 16, "LTAD matched-rich K")
        for metric in ("image_auroc", "image_ap"):
            close(
                float(row[f"limited_{metric}"]) - float(row[f"matched_rich_{metric}"]),
                float(row[f"delta_{metric}"]),
                f"LTAD row delta {metric}",
            )

    document = load_json(root / "summary.json")
    summary = document["macro_strata_effects"]
    require(len(summary) == 4, "LTAD macro/strata summary count")
    for item in summary:
        selected = [row for row in rows if row["split"] == item["split"]]
        require(len(selected) == 75, f"LTAD {item['split']} row count")
        metric = item["metric"]
        limited_field = f"limited_{metric}"
        rich_field = f"matched_rich_{metric}"
        close(mean([float(row[limited_field]) for row in selected]),
              item["limited_macro"], f"LTAD {item['split']} {metric} limited macro")
        close(mean([float(row[rich_field]) for row in selected]),
              item["matched_rich_macro"], f"LTAD {item['split']} {metric} rich macro")
        close(mean([float(row[f"delta_{metric}"]) for row in selected]),
              item["paired_delta"], f"LTAD {item['split']} {metric} effect")

        grouped_deltas: dict[str, list[float]] = {}
        for row in selected:
            grouped_deltas.setdefault(row["category"], []).append(float(row[f"delta_{metric}"]))
        low, high = hierarchical_ci(grouped_deltas)
        close(low, item["ci_low"], f"LTAD {item['split']} {metric} CI low")
        close(high, item["ci_high"], f"LTAD {item['split']} {metric} CI high")

        for stratum in ("head", "tail"):
            stratum_rows = [row for row in selected if row["stratum"] == stratum]
            close(mean([float(row[limited_field]) for row in stratum_rows]),
                  item[f"limited_{stratum}"],
                  f"LTAD {item['split']} {metric} limited {stratum}")
            close(mean([float(row[rich_field]) for row in stratum_rows]),
                  item[f"matched_rich_{stratum}"],
                  f"LTAD {item['split']} {metric} rich {stratum}")

        category_means = group_means(selected, "category", limited_field)
        ordered = sorted((value, category) for category, value in category_means.items())
        close(ordered[0][0], item["worst_group"]["value"],
              f"LTAD {item['split']} {metric} worst value")
        require(ordered[0][1] == item["worst_group"]["category"],
                f"LTAD {item['split']} {metric} worst category")
        bottom_count = math.ceil(len(ordered) / 4)
        close(mean([value for value, _ in ordered[:bottom_count]]),
              item["bottom_performance_quartile"],
              f"LTAD {item['split']} {metric} bottom quartile")

    micro = document["micro_by_draw"]
    require(len(micro) == 20, "LTAD micro summary count")
    require(
        len({(item["split"], item["draw"], item["condition"]) for item in micro}) == 20,
        "LTAD duplicate micro summaries",
    )
    expected_micro = {
        ("exp200", "limited"): (0.8154, 0.9270),
        ("exp200", "matched_rich"): (0.8181, 0.9265),
        ("step200", "limited"): (0.8125, 0.9247),
        ("step200", "matched_rich"): (0.8226, 0.9285),
    }
    for key, expected in expected_micro.items():
        selected = [item for item in micro if (item["split"], item["condition"]) == key]
        require(len(selected) == 5, f"LTAD micro draw count {key}")
        rounded(mean([item["image_auroc"] for item in selected]), expected[0], 4,
                f"LTAD table micro I-AUROC {key}")
        rounded(mean([item["image_ap"] for item in selected]), expected[1], 4,
                f"LTAD table micro I-AP {key}")
        require(all(item["sample_count"] == 1725 for item in selected),
                f"LTAD micro cohort size {key}")

    control = load_json(root / "k0_negative_control.json")
    require(control["official_test_set_unchanged"], "LTAD K0 test cohort changed")
    close(control["split_intervention_delta"], 0.0, "LTAD K0 negative control")


def verify_aebad() -> None:
    root = ROOT / "aebad"
    completion = load_json(root / "completion_audit.json")
    require(completion["complete"], "AeBAD completion flag is false")
    require(completion["expected_archives"] == 30, "AeBAD expected archive count")
    calibration = load_json(root / "design_audit.json")["calibration"]
    require(calibration["protocol"] == "fixed normal cohort shared by K0 and every K4 draw",
            "AeBAD calibration protocol")
    require(calibration["count"] == 32, "AeBAD calibration count")
    require(calibration["excluded_union_support_count"] == 20,
            "AeBAD excluded support count")
    require(len(calibration["queries"]) == len(set(calibration["queries"])) == 32,
            "AeBAD calibration queries are not 32 unique records")
    require(all(Path(item).name == item for item in calibration["queries"]),
            "AeBAD calibration records must be basenames")
    with (root / "per_domain_draw.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    require(len(rows) == 20, "AeBAD paired row count")
    require(len({(row["domain"], row["draw"]) for row in rows}) == 20,
            "AeBAD duplicate domain/draw rows")
    require(len({row["domain"] for row in rows}) == 4, "AeBAD domain count")
    for row in rows:
        for metric in ("i_auroc", "i_ap", "normal_fpr", "anomaly_fnr"):
            close(float(row[f"k4_{metric}"]) - float(row[f"k0_{metric}"]),
                  float(row[f"delta_{metric}"]), f"AeBAD row delta {metric}")

    document = load_json(root / "summary.json")
    effects = {item["metric"]: item for item in document["paired_effects"]}
    require(set(effects) == {"i_auroc", "i_ap", "normal_fpr", "anomaly_fnr"},
            "AeBAD paired-effect endpoints")
    for metric, item in effects.items():
        close(mean([float(row[f"delta_{metric}"]) for row in rows]),
              item["paired_delta"], f"AeBAD {metric}")
        grouped = {
            domain: [float(row[f"delta_{metric}"]) for row in rows if row["domain"] == domain]
            for domain in sorted({row["domain"] for row in rows})
        }
        low, high = hierarchical_ci(grouped)
        close(low, item["ci_low"], f"AeBAD {metric} CI low")
        close(high, item["ci_high"], f"AeBAD {metric} CI high")

    conditions = document["conditions"]
    require(len(conditions) == 6, "AeBAD condition-summary count")
    k0 = [item for item in conditions if item["condition"] == "k0"]
    k4 = [item for item in conditions if item["condition"] == "k4"]
    require(len(k0) == 1 and len(k4) == 5, "AeBAD K0/K4 condition counts")
    for item in conditions:
        draw_rows = [row for row in rows if int(row["draw"]) == item["draw"]]
        require(len(draw_rows) == 4, f"AeBAD draw cohort {item['draw']}")
        prefix = item["condition"]
        for metric in ("i_auroc", "i_ap", "normal_fpr", "anomaly_fnr"):
            values = [float(row[f"{prefix}_{metric}"]) for row in draw_rows]
            close(mean(values), item[f"macro_{metric}"],
                  f"AeBAD {prefix} draw {item['draw']} macro {metric}")
            close(float(np.var(values, ddof=1)), item[f"domain_variance_{metric}"],
                  f"AeBAD {prefix} draw {item['draw']} variance {metric}")
            worst = max(values) if metric in {"normal_fpr", "anomaly_fnr"} else min(values)
            close(worst, item[f"worst_group_{metric}"],
                  f"AeBAD {prefix} draw {item['draw']} worst {metric}")

    table_expected = {
        "k0": {
            "macro_i_auroc": 0.7322, "macro_i_ap": 0.8636,
            "micro_i_auroc": 0.7490, "micro_i_ap": 0.8636,
            "macro_normal_fpr": 0.1713, "macro_anomaly_fnr": 0.5062,
            "domain_variance_i_auroc": 0.01794, "worst_group_i_auroc": 0.5599,
        },
        "k4": {
            "macro_i_auroc": 0.7758, "macro_i_ap": 0.8896,
            "micro_i_auroc": 0.7940, "micro_i_ap": 0.8903,
            "macro_normal_fpr": 0.1678, "macro_anomaly_fnr": 0.4207,
            "domain_variance_i_auroc": 0.01336, "worst_group_i_auroc": 0.6311,
        },
    }
    for condition, expected_fields in table_expected.items():
        selected = k0 if condition == "k0" else k4
        for field, expected in expected_fields.items():
            digits = 5 if field == "domain_variance_i_auroc" else 4
            rounded(mean([item[field] for item in selected]), expected, digits,
                    f"AeBAD table {condition} {field}")


if __name__ == "__main__":
    verify_ltad()
    verify_aebad()
    print("E5 compact records and manuscript-facing statistics verified")
