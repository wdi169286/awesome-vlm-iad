# Controlled Evidence Stress Tests

The controlled studies ask whether an evidence path is decision-active under a matched intervention. They complement source-reported benchmark numbers; they are not a new pooled leaderboard.

| Study | Dependency | Intervention family | Directory |
| --- | --- | --- | --- |
| E1 | State-interface semantics | text errors, state/checkpoint mismatch, description rebinding | [E1](E1_state_semantics/README.md) |
| E2 | Feature-to-coordinate identity | value-preserving permutation and identity rebinding | [E2](E2_spatial_identity/README.md) |
| E3 | Target-reference validity | contamination, cross-category support, memory misbinding | [E3](E3_reference_validity/README.md) |
| E4 | Auxiliary and compositional evidence | removal, corruption, rebinding, reasoning/tool comparison | [E4](E4_auxiliary_composition/README.md) |

## Admission Rule

A contrast enters the final paper bundle only after its paired cohort, replay or recovery requirement, and intervention-specific validity checks pass. Fixed-weight studies use mappings, support draws, or evaluation clusters as repeated units; training studies use independent runs where the design estimates training variability.

## Public Artifact Scope

Public directories contain compact aggregate tables, audit manifests, and analysis scripts. The frozen E4 bundle is available under [results/E4](../results/E4/README.md). Large raw outputs and checkpoints are kept outside Git; checkpoint access is recorded in [MODEL_ZOO.md](../MODEL_ZOO.md).
