# Auxiliary Foundation Prior Coupling — Results

> **v6 interpretation.** The three-checkpoint BTP result remains a scoped negative-transfer boundary. PointAD adds an admitted, implementation-scoped three-train-class RGB-identity × point--pixel-correspondence factorial on MVTec 3D-AD. GS-CLIP is now evaluated on the image-score path that actually consumes depth features; its depth-identity effects are small and unresolved, while RGB-only scores and localization maps serve as negative controls.

| Field | Value |
|---|---|
| Completed method | Official BTP-3DAD, commit `738f3ad51aaac71712e657b2ab0977dd5c3bcb65` |
| Dataset/protocol | AnomalyShapeNet; train auxiliary class `jar0`, evaluate the other 39 target classes |
| Checkpoints | Three independent official-setting training runs, `seed=0/1/2`; checkpoint SHA-256 retained in every result JSON |
| Conditions | `full`, `geometry_zero`, `geometry_permute`, `geometry_cross_sample`, `geometry_cross_category` |
| Statistical unit | Paired target category within checkpoint; final interval independently resamples the 3 checkpoint and 39 category axes (50,000 repetitions) |
| Scale/direction | Values and deltas on 0–1 scale; delta = treatment − matched `full` reference; negative would mean damage |
| Public storage | Per-object predictions are not redistributed; seed aggregates and the final crossed aggregate are included in `raw_compact/btp_anomalyshapenet_*` |

## A-summary. Publication-facing evidence matrix

| Question | Completed evidence | Independent coverage | Result | Boundary / next required cell |
|---|---|---:|---|---|
| Is aligned geometry automatically beneficial? | full versus zero geometry | 1 method × 3 checkpoints × 39 transfer targets | no; zero geometry improves AUPRO@0.30 by +0.0229 under crossed uncertainty | one cross-category protocol cannot establish a general law |
| Is wrong or misbound geometry predictably harmful? | cross-sample, cross-category and permutation | 1 native-geometry implementation | no; effects are non-negative on the primary endpoint | test in-domain data and a different fusion mechanism |
| Is this evidence of an Auxiliary role? | E/B/O path plus controlled intervention | BTP-3DAD | path exists, but the preregistered benefit prediction is refuted | role membership and benefit must remain separate |

| Main-table endpoint | Shared secondary endpoints | Critical missing endpoints |
|---|---|---|
| paired ΔAUPRO@0.30 | ΔI-AUROC, ΔI-AP, ΔPoint-AUROC, ΔPoint-AP | matched in-domain replication, SAM prior, RGB–3D fusion, and second dataset |

## A1. Official baseline reproduction

The baseline was executed with the repository's current official evaluation path. The sampled-point and reconstructed full-resolution metrics are reported separately rather than silently mixed.

| Evaluation | I-AUROC | I-AP | F1-max | Point-AUROC | Point-AP | AUPRO@0.30 |
|---|---:|---:|---:|---:|---:|---:|
| Official current-code baseline, sampled 2,048 points | 0.6611 | 0.7295 | 0.7682 | 0.8421 | 0.2535 | 0.5568 |
| Same predictions, reconstructed full resolution | 0.6611 | 0.7295 | 0.7682 | 0.8426 | 0.2527 | 0.5424 |

Protocol note: the paper and the checked-out GitHub code are not identical in every default. The paper states prompt length 4, whereas the code defaults to `n_ctx=8`; its configurable top-k aggregation defaults to 20%, whereas the paper describes a maximum. The completed rows used `topk=0`, i.e. the paper-style maximum, but retained the code-default prompt length. They are therefore labelled **official-code, paper-style score aggregation**, not a complete paper-parity reconstruction.

## A2. Auxiliary-evidence interventions: full-resolution outputs

| Contrast | ΔI-AUROC (95% CI) | ΔI-AP (95% CI) | ΔPoint-AUROC (95% CI) | ΔPoint-AP (95% CI) | ΔAUPRO@0.30 (95% CI) |
|---|---:|---:|---:|---:|---:|
| Geometry from another sample − full | +0.0117 [−0.0021, +0.0272] | +0.0125 [−0.0032, +0.0293] | +0.0101 [+0.0022, +0.0182] | +0.0141 [+0.0025, +0.0268] | +0.0195 [+0.0054, +0.0343] |
| Permuted geometry − full | +0.0039 [−0.0077, +0.0157] | +0.0033 [−0.0064, +0.0134] | +0.0065 [−0.0056, +0.0173] | +0.0103 [−0.0024, +0.0239] | +0.0155 [−0.0017, +0.0321] |
| Zero geometry − full | +0.0128 [−0.0001, +0.0269] | +0.0169 [+0.0017, +0.0330] | +0.0360 [+0.0246, +0.0482] | +0.0190 [+0.0017, +0.0390] | +0.0235 [+0.0076, +0.0390] |
| Geometry from another target category − full | +0.0065 [−0.0083, +0.0211] | +0.0074 [−0.0082, +0.0231] | +0.0072 [−0.0045, +0.0182] | +0.0115 [−0.0021, +0.0262] | +0.0163 [+0.0018, +0.0295] |

