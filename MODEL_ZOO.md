# Model Zoo and Artifact Registry

This page records the exact model source used by the paper companion. It is an access registry, not a redistribution of third-party weights.

## Status Legend

| Status | Meaning |
| --- | --- |
| Official release | Use the upstream authors' checkpoint |
| Trained in this study | Final checkpoint produced by the controlled study |
| Hosted artifact | Final study checkpoint is available from the companion Hugging Face repository |
| Aggregate only | The retained run supports the aggregate, but no portable standalone checkpoint is published |
| Pending final gate | Experiment or checkpoint selection is still being validated |
| Excluded after final gate | Execution completed, but the registered intervention-to-endpoint gate failed |
| Released-output analysis | Analysis uses authors' prediction records, not a local checkpoint |
| Not redistributed | Licensing or size policy requires use of the upstream host |

## Checkpoints Trained in This Study

Only final paper-supporting checkpoints are uploaded. Optimizer states, redundant intermediate epochs, datasets, and caches are intentionally omitted. The complete bundle, manifest, and checksums are hosted at [DiHugoWang/awesome-vlm-iad-checkpoints](https://huggingface.co/DiHugoWang/awesome-vlm-iad-checkpoints).

| Method | Study | Training unit | Published artifact | Status | Link |
| --- | --- | --- | --- | --- | --- |
| Bayes-PFL | E2 | seeds 333/444/555; 30 epochs on each dataset | six selected MVTec AD/VisA checkpoints | Hosted artifact | [files](https://huggingface.co/DiHugoWang/awesome-vlm-iad-checkpoints/tree/main/Bayes-PFL) |
| PromptAD | E3 | three independent runs; K=4 | compact aggregate documentation; retained runs do not expose portable standalone final weights | Aggregate only | [E3 protocol](experiments/E3_reference_validity/README.md) |
| IIPAD | E3 | seed 4; K=1; 20 epochs | epoch-19 checkpoint | Hosted artifact | [files](https://huggingface.co/DiHugoWang/awesome-vlm-iad-checkpoints/tree/main/IIPAD) |
| BTP-3DAD | E4 | three independently trained checkpoints | seed-0/1/2 selected checkpoints | Hosted artifact | [files](https://huggingface.co/DiHugoWang/awesome-vlm-iad-checkpoints/tree/main/BTP-3DAD) |
| PointAD | E4 | three-checkpoint RGB-identity $\times$ correspondence factorial | carrot/cookie/dowel epoch-15 checkpoints | Hosted artifact | [files](https://huggingface.co/DiHugoWang/awesome-vlm-iad-checkpoints/tree/main/PointAD) |
| GS-CLIP | E4 boundary | carrot/cookie/dowel; stage 1 and stage 2 | no upload planned because the registered endpoint-path gate failed | Excluded after final gate | -- |

## Official or Fixed Checkpoints Used

Exact upstream URLs and immutable revisions will be filled after link verification. Until then, the cited official repository or model release remains authoritative.

| Method | Use in companion | Weight source | Redistribution |
| --- | --- | --- | --- |
| WinCLIP / WinCLIP+ | E1, E2, E3 | pretrained OpenAI CLIP | Not redistributed |
| APRIL-GAN/VAND | E1, E2 | authors' released checkpoint | Link only |
| AnomalyCLIP | E1, E2; epochs 12--15 where applicable | authors' released checkpoints | Link only |
| AdaCLIP | E1 | authors' released checkpoint | Link only |
| FiLo | E1, E2 | authors' released checkpoint | Link only |
| InCTRL | E3 | authors' released checkpoint | Link only |
| SAA+ | E4 | released pretrained proposal and SAM components | Link only |
| AnomalyR1 | E4 | released 3B base and GRPO-tuned checkpoints | Link only |
| AD-Copilot | E4 | released 7B base and Thinking checkpoints | Link only |

## Released Outputs Without Local Checkpoint Execution

| Method | Study | Artifact used | Local model execution |
| --- | --- | --- | --- |
| AnomalyClaw | E4 | authors' released per-record direct and tool-fused predictions | No local 27B rerun |

## Hugging Face Layout

The published repository contains a root model card, `artifact_manifest.json`, and `SHA256SUMS`, followed by directories for Bayes-PFL, IIPAD, BTP-3DAD, and PointAD. It also includes the compact final PointAD and GS-CLIP E4 audit records. PromptAD is represented by compact aggregates in this GitHub companion rather than by a potentially misleading standalone weight. GS-CLIP checkpoints are not published because its registered endpoint-path gate failed.

Each method directory contains the selected final weight file(s) and a short model card recording the supported study. File sizes and immutable SHA-256 digests are recorded in the Hub manifest.
