# Semantic Prior Construction — Results

> **Current interpretation.** Collapse and swap degradation are retained only
> as bounds. The confirmatory E1 panel now uses interpretable natural-language
> state interventions in WinCLIP and APRIL-GAN/VAND: a semantic-content error,
> format-matched irrelevant text, and a meaning-preserving paraphrase. Learned
> state/prototype mismatch remains separately labelled as latent compatibility
> stress. Final claims and admissibility gates are assembled in
> `../main_tables.md`.

| Field | Value |
|---|---|
| Completed independent methods | WinCLIP; AnomalyCLIP; APRIL-GAN/VAND; AdaCLIP |
| Secondary protocol configuration | WinCLIP+ K4, used for support-compensation analysis; not counted as a fourth method |
| Completed datasets | MVTec AD, all 15 categories; VisA, all 12 categories |
| Run | `seed=0`; support `draw=0`; values on 0–1 scale |
| Effect definition | Δ = treatment − matched full reference |
| Uncertainty | 95% category-bootstrap CI, 10,000 repetitions; not a seed CI |
| Sources | `review/results/mvtec15_seed0_v2/`; `review/results/visa12_seed0_v1/` |

## S-summary. Archived descriptive evidence matrix

| Question | Completed evidence | Independent coverage | Result | Boundary / missing cell |
|---|---|---:|---|---|
| Does removing semantic-state separation damage image discrimination? | neutralization/prototype collapse in four implementations | 4 methods × 2 datasets | yes in 8/8 method–dataset units | current collapse conditions are strict sanity bounds |
| Is confidently wrong state evidence worse than missing state evidence? | normal/abnormal reversal versus collapse | 4 methods × 2 datasets | yes in 8/8 units by absolute ΔI-AUROC | natural one-sided mismatch is implementation-dependent and must be reported separately |
| Can target support compensate for weak semantic evidence? | WinCLIP K0 versus WinCLIP+ K4 DiD | 1 method family × MVTec AD | compensation is positive on all four reported endpoints | not yet a cross-method conclusion |
| Is the finding stable beyond fixed/manual states? | AnomalyCLIP learned prototypes and AdaCLIP image-conditioned prompts included | two learned-prompt families | supported within tested scope | distributional/fine-grained prompts remain missing |

| Main-table endpoint | Shared secondary endpoints | Diagnostic-only endpoints still missing |
|---|---|---|
| paired ΔI-AUROC with category-bootstrap CI | ΔI-AP, ΔI-pAUROC@0.05, ΔP-AUROC, ΔP-AP, ΔP-pAUROC@0.05, ΔAUPRO@0.30 | signed normal–anomaly margin and per-image state-reversal rate for all methods |

## S0. AnomalyCLIP official-baseline parity gate

| Dataset | Implementation | I-AUROC (%) | I-AP (%) | P-AUROC (%) | AUPRO (%) | Role in audit |
|---|---|---:|---:|---:|---:|---|
| MVTec AD | Official `test.py`, commit `3911738`, layer 24 | 91.6 | 96.4 | 91.1 | 81.4 | Published-code reproduction reference |
| MVTec AD | Audit adapter, same checkpoint/query | 91.5529 | 96.3555 | 91.0730 | 85.2807 (unified evaluator) | Intervention baseline |

| Parity statistic across 15 categories | P-AUROC | I-AUROC | I-AP | Status |
|---|---:|---:|---:|---|
| Maximum absolute adapter–official difference (percentage points) | 0.0485 | 0.0492 | 0.0410 | Passed; below one-decimal official-table rounding bound |
| AUPRO comparability | — | — | — | Official old AUPRO and unified evaluator differ; official 81.4 is parity-only and is not mixed with intervention effects |

## S1. Completed common-metric response

| Method/configuration | Dataset | Contrast | ΔI-AUROC | ΔI-AP | ΔI-pAUROC@0.05 | ΔP-AUROC | ΔP-AP | ΔP-pAUROC@0.05 | ΔAUPRO@0.30 |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| WinCLIP K0 | MVTec AD | neutral − full | -0.4032 | -0.2334 | -0.3210 | -0.3243 | -0.1484 | -0.1216 | -0.4716 |
| WinCLIP K0 | MVTec AD | swap − full | -0.8065 | -0.4056 | -0.3321 | -0.6129 | -0.1593 | -0.1336 | -0.6141 |
| WinCLIP+ K4 | MVTec AD | neutral − full | -0.0057 | -0.0107 | -0.0308 | +0.0164 | +0.0971 | +0.0508 | +0.0331 |
| WinCLIP+ K4 | MVTec AD | swap − full | -0.5773 | -0.2923 | -0.3611 | -0.1349 | -0.1921 | -0.1183 | -0.2902 |

