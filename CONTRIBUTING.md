# Contributing

Thank you for helping maintain this research resource.

## Adding or Correcting a Paper

Please include:

- official paper title, year, and venue or source;
- paper and official code/project links when available;
- one or more evidence dependencies;
- inspection setting, datasets, and metrics;
- a short protocol note;
- the source of any displayed numerical value.

Evidence dependencies are non-exclusive:

- state-interface-semantics
- spatial-identity
- target-reference-validity
- auxiliary-evidence
- grounded-composition
- benchmark-or-dataset
- future-reference

## Quality Rules

- Add only verifiable papers, official project pages, or stable preprints.
- Do not report a metric without its dataset, task level, and protocol setting.
- Do not merge zero-shot, few-shot, online, adaptation, and reasoning protocols into one ranking.
- Prefer original-source values. If a number comes from a later comparison table, identify that source.
- Keep official method names and distinguish official from unofficial implementations.
- Do not commit datasets, checkpoints, caches, or large raw prediction files.

## Pull Request Checklist

- [ ] The relevant evidence dependency or dependencies are selected.
- [ ] The protocol setting is explicit.
- [ ] Paper and code links were checked.
- [ ] Dataset and metric names are explicit.
- [ ] Numerical provenance is recorded.
- [ ] The structured catalogue is updated when appropriate.