## A3. What the completed experiment does—and does not—show

- The planned prediction “removing or misaligning geometry must reduce localization” is **not supported** in this cross-category transfer setting.
- Zeroing the geometry branch improves full-resolution Point-AUROC by 0.0360 and AUPRO by 0.0235. Cross-sample geometry also improves the three localization metrics. This is consistent with auxiliary geometry producing negative transfer when the model is trained on one auxiliary object class and tested on disjoint target classes.
- The result is stronger than a module-removal anecdote because the same 39 query categories, appearance input and evaluation code are paired across absence, within-sample permutation and cross-sample replacement, and the registered removal effect recurs across three independently trained checkpoints.
- It does **not** establish that geometry is generally harmful. PointAD supplies a separate correspondence result under its disclosed implementation; its absolute paper-performance gaps remain a reproducibility boundary and are not used for cross-method ranking.

## A4. Remaining auxiliary experiments

| Method | Dataset | Contrast | Status / gate |
|---|---|---|---|
| PointAD | MVTec 3D-AD | RGB identity $\times$ point--pixel correspondence | Complete on three train-class checkpoints. All 27 run--held-out-category controls passed. Correspondence rebinding: point AUPRO $-0.42896$ [$-0.55469,-0.29619$], point P-AUROC $-0.23981$ [$-0.30303,-0.16503$]; RGB-identity rebinding: RGB AUPRO $-0.33246$ [$-0.38996,-0.27444$], RGB P-AUROC $-0.12299$ [$-0.15786,-0.09380$]; fused AUPRO interaction $-0.16401$ [$-0.24048,-0.09287$]. |
| GS-CLIP | MVTec 3D-AD | clean rendered--depth pairing versus label-stratified no-fixed-point depth identity rebinding | All 21 clean/rebinding/inverse units completed. Point-path I-AUROC $+0.00048$ [$-0.00003,+0.00122$] and fused I-AUROC $+0.00013$ [$-0.00041,+0.00090$]. The image-score path consumes depth features; RGB-only scores are exactly fixed, localization changes are below $10^{-5}$, and inverse recovery passes. |
| PointAD | Eyecandies / Real3D-AD | external-dataset extension | Deferred. It cannot replace the complete official MVTec 3D-AD protocol or be relabelled as native RGB–3D evidence where the modality is absent. |
| BTP-3DAD | AnomalyShapeNet | state-matched geometry donor − full | Old compound donor rows remain excluded. The final three-checkpoint table uses the registered hash-sorted donor protocol and crossed checkpoint×category uncertainty. |
| BTP-3DAD sensitivity | AnomalyShapeNet | `n_ctx=4` vs code-default `n_ctx=8`; paper-style max vs code-default top-20% image aggregation | Useful paper/code sensitivity check; lower priority than the native PointAD factorial. |
| Additional BTP training seeds | AnomalyShapeNet | repeat all four interventions | Complete for seeds 0/1/2; final crossed checkpoint × category analysis is reported in A6 |

## A5. Independent checkpoint replication (seed 1)

Seed 1 is retained below as a separate trained-checkpoint diagnostic rather than pooled with seed 0 as if categories were independent across seeds. The primary AUPRO effect of removing geometry recurred, while the three wrong/misbound-geometry effects attenuated and crossed zero. The final inference is the crossed three-checkpoint analysis in A6.

| Contrast | Delta Point-AP (95% CI) | Delta AUPRO@0.30 (95% CI) | Positive category signs for AUPRO |
|---|---:|---:|---:|
| Geometry from another sample minus full | -0.0017 [-0.0098, +0.0077] | +0.0065 [-0.0022, +0.0151] | 21/39 |
| Permuted geometry minus full | -0.0040 [-0.0139, +0.0064] | +0.0027 [-0.0050, +0.0105] | 20/39 |
| Zero geometry minus full | -0.0051 [-0.0194, +0.0070] | +0.0229 [+0.0151, +0.0309] | 32/39 |
| Geometry from another target category minus full | -0.0014 [-0.0095, +0.0070] | +0.0034 [-0.0056, +0.0121] | 23/39 |