## S2. Verified primary-effect confidence intervals

| Method/configuration | Contrast | ΔI-AUROC [95% CI] | ΔI-AP [95% CI] | Category direction | Status |
|---|---|---:|---:|---:|---|
| WinCLIP K0 | neutral − full | -0.4032 [-0.4499, -0.3508] | -0.2334 [-0.2783, -0.1918] | 15/15 harmed on both metrics | Completed |
| WinCLIP K0 | swap − full | -0.8065 [-0.8998, -0.7017] | -0.4056 [-0.4594, -0.3466] | 15/15 negative I-AUROC effects | Completed; sanity bound |
| WinCLIP+ K4 | neutral − full | -0.0057 [-0.0170, +0.0074] | -0.0107 [-0.0301, +0.0012] | 10/15 and 11/15 harmed | Completed; CI includes zero |
| WinCLIP+ K4 | swap − full | -0.5773 [-0.7240, -0.4298] | -0.2923 [-0.3803, -0.2020] | 15/15 negative I-AUROC effects | Completed; sanity bound |

## S3. Protocol compensation

| Contrast | ΔI-AUROC DiD [95% CI] | ΔI-AP DiD [95% CI] | ΔP-AUROC DiD [95% CI] | ΔP-AP DiD [95% CI] | ΔAUPRO@0.30 DiD [95% CI] | Categories supporting compensation |
|---|---:|---:|---:|---:|---:|---:|
| (K4 neutral − K4 full) − (K0 neutral − K0 full) | +0.3976 [+0.3498, +0.4415] | +0.2227 [+0.1896, +0.2559] | +0.3408 [+0.2909, +0.3846] | +0.2455 [+0.1905, +0.3036] | +0.5047 [+0.4420, +0.5646] | 15/15 |

## S3b. VisA replication (12 categories)

| Method/configuration | Contrast | ΔI-AUROC [95% CI] | ΔI-AP [95% CI] | ΔI-pAUROC@0.05 [95% CI] | ΔP-AUROC [95% CI] | ΔP-AP [95% CI] | ΔAUPRO@0.30 [95% CI] |
|---|---|---:|---:|---:|---:|---:|---:|
| WinCLIP K0 | neutral − full | -0.2549 [-0.3385, -0.1678] | -0.2265 [-0.2946, -0.1557] | -0.1445 [-0.2225, -0.0744] | -0.2262 [-0.3169, -0.1283] | -0.0370 [-0.0763, -0.0107] | -0.3725 [-0.5059, -0.2351] |
| WinCLIP K0 | swap − full | -0.5098 [-0.6712, -0.3370] | -0.3444 [-0.4475, -0.2331] | -0.1511 [-0.2314, -0.0788] | -0.4453 [-0.6224, -0.2498] | -0.0375 [-0.0786, -0.0096] | -0.4888 [-0.6448, -0.3305] |
| WinCLIP+ K4 | neutral − full | +0.0062 [-0.0187, +0.0336] | +0.0054 [-0.0174, +0.0309] | -0.0093 [-0.0490, +0.0305] | +0.0172 [+0.0037, +0.0304] | +0.0616 [+0.0197, +0.1078] | +0.0105 [-0.0046, +0.0248] |
| WinCLIP+ K4 | swap − full | -0.2356 [-0.3462, -0.1346] | -0.1812 [-0.2712, -0.1046] | -0.1929 [-0.2641, -0.1232] | -0.0581 [-0.0976, -0.0222] | +0.0126 [-0.0369, +0.0658] | -0.2279 [-0.3222, -0.1452] |

## S4. Updated first-round result slots

| Method | Dataset | Experiment | Primary endpoint | Result | Status |
|---|---|---|---|---:|---|
| WinCLIP K0 | MVTec AD + VisA | meaning-preserving paraphrase | ΔI-AUROC; paraphrase control | See S4b | Complete, 15/15 and 12/12 categories |
| WinCLIP K0 | MVTec AD + VisA | format-matched irrelevant state text | ΔI-AUROC | See S4b | Complete, 15/15 and 12/12 categories |
| WinCLIP K0 | MVTec AD + VisA | semantic-content error | ΔI-AUROC | See S4b | Complete, 15/15 and 12/12 categories |
| WinCLIP/WinCLIP+ | VisA | neutral / single-pair / swap | common 2D panel | See S3b | Complete and audited; 12/12 categories |
| AnomalyCLIP | MVTec AD | same-domain epoch-12/13/14 state mismatch against epoch 15 / collapse / swap | score margin and ΔI-AUROC | See S6b and S7 | Complete; 15/15 categories, donor epoch recorded |
| AnomalyCLIP | VisA | same-domain epoch-12/13/14 state mismatch against epoch 15 / collapse / swap | score margin and ΔI-AUROC | See S6b and S7 | Complete; 12/12 categories, donor epoch recorded |

