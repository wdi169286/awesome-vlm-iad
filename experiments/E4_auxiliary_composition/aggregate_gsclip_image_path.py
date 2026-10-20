#!/usr/bin/env python3
"""Aggregate the GS-CLIP depth-identity intervention on consumed endpoints.

The released evaluator uses depth features in the fused image-level score, but
not in the point/rendered localization maps.  This audit therefore treats
image AUROC/AP as target endpoints and the RGB-only score plus all localization
maps as negative controls.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
DEFAULT_ROOT = HERE / "raw_completed_20261020" / "gsclip_depth_rebinding_complete"
DEFAULT_OUT = HERE / "final_completed_20261020" / "gsclip_depth_identity_image_audit.json"
TRAIN_CLASSES = ("carrot", "dowel", "cookie")
MAPPING_SEEDS = (0, 1, 2)

TARGETS = {
    "point_image_auroc": ("image", "image-auroc", "pr_sp"),
    "point_image_ap": ("image", "image-ap", "pr_sp"),
    "fused_image_auroc": ("image", "image-auroc", "integrate_pr_sp"),
    "fused_image_ap": ("image", "image-ap", "integrate_pr_sp"),
}
CONTROLS = {
    "rgb_image_auroc": ("image", "image-auroc", "color_pr_sp"),
    "rgb_image_ap": ("image", "image-ap", "color_pr_sp"),
    "point_pixel_auroc": ("pixel", "pixel-auroc", "anomaly_maps"),
    "point_aupro": ("pixel", "pixel-aupro", "anomaly_maps"),
    "rgb_pixel_auroc": ("pixel", "pixel-auroc", "color_anomaly_maps"),
    "rgb_aupro": ("pixel", "pixel-aupro", "color_anomaly_maps"),
    "fused_pixel_auroc": ("pixel", "pixel-auroc", "integrate_anomaly_maps"),
    "fused_aupro": ("pixel", "pixel-aupro", "integrate_anomaly_maps"),
}


def stable_seed(label: str) -> int:
    return int.from_bytes(hashlib.sha256(label.encode()).digest()[:8], "little")


def load_metrics(root: Path, train_class: str, condition: str) -> dict[tuple[str, str, str, str], float]:
    path = root / train_class / condition / "metrics_full_precision.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {
        (row["class_name"], row["level"], row["metric"], row["modality"]): float(row["value"])
        for row in payload["records"]
    }


def interval(cells: dict[str, dict[str, list[float]]], label: str) -> tuple[float, float]:
    """Resample checkpoint, held-out category, and mapping identity."""
    rng = np.random.default_rng(stable_seed(label))
    runs = tuple(cells)
    draws = np.empty(20_000, dtype=float)
    for draw in range(draws.size):
        run_means = []
        for run in rng.choice(runs, size=len(runs), replace=True):
            categories = tuple(cells[str(run)])
            sampled = rng.choice(categories, size=len(categories), replace=True)
            category_means = []
            for category in sampled:
                mappings = np.asarray(cells[str(run)][str(category)], dtype=float)
                category_means.append(float(rng.choice(mappings, size=len(mappings), replace=True).mean()))
            run_means.append(float(np.mean(category_means)))
        draws[draw] = float(np.mean(run_means))
    return tuple(float(x) for x in np.quantile(draws, (0.025, 0.975)))


def summarize_endpoint(
    loaded: dict[str, dict[str, dict[tuple[str, str, str, str], float]]],
    name: str,
    endpoint: tuple[str, str, str],
) -> dict[str, object]:
    level, metric, modality = endpoint
    cells: dict[str, dict[str, list[float]]] = {}
    inverse_deltas: list[float] = []
    for train_class in TRAIN_CLASSES:
        clean = loaded[train_class]["clean"]
        categories = sorted(key[0] for key in clean if key[1:] == endpoint)
        cells[train_class] = {category: [] for category in categories}
        for mapping_seed in MAPPING_SEEDS:
            treated = loaded[train_class][f"depth_rebind_seed{mapping_seed}"]
            recovered = loaded[train_class][f"inverse_recovered_seed{mapping_seed}"]
            for category in categories:
                key = (category, level, metric, modality)
                cells[train_class][category].append(treated[key] - clean[key])
                inverse_deltas.append(recovered[key] - clean[key])
    flat = [value for by_category in cells.values() for values in by_category.values() for value in values]
    low, high = interval(cells, name)
    return {
        "effect": float(np.mean(flat)),
        "ci95_low": low,
        "ci95_high": high,
        "n_checkpoint_category_mapping_cells": len(flat),
        "max_abs_inverse_delta": float(max(abs(value) for value in inverse_deltas)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    root = args.raw_root.resolve()
    output = args.output.resolve()
    conditions = ["clean"] + [f"depth_rebind_seed{s}" for s in MAPPING_SEEDS] + [
        f"inverse_recovered_seed{s}" for s in MAPPING_SEEDS
    ]
    loaded = {
        train_class: {condition: load_metrics(root, train_class, condition) for condition in conditions}
        for train_class in TRAIN_CLASSES
    }
    keys_paired = all(
        set(loaded[train_class][condition]) == set(loaded[train_class]["clean"])
        for train_class in TRAIN_CLASSES
        for condition in conditions
    )
    targets = {
        name: summarize_endpoint(loaded, name, endpoint) for name, endpoint in TARGETS.items()
    }
    controls = {
        name: summarize_endpoint(loaded, name, endpoint) for name, endpoint in CONTROLS.items()
    }
    validations = [
        json.loads((root / "metadata" / f"depth_rebind_seed{s}" / "validation.json").read_text())
        for s in MAPPING_SEEDS
    ]
    source = (root / "provenance" / "official_test2.py").read_text(encoding="utf-8")
    path_markers = (
        "image_features2, patch_features2 = model.encode_depth(whole_image2",
        "image_features = model.fusion_r_d(image_features,image_features2)",
        "text_probs = image_features.unsqueeze(1) @ text_features.permute",
        "results[cls_name[0]]['pr_sp'].extend(0.5*anomaly_map.max() + 0.5*text_probs",
    )
    target_path_consumed = all(marker in source for marker in path_markers)
    localization_controls = tuple(
        controls[name] for name in controls if "pixel" in name or "aupro" in name
    )
    payload = {
        "schema": 1,
        "estimand": "depth-identity-rebinding minus clean on GS-CLIP image-level outputs",
        "scope": "three train-class checkpoints by nine held-out categories by three mappings",
        "bootstrap": "20,000 draws: checkpoint, held-out category, then mapping identity",
        "targets": targets,
        "negative_controls": controls,
        "gates": {
            "complete_21_of_21_units": all(
                (root / train_class / condition / "metrics_full_precision.json").is_file()
                for train_class in TRAIN_CLASSES
                for condition in conditions
            ),
            "metric_keys_paired": keys_paired,
            "1197_records_each_mapping": all(row["records"] == 1197 for row in validations),
            "no_fixed_points": all(row["fixed_points"] == 0 for row in validations),
            "multiset_preserved": all(row["multiset_preserved_per_stratum"] for row in validations),
            "metadata_inverse_recovery": all(row["inverse_metadata_recovery"] for row in validations),
            "registered_image_endpoint_consumes_rebound_depth": target_path_consumed,
            "rgb_image_score_exactly_fixed": controls["rgb_image_auroc"]["effect"] == 0.0
            and controls["rgb_image_ap"]["effect"] == 0.0,
            "localization_controls_within_1e-5": max(
                abs(float(row["effect"])) for row in localization_controls
            ) <= 1e-5,
            "inverse_recovery_within_1e-5": max(
                float(row["max_abs_inverse_delta"]) for row in (*targets.values(), *controls.values())
            ) <= 1e-5,
        },
    }
    payload["admission"] = (
        "admitted_as_image_level_depth_identity_stress"
        if all(payload["gates"].values())
        else "excluded_failed_gate"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
