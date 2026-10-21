# Review Audit Data

This directory contains the frozen screening and evidence-path audit tables for the survey.

## Files

- `review_protocol.md`: concise review scope, selection rules, deduplication procedure, study flow, and reliability design.

- `screening_audit.csv`: one row per deduplicated candidate record, including the final screening decision, exclusion reason where applicable, and the two independent title--abstract decisions for the reliability sample. The two coder columns record title--abstract screening only. The first author assigned `final_decision` after assessing the available full text or official source information, so it may differ from either preliminary decision.

- `evidence_path_audit.csv`: records each applicable evidence path for every included method setting (zero- or few-shot). Each row identifies the setting, the affected model output, the matched test used or proposed to examine that path, and the supporting source location.

## Audit-field interpretation

In `evidence_path_audit.csv`, `verified` means that the recorded primary-source material supports the evidence-path assignment at the stated provenance level. It does not indicate independent experimental validation or imply that the source paper reported a corresponding ablation. The `anchor_level` field distinguishes an exact full-text location, a full-text summary, an official primary-source record, and an official abstract.

Exact OpenAlex queries, search dates, and retrieval counts are reported in `review_protocol.md`. Google Scholar, IEEE Xplore, Scopus, and Web of Science were used for supplementary discovery, citation checking, and source verification; provider-native result pages and licensed exports are not redistributed.

## Snapshot

- Candidate records: 952
- Included core studies: 282
- Configuration--question records: 736
- Unique paper--question occurrences: 673
- Independently screened reliability sample: 95 records
- Exact pre-adjudication agreement: 85/95 (89.5%)
- Cohen's kappa: 0.834

Evidence paths are non-exclusive. A paper may therefore contribute multiple configurations or evidence questions. `unclear` indicates that the available information was insufficient for a final screening decision.