### S4b. Confirmatory natural-language state-interface panel

All effects are treatment minus the matched full prompt ensemble. Intervals
are 10,000-repetition category bootstraps; the run has one frozen execution
seed and therefore does not estimate training-seed variation.

| Method | Dataset | Semantic-content error ΔI-AUROC [95% CI] | Format-matched irrelevant ΔI-AUROC [95% CI] | Meaning-preserving paraphrase ΔI-AUROC [95% CI] |
|---|---|---:|---:|---:|
| WinCLIP | MVTec AD | −0.2080 [−0.2925, −0.1263] | −0.3397 [−0.4406, −0.2603] | −0.0210 [−0.0406, −0.0054] |
| WinCLIP | VisA | −0.1538 [−0.2545, −0.0479] | −0.2379 [−0.3816, −0.1142] | +0.0145 [−0.0304, +0.0594] |
| APRIL-GAN/VAND | MVTec AD | −0.3451 [−0.4356, −0.2604] | −0.3158 [−0.4355, −0.2074] | −0.0048 [−0.0296, +0.0180] |
| APRIL-GAN/VAND | VisA | −0.1448 [−0.2315, −0.0808] | −0.2589 [−0.3977, −0.1205] | +0.0169 [−0.0200, +0.0584] |

Semantic-content errors reduced image separation in all four
method–dataset units, whereas the meaning-preserving control was close to zero
in three units. WinCLIP on MVTec AD showed a small but nonzero paraphrase cost;
the paper should therefore report representation- and dataset-dependent
robustness rather than claim complete invariance to wording.

### S4c. Independently calibrated operational error routes

For each category, the threshold is the q95 of official train-normal scores
under the full state description and is then frozen across paired test-query
conditions. Train/test identity overlap was checked to be zero. Effects are
treatment minus full with 10,000 category-bootstrap repetitions.

| Method | Dataset | Δ normal FPR [95% CI] | Δ anomaly FNR [95% CI] | Route summary |
|---|---|---:|---:|---|
| WinCLIP | MVTec AD | +0.5981 [+0.3714, +0.8133] | −0.0926 [−0.3060, +0.1182] | false-alarm increase dominates |
| WinCLIP | VisA | +0.6492 [+0.4059, +0.8609] | −0.3692 [−0.6217, −0.0833] | false alarms increase while misses decrease |
| APRIL-GAN/VAND | MVTec AD | +0.2768 [+0.0700, +0.4989] | +0.2736 [−0.0073, +0.5327] | false alarms increase; miss change unresolved |
| APRIL-GAN/VAND | VisA | +0.5400 [+0.2834, +0.7809] | −0.1992 [−0.4575, +0.0658] | false alarms increase; miss change unresolved |

Thus the reproducible route in this panel is an increase in false alarms, not
a universal increase in missed anomalies. The result is scoped to the two
natural-language state implementations; learned-token compatibility stresses
remain a distinct estimand.

## S5. Metric completion status

| Metric | MVTec WinCLIP existing runs | VisA | AnomalyCLIP |
|---|---|---|---|
| I-AUROC / I-AP | Complete | Complete | Complete on both datasets |
| P-AUROC / P-AP | Complete | Complete | Complete on both datasets |
| I/P-pAUROC@0.05 | Complete | Complete | Complete on both datasets |
| AUPRO@0.30 | Complete | Complete | Complete on both datasets |
| AUPRO@0.05 | Not yet computed | Not yet computed | Complete on both datasets |
| Frozen-threshold normal FPR / anomaly FNR | Not yet computed | Not yet computed | Not run |
| Score margin / paraphrase variance | Not yet computed | Not yet computed | Not run |

## S6. Additional completed official implementations (2026-10-14 audit)

