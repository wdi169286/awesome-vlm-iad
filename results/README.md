# Controlled Result Records

This directory contains compact, machine-readable records underlying the controlled experiments. It intentionally excludes datasets, image payloads, raw prediction tensors, caches, and model weights.

| Study | Public records |
| --- | --- |
| E1--E3 | [Controlled intervention ledger](controlled_intervention_ledger.csv), including estimands, effects, confidence intervals, repeated units, validity gates, scope notes, and admission status |
| E4 | [PointAD factorial and GS-CLIP endpoint-path audits](E4/README.md) |

All effects use intervention minus matched reference. The ledger retains scoped, provisional, and excluded records so that the audit trail is visible; only rows admitted by the paper's stated gates support its numerical conclusions. The paper remains the authoritative source for estimands, confidence-interval units, and interpretation.
