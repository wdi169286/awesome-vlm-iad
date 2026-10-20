# E4 Result Bundle

This bundle freezes the final PointAD and GS-CLIP decisions used by the manuscript.

| File | Purpose |
| --- | --- |
| `paper_effects.csv` | Compact manuscript-facing effect table |
| `pointad_factorial_final_audit.json` | Admission decision, effects, intervals, and validity gates |
| `pointad_aggregate_factorial.json` | Full three-checkpoint factorial aggregate |
| `gsclip_depth_rebinding_final_audit.json` | Completed-unit audit and endpoint-path exclusion decision |

PointAD is admitted as an implementation-scoped E4 analysis: all 27 run--held-out-category controls passed, including exact inverse recovery and branch isolation. GS-CLIP completed 21/21 planned units but is not used for a numerical E4 claim because the manipulated depth-patch path does not construct the registered localization endpoints in the released evaluator.

Rebuild the two audit summaries with [`aggregate_pointad_gsclip_final.py`](../../experiments/E4_auxiliary_composition/aggregate_pointad_gsclip_final.py) using the private raw run roots documented in the script. The public audit files are sufficient to inspect the final admission logic without downloading multi-gigabyte intermediate tensors.
