# Awesome VLM-Grounded Industrial Anomaly Detection

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-blue)

A curated research hub and paper companion for vision-language and multimodal foundation models in industrial anomaly detection (VLM-IAD).

The repository connects three kinds of evidence that are often scattered across papers: the literature landscape, protocol-aware source-reported results, and controlled experiments that test whether particular evidence paths are decision-active.

## Start Here

| Resource | What it provides |
| --- | --- |
| [Papers](papers.md) | Curated literature organized by evidence dependency |
| [Datasets](datasets.md) | Dataset scope, modalities, and inspection questions |
| [Metrics and protocols](metrics-and-protocols.md) | Metric definitions and comparison cautions |
| [Paper companion](paper/README.md) | Map from the manuscript to public tables, figures, and records |
| [Controlled experiments](experiments/README.md) | E1--E4 interventions, validity checks, and result artifacts |
| [Result records](results/README.md) | Compact machine-readable aggregates and final validity audits |
| [Model zoo](MODEL_ZOO.md) | Official weights, study-trained checkpoints, and released-output analyses |
| [Machine-readable catalogue](data/papers.yml) | Structured paper records |

## Evidence-to-Decision Map

The categories below are non-exclusive research questions, not a single-label leaderboard taxonomy. A method may participate in several evidence paths.

| Question | What is tested | Representative operations |
| --- | --- | --- |
| State-interface semantics | How normal and abnormal states are constructed and communicated to the model | fixed prompts, learned prompts, fine-grained descriptions, state compatibility |
| Feature-to-coordinate identity | Whether local evidence remains bound to the correct position, region, or query | window/patch alignment, dense maps, proposal boxes, spatial rebinding |
| Target-reference validity | How normal supports, prototypes, memories, or retrieved references shape the decision boundary | few-shot support, contamination, cross-category binding, retrieval memory |
| Auxiliary evidence | When extra modalities or foundation priors help, fail, or cause negative transfer | masks, geometry, 3D views, frequency cues, proposal refinement |
| Grounded composition | How reasoning, tools, rules, and observations are combined into inspection decisions | reasoning checkpoints, retrieval, tool fusion, structured inspection claims |

## Two Evidence Layers

### Source-reported evidence

The literature catalogue preserves the protocol attached to every result. Values from different shot counts, adaptation settings, metric definitions, or inference access conditions are not silently pooled. A displayed value may come from the original paper or from a cited comparison source; the provenance should remain visible.

### Controlled evidence

The companion experiments use matched interventions to probe four dependencies:

- **E1 -- state-interface semantics:** perturb state descriptions or learned-state compatibility.
- **E2 -- spatial identity:** change feature-to-coordinate or proposal-to-query binding while preserving local values where possible.
- **E3 -- target-reference validity:** contaminate, cross-bind, or misbind normal references.
- **E4 -- auxiliary and compositional evidence:** remove, rebind, or replace an auxiliary, reasoning, or tool path.

See [experiments/README.md](experiments/README.md) for the scope and admission rules. Pending experiments are identified as pending and are not promoted to final conclusions.

## Benchmark Entry Points

| Benchmark | Primary use |
| --- | --- |
| [MVTec AD](https://www.mvtec.com/company/research/datasets/mvtec-ad) | RGB anomaly classification and segmentation |
| [VisA](https://github.com/amazon-science/spot-diff) | Multi-category RGB anomaly detection |
| [MVTec LOCO AD](https://www.mvtec.com/company/research/datasets/mvtec-loco) | Structural and logical anomalies |
| [MVTec 3D-AD](https://www.mvtec.com/company/research/datasets/mvtec-3d-ad) | RGB-D and 3D anomaly detection |

## Checkpoint Policy

Large model files are not stored in Git. [MODEL_ZOO.md](MODEL_ZOO.md) distinguishes:

- official checkpoints linked to their upstream maintainers;
- final paper-supporting checkpoints trained in this study and hosted on Hugging Face;
- analyses based on authors' released outputs rather than a local model execution.

The selected study-trained checkpoints are available from the [companion Hugging Face repository](https://huggingface.co/DiHugoWang/awesome-vlm-iad-checkpoints). Datasets, optimizer states, caches, and redundant intermediate epochs are excluded; the Hub bundle includes an artifact manifest and SHA-256 checksums.

## Comparison Rules

- Keep dataset, task level, shot count, adaptation setting, and metric definition visible.
- Do not combine image AUROC, pixel AUROC, AP, PRO, and reasoning accuracy into one score.
- Distinguish original-source values from values copied by a later comparison paper.
- Treat controlled effects as intervention-specific evidence, not architecture rankings.

## Contributing

Corrections and additions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). A paper may be tagged with more than one evidence dependency when justified.

## Citation

If this repository is useful, please cite the companion survey. The final BibTeX entry will be added after publication.

## Related Resource

This repository is inspired by community-maintained lists such as [M-3LAB/awesome-industrial-anomaly-detection](https://github.com/m-3lab/awesome-industrial-anomaly-detection), while focusing specifically on VLM-grounded and multimodal foundation-model based IAD and its evaluation protocols.
