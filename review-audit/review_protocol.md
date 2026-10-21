# Review Protocol

## Scope and discovery

The review covers primary studies published from January 2021 through October 16, 2026 in which a vision--language component contributes to a zero- or few-shot industrial anomaly-inspection output. OpenAlex was the principal discovery source. Candidate discovery was supplemented by the manuscript bibliography, backward and forward citation checking, DOI and publisher verification, and targeted searches in Google Scholar, IEEE Xplore, Scopus, and Web of Science. Licensed exports and provider-native result pages are not redistributed.

### OpenAlex search record

All seven OpenAlex searches covered publications from January 1, 2021 through October 16, 2026 and were executed on October 16, 2026 (America/Chicago). Counts are before cross-query deduplication.

| Query ID | Exact query | Records retrieved |
| --- | --- | ---: |
| Q1 | `industrial anomaly detection vision language` | 295 |
| Q2 | `industrial anomaly detection CLIP` | 214 |
| Q3 | `industrial defect detection vision language` | 173 |
| Q4 | `industrial anomaly detection multimodal foundation model` | 54 |
| Q5 | `zero shot industrial anomaly detection vision language` | 317 |
| Q6 | `few shot industrial anomaly detection vision language` | 277 |
| Q7 | `large vision language model industrial anomaly inspection` | 136 |

The searches returned 1,466 query-level records in total. After cross-query merging and integration with the bibliography-based supplementary discovery set, 952 unique candidates entered screening.

## Record consolidation

Records were merged using DOI, arXiv identifier, and normalized title. Uncertain matches and multiple versions of the same work were inspected manually, with the most complete eligible version retained.

## Selection rules

A core study must evaluate an industrial inspection setting, use a zero- or few-shot target-data protocol, include a vision--language component that affects the inspection decision, and report an image, pixel, region, point, or structured inspection output. Fully supervised target-domain studies, non-industrial evaluations, vision-only methods, secondary studies, and records without an eligible inspection output were excluded from the core corpus. Relevant background studies were retained only as contextual records. `unclear` denotes a report for which the available source did not support a final eligibility decision.

## Study flow

The audit contains 952 deduplicated candidates. Of these, 424 advanced to full-text assessment. Fifteen remained unavailable or protocol-unresolved. Among the 409 assessable reports, 127 were excluded and 282 entered the core corpus.

## Screening reliability

One author screened all title--abstract records. A second author independently screened a fixed 95-record subset using `include`, `exclude`, and `unclear`. Agreement was calculated from these independent decisions before discussion or full-text resolution. The coders agreed on 85 of 95 records (89.5%; Cohen's kappa = 0.834), and the ten disagreements were resolved jointly.

## Public audit files

`screening_audit.csv` provides candidate-level decisions and the independent labels for the reliability subset. `evidence_path_audit.csv` records the evidence-path coding and source provenance for included studies.
