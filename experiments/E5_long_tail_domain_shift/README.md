# E5: Long-Tail and Domain-Shift Stability

**Question.** Do zero-shot semantic evidence and few-shot reference evidence remain stable when target normal references are long-tailed or acquisition conditions shift?

**LTAD-MVTec design.** The official exponential-200 and step-200 LTAD-MVTec training splits define per-category normal-reference availability. WinCLIP+ uses either the available official references capped at `K=16` (`limited`) or a nested `K=16` reference set (`matched-rich`). Five paired draws are evaluated for every category. The unchanged MVTec AD test cohort permits paired category/draw contrasts and a reused WinCLIP `K=0` negative control. Reported endpoints include macro and micro image AUROC/AP, head/tail strata, the worst category, the bottom performance quartile, and hierarchical bootstrap intervals.

**AeBAD-S design.** The official same-domain, background, illumination, and view test groups are evaluated with WinCLIP (`K=0`) and WinCLIP+ (`K=4`, five draws). Operating thresholds are fitted as the 95th percentile of one fixed 32-image normal calibration cohort shared by K0 and every K4 draw; the cohort is disjoint from the union of all support draws. Reported endpoints include macro and micro image AUROC/AP, normal FPR, anomaly FNR, the worst domain, cross-domain variance, and paired hierarchical bootstrap intervals.

**Scope.** E5 is a bounded evidence-stability extension, not a cross-method leaderboard. LTAD-MVTec isolates unequal normal-reference access; AeBAD-S isolates named acquisition shifts. Neither dataset is relabeled to manufacture a synthetic long tail or domain definition.

Compact manifests, aggregates, completion audits, and checksums are released under [`results/E5/`](../../results/E5/); all registered configurations passed their completeness and cohort checks. Datasets, model weights, and raw image payloads are excluded.

Run `python verify_e5_records.py` from this directory with Python 3 and NumPy to recompute the completion gates, paired-record counts, metadata-only stratum correction, negative control, hierarchical-bootstrap intervals, macro and stratum summaries, domain statistics, and manuscript-facing rounded values from the compact CSV/JSON bundle.