| Method | Dataset | Contrast | ΔI-AUROC [95% category-bootstrap CI] | ΔI-AP [95% CI] | Interpretation |
|---|---|---|---:|---:|---|
| AnomalyCLIP | MVTec AD | semantic collapse − full | −0.4155 [−0.4551, −0.3702] | −0.2406 [−0.2932, −0.1992] | Removing the normal/abnormal distinction harms discrimination |
| AnomalyCLIP | MVTec AD | semantic swap − full | −0.8311 [−0.9103, −0.7403] | −0.4137 [−0.4705, −0.3599] | Reversing state meaning is more harmful than neutralization |
| AnomalyCLIP | VisA | semantic collapse − full | −0.3197 [−0.3823, −0.2516] | −0.2878 [−0.3326, −0.2420] | Replicates on 12 categories |
| AnomalyCLIP | VisA | semantic swap − full | −0.6394 [−0.7647, −0.5033] | −0.4337 [−0.5035, −0.3570] | Replicates on 12 categories |
| APRIL-GAN/VAND | MVTec AD | semantic collapse − full | −0.3612 [−0.4180, −0.2926] | −0.2126 [−0.2575, −0.1654] | Same functional response in a different implementation |
| APRIL-GAN/VAND | MVTec AD | semantic swap − full | −0.7224 [−0.8360, −0.5853] | −0.3573 [−0.4228, −0.2791] | Swap is again more harmful than collapse |
| APRIL-GAN/VAND | VisA | semantic collapse − full | −0.2749 [−0.3550, −0.1935] | −0.2429 [−0.3022, −0.1826] | Replicates on 12 categories |
| APRIL-GAN/VAND | VisA | semantic swap − full | −0.5498 [−0.7101, −0.3870] | −0.3724 [−0.4599, −0.2776] | Replicates on 12 categories |
| AdaCLIP | MVTec AD | semantic collapse − full | −0.4932 [−0.4976, −0.4882] | −0.2740 [−0.3301, −0.2298] | Hybrid static/dynamic learned prompts; 15 categories |
| AdaCLIP | MVTec AD | semantic swap − full | −0.8737 [−0.9235, −0.8087] | −0.4210 [−0.4878, −0.3571] | Swap is more harmful than collapse |
| AdaCLIP | VisA | semantic collapse − full | −0.4381 [−0.4677, −0.4053] | −0.3779 [−0.4126, −0.3449] | Replicates across 12 categories |
| AdaCLIP | VisA | semantic swap − full | −0.8228 [−0.8977, −0.7460] | −0.5524 [−0.5892, −0.5169] | Swap is more harmful than collapse |

The earlier AnomalyCLIP one-sided result used a cross-training-domain donor and is
excluded from the confirmatory ledger.  Its replacement uses correlated
epoch-12/13/14 snapshots from the same official training trajectory as the
epoch-15 reference.  These are compatibility-stress levels, not independent
training seeds and not natural-language semantic substitutions.

AdaCLIP completed the corrected official cross-domain evaluation direction and
path-aware integrity validation for all 1,725 MVTec AD and 2,162 VisA queries.
The registered 2×2 intervention independently rebinds the dynamic text-prompt
source and dynamic visual-prompt source within category and binary query state.
All individual and joint score-margin intervals included zero; therefore this
experiment is a meaningful negative boundary result rather than evidence that
all state-interface perturbations must be harmful.

### S6b. Completed learned-state compatibility stresses

Effects are treatment minus matched. Intervals are 10,000-repetition category
bootstraps. The AnomalyCLIP donors are correlated checkpoints; the AdaCLIP
factorial uses one frozen execution seed.

