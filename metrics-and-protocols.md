# Metrics and Protocols

VLM-grounded industrial anomaly detection papers often report similar metric names under different evidence settings. This page keeps the main distinctions explicit.

## Metrics

| Metric | Typical level | What it measures | Caution |
| --- | --- | --- | --- |
| I-AUROC | image level | ranking of normal and anomalous images | does not establish localization quality or a usable operating threshold |
| I-AP | image level | image-level precision--recall behavior | depends on anomaly prevalence and is not directly comparable across differently composed test sets |
| P-AUROC | pixel level | ranking of normal and anomalous pixels | can remain high despite weak defect-region coverage |
| P-AP / local AP | pixel or anomalous-image level | precision--recall behavior under severe spatial imbalance | the aggregation unit must be stated; dataset-level P-AP and anomalous-image mean P-AP are different estimands |
| PRO / AUPRO | region level | connected-region coverage under false-positive constraints | report the integration limit, for example AUPRO@0.30; source-specific PRO variants are not automatically interchangeable |
| F1 | image, pixel, or reasoning level | thresholded precision-recall trade-off | depends strongly on threshold selection |
| FPR / FNR | image or decision level | false alarms on normal cases and misses on anomalous cases | report how and where the operating threshold was fitted |
| Accuracy | reasoning or classification | correctness of labels or answers | may hide class imbalance and grounding errors |

## Protocol Labels

| Label | Evidence allowed at inference | Typical methods |
| --- | --- | --- |
| Single-image zero-shot | the inspected image and fixed text prompts | prompt-only CLIP scoring, simple VLM scoring |
| Context-enhanced zero-shot | the inspected image plus unlabeled context or online stream context | MuSc, RareCLIP-style context or memory |
| Few-normal-shot | limited normal support images for the target category | WinCLIP few-shot, PromptAD, adapter or prototype methods |
| Adapted CLIP or VLM | prompt, adapter, or projection parameters updated before inference | AnomalyCLIP, AdaCLIP, AA-CLIP |
| Auxiliary-prior fusion | masks, 3D views, frequency features, DINO features, or other priors | CLIP-SAM, PointAD, FE-CLIP, S2SWCLIP |
| Reasoning-level inspection | generated text, retrieved knowledge, logic rules, or tool calls | AnomalyGPT, MMAD, LogicAD, AgentIAD |

## Reporting Rules

- Do not rank methods only by a single number if their evidence protocols differ.
- Report the backbone, input resolution, support budget, memory budget, prompt count, sampling count, and whether context features are precomputed.
- Keep image-level, pixel-level, region-level, and reasoning metrics separate.
- State whether changes use a 0--1 scale or percentage points.
- For paired effects, define the sign convention and the repeated unit used for uncertainty intervals.
- Do not interpret a confidence interval across categories, mappings, support draws, or image clusters as training-seed variability unless independent training runs were actually used.
- For ablations, identify whether the component is removed in isolation or only as part of a coupled pipeline.
- For computational cost, report hardware, latency unit, batch size, memory, and whether preprocessing or support features are cached.
