# Controlled Result Records

This directory contains compact, machine-readable records underlying the controlled experiments. It intentionally excludes datasets, image payloads, raw prediction tensors, caches, and model weights.

| Study | Public records |
| --- | --- |
| E1--E3 | [Controlled intervention ledger](controlled_intervention_ledger.csv), including estimands, effects, confidence intervals, repeated units, validity gates, scope notes, admission status, and the compact source artifact for every row |
| E4 | [PointAD factorial and GS-CLIP endpoint-path audits](E4/README.md) |
| Artifact navigation | [Clickable artifact index](ARTIFACT_INDEX.md) for all unique ledger targets and supporting audit files |

Every non-empty `source_artifact` entry in the controlled intervention ledger is a path relative to this `results/` directory. The referenced JSON, CSV, or Markdown record is included at that exact path. Several ledger rows may point to the same artifact when one compact record contains multiple endpoints or contrasts.

The compact records preserve aggregate effects, resampling summaries, and validity diagnostics. Paths to private intermediate tensors in four E1 boundary records are represented as `private_intermediate_not_redistributed/...`; the underlying `.npz` prediction tensors are intentionally excluded under the repository's data policy.

All effects use intervention minus matched reference. The ledger retains scoped, provisional, and excluded records so that the audit trail is visible; only rows admitted by the paper's stated gates support its numerical conclusions. The paper remains the authoritative source for estimands, confidence-interval units, and interpretation.
