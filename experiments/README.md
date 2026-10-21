# Controlled Evidence Stress Tests

The controlled studies ask whether an evidence path is decision-active under a matched intervention. They complement source-reported benchmark numbers; they are not a new pooled leaderboard.

| Study | Dependency | Intervention family | Directory |
| --- | --- | --- | --- |
| E1 | State-interface semantics | text errors, state/checkpoint mismatch, description rebinding | [E1](E1_state_semantics/README.md) |
| E2 | Feature-to-coordinate identity | value-preserving permutation and identity rebinding | [E2](E2_spatial_identity/README.md) |
| E3 | Target-reference validity | contamination, cross-category support, memory misbinding | [E3](E3_reference_validity/README.md) |
| E4 | Auxiliary and compositional evidence | removal, corruption, rebinding, reasoning/tool comparison | [E4](E4_auxiliary_composition/README.md) |
| E5 | Long-tail and domain-shift stability | unequal reference access and named acquisition shifts | [E5](E5_long_tail_domain_shift/README.md) |

## Admission Rule

A contrast enters the final paper bundle only after its paired cohort, replay or recovery requirement, and intervention-specific validity checks pass. Fixed-weight studies use mappings, support draws, or evaluation clusters as repeated units; training studies use independent runs where the design estimates training variability.

## Public Artifact Scope

Public directories contain compact aggregate tables, audit manifests, and analysis scripts. Frozen bundles are available for [E4](../results/E4/README.md) and [E5](../results/E5/README.md). Large raw outputs and checkpoints are kept outside Git; checkpoint access is recorded in [MODEL_ZOO.md](../MODEL_ZOO.md).

## Companion Code Currently Released

| Script | Purpose |
| --- | --- |
| [`aggregate_pointad_gsclip_final.py`](E4_auxiliary_composition/aggregate_pointad_gsclip_final.py) | Rebuild the final PointAD factorial aggregate and GS-CLIP endpoint-path audit from compact input records |
| [`verify_e5_records.py`](E5_long_tail_domain_shift/verify_e5_records.py) | Verify E5 completion gates and manuscript-facing effects against the compact paired records |

This list describes code authored for the companion study. Implementations owned by prior papers are not copied into this repository; verified upstream links are maintained in the [paper and code index](../papers.md#quick-paper-and-code-index).