| Method | Dataset | Contrast | Δ score margin [95% CI] | ΔI-AUROC [95% CI] | Interpretation |
|---|---|---|---:|---:|---|
| AnomalyCLIP | MVTec AD | epoch 12 state / epoch 15 matched | −0.00160 [−0.00397, +0.00006] | −0.00032 [−0.00185, +0.00150] | unresolved at the category level |
| AnomalyCLIP | MVTec AD | epoch 13 state / epoch 15 matched | −0.00556 [−0.00936, −0.00251] | −0.00189 [−0.00378, −0.00035] | small but resolved compatibility loss |
| AnomalyCLIP | MVTec AD | epoch 14 state / epoch 15 matched | −0.00502 [−0.00947, −0.00156] | −0.00406 [−0.00718, −0.00152] | loss is not monotone in epoch distance |
| AnomalyCLIP | VisA | epoch 12 state / epoch 15 matched | −0.00106 [−0.00412, +0.00116] | +0.00007 [−0.00213, +0.00209] | unresolved |
| AnomalyCLIP | VisA | epoch 13 state / epoch 15 matched | −0.00340 [−0.00534, −0.00172] | −0.00547 [−0.01034, −0.00112] | small but resolved compatibility loss |
| AnomalyCLIP | VisA | epoch 14 state / epoch 15 matched | +0.00017 [−0.00238, +0.00272] | −0.00244 [−0.00737, +0.00179] | unresolved |
| AdaCLIP | MVTec AD | dynamic text source mismatch | +0.00146 [−0.00011, +0.00327] | +0.00955 [−0.00263, +0.02287] | no registered loss |
| AdaCLIP | MVTec AD | dynamic visual source mismatch | −0.00003 [−0.00082, +0.00084] | +0.00257 [+0.00057, +0.00490] | margin unresolved; small ranking gain |
| AdaCLIP | MVTec AD | both dynamic sources mismatched | +0.00162 [−0.00030, +0.00389] | +0.00741 [−0.00417, +0.01926] | no registered loss |
| AdaCLIP | VisA | dynamic text source mismatch | +0.00004 [−0.00063, +0.00078] | +0.00375 [−0.00242, +0.01035] | no registered loss |
| AdaCLIP | VisA | dynamic visual source mismatch | −0.00013 [−0.00162, +0.00163] | +0.00913 [+0.00471, +0.01378] | margin unresolved; small ranking gain |
| AdaCLIP | VisA | both dynamic sources mismatched | +0.00010 [−0.00099, +0.00116] | +0.00857 [+0.00405, +0.01315] | margin unresolved; small ranking gain |

The useful cross-method result is heterogeneity: interpretable text-state errors
strongly reduced separation in WinCLIP and APRIL-GAN/VAND, while learned-state
compatibility stresses were small, checkpoint-dependent, or null. This supports
representation-dependent state-interface robustness, not a universal damage law.

## S7. Frozen operating-point boundary audit

AUROC degradation alone does not establish how a semantic intervention changes the operational boundary. For each category, the following diagnostic freezes a threshold at the 95th percentile of the **full-condition normal scores**, then applies that unchanged threshold to the same paired queries under semantic intervention. `Δmargin` is the change in `(mean anomaly score − mean normal score) / SD(full scores)`. Confidence intervals use 10,000 category-bootstrap repetitions. This is a boundary diagnostic, not a deployment threshold estimate.

| Method | Dataset | Collapse Δmargin [95% CI] | Swap Δmargin [95% CI] | Dominant frozen-threshold failure | Legacy cross-domain mismatch Δmargin [95% CI] |
|---|---|---:|---:|---|---:|
| AnomalyCLIP | MVTec AD | −1.4777 [−1.6786, −1.2628] | −2.9553 [−3.3572, −2.5256] | anomaly TPR loss (−0.619/−0.722) | +0.5739 [+0.0988, +1.0830] |
| AnomalyCLIP | VisA | −1.0719 [−1.2978, −0.8330] | −2.1438 [−2.5955, −1.6660] | anomaly TPR loss (−0.510 for both) | +0.7268 [+0.4209, +1.0485] |
| APRIL-GAN/VAND | MVTec AD | −1.2578 [−1.5065, −0.9826] | −2.5156 [−3.0129, −1.9653] | mixed; TPR loss dominates | −0.9281 [−1.3489, −0.4064] |
| APRIL-GAN/VAND | VisA | −0.9047 [−1.1424, −0.6641] | −1.8093 [−2.2849, −1.3283] | normal FPR increase dominates | −0.7270 [−1.0262, −0.4230] |
| AdaCLIP | MVTec AD | −1.9405 [−2.0264, −1.8523] | −2.0142 [−2.0906, −1.9370] | normal FPR increase (+0.804/+0.937) | −0.5274 [−0.6870, −0.3603] |
| AdaCLIP | VisA | −1.5270 [−1.6615, −1.3873] | −2.7790 [−3.6821, −2.1746] | TPR loss for collapse; mixed for swap | +0.0805 [−0.1695, +0.4122] |

The last column is retained only as a legacy diagnostic and is excluded from the
confirmatory ledger because its donor crossed training domains. The valid
same-domain replacement is reported in S6b. The robust cross-implementation
finding is therefore narrower and more informative than “semantic prompts
help”: collapse and swap reduce score separation in all six learned-state
method–dataset units, but compatibility stress is heterogeneous. The **error
route is not universal**—some configurations mainly create false positives
while others mainly suppress anomaly recall. Full per-category values,
frozen-threshold FPR/TPR changes, flip rates and archive hashes are retained
under `raw_compact/boundary/`.
