# E5: Long-Tail and Domain-Shift Stability

This directory contains the compact aggregate records for the registered E5 extension. All effects are intervention minus reference on the 0--1 scale; the percentages below multiply them by 100.

## LTAD-MVTec

All 300 WinCLIP+ category--draw--condition configurations completed. Under the exponential-200 split, limited references reduce macro I-AUROC by `-0.624 pp [-1.681,-0.008]` and macro I-AP by `-0.265 pp [-0.712,+0.016]` relative to nested `K=16` references. Under step-200, the corresponding effects are `-1.769 pp [-3.397,-0.517]` and `-0.683 pp [-1.285,-0.195]`. Head categories are unchanged because they already have at least 16 official references; the loss is confined to tail categories. The WinCLIP `K=0` negative control has exactly zero split-intervention effect because it does not consume target references and the official test set is unchanged.

The head/tail audit uses complete frequency groups nearest to half the categories and never splits a tie. This corrects one preregistration-metadata error in step-200: all eight one-reference categories, including `cable`, are tail categories. The support and query cohorts are byte-identical before and after this metadata-only correction.

Files:

- `summary.json`: macro, micro, head/tail, worst-group, bottom-quartile, and paired hierarchical-bootstrap results.
- `paired_category_draw.csv`: 150 paired category/draw contrasts.
- `k0_negative_control.json`: deterministic zero-shot control.
- `completion_audit.json`: 300/300 completeness and duplicate check.
- `design_audit.json` and `stratum_correction_audit.json`: official counts, tie-preserving strata, and cohort-preservation checks.

## AeBAD-S

All 30 registered test and calibration archives completed. Across the four official domains, WinCLIP+ `K=4` versus WinCLIP `K=0` changes I-AUROC by `+4.362 pp [2.450,6.545]`, I-AP by `+2.598 pp [1.559,3.723]`, normal FPR by `-0.349 pp [-3.210,2.872]`, and anomaly FNR by `-8.557 pp [-13.729,-3.897]`. K0 and every K4 draw use the same fixed 32-image normal calibration cohort, which is disjoint from the union of all support draws. Thus reference evidence improves ranking and reduces misses, while the matched normal-FPR interval includes zero.

Files:

- `summary.json`: macro/micro endpoints, worst domain, cross-domain variance, and paired hierarchical-bootstrap effects.
- `per_domain_draw.csv`: the 20 domain/draw pairs and frozen calibration thresholds.
- `completion_audit.json`: 30/30 completeness check.
- `design_audit.json`: official domain and defect counts after hidden metadata files are excluded.

Raw image payloads, full anomaly maps, datasets, and model weights are intentionally excluded.
