# E4 Result Bundle

This bundle freezes the final PointAD and GS-CLIP decisions used by the manuscript.

| File | Purpose |
| --- | --- |
| `paper_effects.csv` | Compact manuscript-facing effect table |
| `pointad_factorial_final_audit.json` | Admission decision, effects, intervals, and validity gates |
| `pointad_aggregate_factorial.json` | Full three-checkpoint factorial aggregate |
| `gsclip_depth_rebinding_final_audit.json` | Original localization-endpoint audit showing that depth patches do not construct the released localization maps |
| `gsclip_depth_identity_image_audit.json` | Corrected image-path effects, intervals, and validity gates |

PointAD is admitted as an implementation-scoped E4 analysis: all 27 run--held-out-category controls passed, including exact inverse recovery and branch isolation. GS-CLIP completed 21/21 planned units. Its depth features enter the image-score path, for which the corrected audit reports small intervals that cross zero; its structurally independent localization maps are retained as negative controls rather than target endpoints.

Rebuild the two audit summaries with [`aggregate_pointad_gsclip_final.py`](../../experiments/E4_auxiliary_composition/aggregate_pointad_gsclip_final.py) using the private raw run roots documented in the script. The public audit files are sufficient to inspect the final admission logic without downloading multi-gigabyte intermediate tensors.
