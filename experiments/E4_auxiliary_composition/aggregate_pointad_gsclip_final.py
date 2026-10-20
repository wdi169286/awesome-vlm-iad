"""Finalize the PointAD and GS-CLIP MVTec 3D-AD evidence audit.

The script consumes only compact downloaded artifacts.  It deliberately keeps
GS-CLIP's numerical summary separate from the admitted PointAD result because
the released GS-CLIP localization path does not consume the rebound depth
features (see the structural gate below).
"""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
RAW = HERE / "raw_completed_20261020"
GS_ROOT = RAW / "gsclip_depth_rebinding_complete"
POINT_ROOT = RAW / "pointad_mvtec3d_factorial_v3"
OUT = HERE / "final_completed_20261020"
TRAIN_CLASSES = ("carrot", "dowel", "cookie")
MAPPING_SEEDS = (0, 1, 2)
TARGETS = {
    "point": ("pixel", "pixel-auroc", "anomaly_maps"),
    "point_aupro": ("pixel", "pixel-aupro", "anomaly_maps"),
    "rendered": ("pixel", "pixel-auroc", "color_anomaly_maps"),
    "rendered_aupro": ("pixel", "pixel-aupro", "color_anomaly_maps"),
    "fused": ("pixel", "pixel-auroc", "integrate_anomaly_maps"),
    "fused_aupro": ("pixel", "pixel-aupro", "integrate_anomaly_maps"),
}


def stable_seed(label: str) -> int:
    return int.from_bytes(hashlib.sha256(label.encode()).digest()[:8], "little")


def load_gs(train_class: str, condition: str) -> dict[tuple[str, str, str, str], float]:
    path = GS_ROOT / train_class / condition / "metrics_full_precision.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {
        (row["class_name"], row["level"], row["metric"], row["modality"]): float(row["value"])
        for row in payload["records"]
    }


def hierarchical_interval(cells: dict[str, dict[str, list[float]]], label: str) -> tuple[float, float]:
    """Resample train-class runs, held-out categories, then mapping identities."""
    rng = np.random.default_rng(stable_seed(label))
    runs = tuple(cells)
    draws = np.empty(10_000, dtype=float)
    for draw in range(draws.size):
        run_means = []
        for selected in rng.choice(runs, size=len(runs), replace=True):
            categories = tuple(cells[str(selected)])
            sampled_categories = rng.choice(categories, size=len(categories), replace=True)
            category_means = []
            for category in sampled_categories:
                mappings = np.asarray(cells[str(selected)][str(category)], dtype=float)
                category_means.append(float(rng.choice(mappings, size=len(mappings), replace=True).mean()))
            run_means.append(float(np.mean(category_means)))
        draws[draw] = float(np.mean(run_means))
    return tuple(float(value) for value in np.quantile(draws, (0.025, 0.975)))


