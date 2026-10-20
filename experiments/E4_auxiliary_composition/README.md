# E4: Auxiliary and Compositional Evidence

**Question.** When does an auxiliary modality, refinement module, reasoning checkpoint, or tool path improve, fail, or harm an inspection decision?

**Interventions.** Geometry removal/corruption, proposal-to-mask interaction, matched reasoning-checkpoint comparison, and direct-versus-tool-fused output analysis.

**Methods represented in admitted analyses.** BTP-3DAD, PointAD, GS-CLIP, SAA+, AnomalyR1, AD-Copilot, and AnomalyClaw.

**Completed depth-identity study.** GS-CLIP completed all 21 clean, depth-rebinding, and inverse-recovery units. The corrected analysis registers image AUROC/AP because the released evaluator consumes depth features in its image-score path, while its localization maps are constructed from rendered-image patch features. Point-path I-AUROC changes by `+0.00048 [-0.00003,+0.00122]` and fused I-AUROC by `+0.00013 [-0.00041,+0.00090]`. RGB-only scores are exactly fixed, localization outputs remain below the `1e-5` control tolerance, and inverse recovery passes. This is an endpoint-aligned near-null result, not evidence of depth-position invariance.

**Primary readouts.** Each method retains its native task endpoint; heterogeneous endpoints are not pooled.

PointAD's complete three-train-class RGB-identity $\times$ point--pixel-correspondence factorial is admitted as an implementation-scoped analysis. The [frozen result bundle](../../results/E4/README.md) contains its full aggregate and final audit, both GS-CLIP endpoint audits, and the manuscript-facing effect table. The aggregation scripts are retained beside this README.