The route is more specific than the seed-0 table alone suggested: removing the transferred geometry branch repeatedly improves region-overlap localization, but does not repeatedly improve Point-AP. Seed 2 subsequently completed; A6 supersedes this interim single-checkpoint interpretation.

## A6. Three-checkpoint crossed analysis (supersedes the pending seed-2 note)

Seed 2 has completed under the registered state-matched, hash-sorted donor protocol. The final analysis keeps the three independently trained checkpoints and the 39 target categories as separate crossed axes. It does not treat the 117 checkpoint-category cells as independent observations. The 95% intervals below independently resample checkpoint and category indices (50,000 repetitions); the machine-readable result is `raw_compact/btp_anomalyshapenet_three_checkpoint_crossed_bootstrap.json`.

| Contrast | ΔI-AUROC (crossed 95% CI) | ΔPoint-AUROC (crossed 95% CI) | ΔPoint-AP (crossed 95% CI) | ΔAUPRO@0.30 (crossed 95% CI) | Checkpoint signs for AUPRO |
|---|---:|---:|---:|---:|---:|
| Geometry from another sample − full | −0.0057 [−0.0150, +0.0025] | +0.0127 [+0.0044, +0.0222] | +0.0030 [−0.0067, +0.0159] | +0.0097 [−0.0011, +0.0230] | 3/3 positive |
| Permuted geometry − full | −0.0094 [−0.0200, −0.0011] | +0.0108 [−0.0002, +0.0215] | +0.0010 [−0.0090, +0.0132] | +0.0090 [−0.0009, +0.0219] | 3/3 positive |
| Zero geometry − full | −0.0100 [−0.0230, +0.0007] | +0.0288 [+0.0177, +0.0414] | +0.0038 [−0.0115, +0.0233] | +0.0229 [+0.0137, +0.0329] | 3/3 positive |
| Geometry from another target category − full | −0.0105 [−0.0301, +0.0031] | +0.0111 [+0.0018, +0.0206] | +0.0024 [−0.0072, +0.0150] | +0.0105 [+0.0002, +0.0223] | 3/3 positive |

The stable finding is narrower and more informative than “geometry corruption helps.” Removing the transferred geometry branch improves Point-AUROC and region-overlap AUPRO in every checkpoint, while Point-AP does not show a stable gain and image-level AUROC tends to decrease. Thus the auxiliary stream changes the operational error route: it can hinder spatial ranking under cross-category transfer even while contributing to image-level discrimination. This remains a bounded BTP/AnomalyShapeNet finding. The admitted PointAD factorial is reported separately because it tests identity and correspondence under a different implementation and dataset; its absolute baseline gaps remain disclosed.

## A7. PointAD reproducibility boundary

The full MVTec 3D-AD content audit passed for 1,197 scans and 10,773 official rendered views, and the official evaluator agreed with our wrapper for the three preregistered training categories (`carrot`, `cookie`, `dowel`). However, the mean held-out performance did not reproduce the paper within the preregistered ±2 percentage-point tolerance.

| Stream | Metric | Paper value (%) | Reproduced mean (%) | Difference (pp) |
|---|---|---:|---:|---:|
| Fusion | image AP | 96.10 | 95.42 | −0.68 |
| Fusion | image AUROC | 86.90 | 84.61 | −2.29 |
| Fusion | pixel AUPRO | 90.20 | 86.64 | −3.56 |
| Fusion | pixel AUROC | 97.20 | 95.71 | −1.49 |
| Point | image AP | 94.20 | 92.36 | −1.84 |
| Point | image AUROC | 82.00 | 77.71 | −4.29 |
| Point | pixel AUPRO | 84.40 | 68.00 | −16.40 |
| Point | pixel AUROC | 95.50 | 86.63 | −8.87 |

The numerical differences do not invalidate the completed implementation:
environment, preprocessing, checkpoints and all observed paper-score deltas are
disclosed, and the values are not used for absolute cross-method ranking. The
factorial mechanism contrasts are admitted because their matched controls and
inverse checks passed; this does not convert the absolute baseline into paper
parity or make it suitable for cross-method ranking. GS-CLIP's corrected
endpoint-aligned image-score analysis is reported in
[`../E4/gsclip_depth_identity_image_audit.json`](../E4/gsclip_depth_identity_image_audit.json);
the earlier localization-path audit is retained separately in
[`../E4/gsclip_depth_rebinding_final_audit.json`](../E4/gsclip_depth_rebinding_final_audit.json).
`raw_compact/pointad_three_checkpoint_performance_parity_failed.json` and
`raw_compact/pointad_three_checkpoint_wrapper_parity.json` retain the exact
comparison and wrapper checks.