def gs_summary() -> dict:
    conditions = ["clean"] + [f"depth_rebind_seed{s}" for s in MAPPING_SEEDS] + [
        f"inverse_recovered_seed{s}" for s in MAPPING_SEEDS
    ]
    loaded = {train: {condition: load_gs(train, condition) for condition in conditions} for train in TRAIN_CLASSES}
    key_gate = all(
        set(loaded[train][condition]) == set(loaded[train]["clean"])
        for train in TRAIN_CLASSES
        for condition in conditions
    )

    effects: dict[str, dict] = {}
    max_inverse_error = 0.0
    max_rendered_control_error = 0.0
    for target, (level, metric, modality) in TARGETS.items():
        cells: dict[str, dict[str, list[float]]] = {}
        inverse_values = []
        for train in TRAIN_CLASSES:
            clean = loaded[train]["clean"]
            categories = sorted(
                key[0] for key in clean if key[1:] == (level, metric, modality)
            )
            cells[train] = {category: [] for category in categories}
            for mapping_seed in MAPPING_SEEDS:
                treated = loaded[train][f"depth_rebind_seed{mapping_seed}"]
                recovered = loaded[train][f"inverse_recovered_seed{mapping_seed}"]
                for category in categories:
                    key = (category, level, metric, modality)
                    delta = treated[key] - clean[key]
                    cells[train][category].append(delta)
                    inverse_delta = recovered[key] - clean[key]
                    inverse_values.append(inverse_delta)
                    max_inverse_error = max(max_inverse_error, abs(inverse_delta))
                    if target.startswith("rendered"):
                        max_rendered_control_error = max(max_rendered_control_error, abs(delta))
        flat = [value for by_category in cells.values() for values in by_category.values() for value in values]
        low, high = hierarchical_interval(cells, target)
        effects[target] = {
            "effect": float(np.mean(flat)),
            "ci95_low": low,
            "ci95_high": high,
            "n_train_class_runs": len(TRAIN_CLASSES),
            "n_mapping_seeds": len(MAPPING_SEEDS),
            "n_paired_cells": len(flat),
            "max_abs_inverse_delta": float(max(abs(value) for value in inverse_values)),
        }

    validations = [
        json.loads((GS_ROOT / "metadata" / f"depth_rebind_seed{s}" / "validation.json").read_text())
        for s in MAPPING_SEEDS
    ]
    test_source = (GS_ROOT / "provenance" / "official_test2.py").read_text(encoding="utf-8")
    structural_gate = all(
        marker in test_source
        for marker in (
            "image_features2, patch_features2 = model.encode_depth",
            "patch_feature = patch_features[0]",
            "d3_similarity_map = back_to_3d(similarity_map, d2_3d_cor, non_zero_index)",
        )
    )
    # The three markers jointly show that depth patch features are computed but
    # not used to form the registered point/fused localization maps.
    localization_uses_rebound_depth = not structural_gate
    gates = {
        "complete_21_of_21_units": sum(
            (GS_ROOT / train / condition / "metrics_full_precision.json").is_file()
            for train in TRAIN_CLASSES
            for condition in conditions
        ) == 21,
        "metric_keys_paired": key_gate,
        "1197_records_each_mapping": all(row["records"] == 1197 for row in validations),
        "no_fixed_points": all(row["fixed_points"] == 0 for row in validations),
        "multiset_preserved": all(row["multiset_preserved_per_stratum"] for row in validations),
        "metadata_inverse_recovery": all(row["inverse_metadata_recovery"] for row in validations),
        "numeric_inverse_recovery_at_1e-5": max_inverse_error <= 1e-5,
        "rendered_negative_control_at_1e-5": max_rendered_control_error <= 1e-5,
        "registered_localization_endpoint_consumes_rebound_depth": localization_uses_rebound_depth,
    }
    return {
        "schema": 1,
        "estimand": "depth_rebind-minus-clean within train-class checkpoint, held-out category, and mapping seed",
        "bootstrap": "10,000 draws; train-class run, then category, then mapping identity",
        "effects": effects,
        "gates": gates,
        "max_abs_numeric_inverse_delta": max_inverse_error,
        "max_abs_rendered_control_delta": max_rendered_control_error,
        "admission": "excluded_from_E4_numeric_conclusion",
        "admission_reason": (
            "The released test2 localization path computes depth patch features but forms point and fused "
            "localization maps from rendered-image patch features; therefore depth-path rebinding does not "
            "manipulate the registered AUPRO or Point-AUROC endpoint."
        ),
    }


def point_summary() -> dict:
    source = json.loads((POINT_ROOT / "aggregate_factorial.json").read_text(encoding="utf-8"))
    coverage = json.loads((POINT_ROOT / "validation" / "coverage.json").read_text(encoding="utf-8"))
    chosen = {}
    for contrast in ("correspondence_permute", "rgb_swap", "interaction_did"):
        chosen[contrast] = {}
        for modality in ("point", "rgb", "fusion"):
            chosen[contrast][modality] = {}
            for metric in ("pixel_auroc", "pixel_ap", "aupro_0_30", "image_auroc"):
                chosen[contrast][modality][metric] = source["across_run"][contrast][modality][metric]
    controls = coverage["intervention_controls"]
    return {
        "schema": 1,
        "estimand": source["estimand"],
        "aggregation": source["aggregation"],
        "effects": chosen,
        "gates": {
            "suite_complete": (POINT_ROOT / "SUITE_COMPLETE").is_file(),
            "three_train_class_runs": source["train_classes"] == ["carrot", "cookie", "dowel"],
            "complete_2x2_cells": len(coverage["cells"]) == 3,
            "all_27_train_category_controls_passed": len(controls) == 27 and all(row["passed"] for row in controls),
            "correspondence_inverse_exact": all(row["correspondence_audit_passed"] for row in controls),
            "rgb_branch_fixed_under_correspondence_permutation": all(
                row["rgb_branch_fixed_under_correspondence_permute"] for row in controls
            ),
            "point_branch_fixed_under_rgb_swap": all(row["point_branch_fixed_under_rgb_swap"] for row in controls),
        },
        "admission": "admitted_to_E4_as_implementation_scoped_factorial",
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    gs = gs_summary()
    point = point_summary()
    (OUT / "gsclip_depth_rebinding_final_audit.json").write_text(
        json.dumps(gs, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (OUT / "pointad_factorial_final_audit.json").write_text(
        json.dumps(point, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    with (OUT / "paper_effects.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(("method", "contrast", "modality", "metric", "effect", "ci95_low", "ci95_high", "admission"))
        for contrast, modalities in point["effects"].items():
            for modality, metrics in modalities.items():
                for metric, row in metrics.items():
                    writer.writerow(("PointAD", contrast, modality, metric, row["effect"], row["ci95_low_hierarchical"], row["ci95_high_hierarchical"], point["admission"]))
        for target, row in gs["effects"].items():
            writer.writerow(("GS-CLIP", "depth_rebind", target, target.split("_")[-1], row["effect"], row["ci95_low"], row["ci95_high"], gs["admission"]))
    print(json.dumps({"pointad": point["admission"], "gsclip": gs["admission"], "output": str(OUT)}, indent=2))


if __name__ == "__main__":
    main()
