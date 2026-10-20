# Model Zoo and Artifact Registry

This page records the exact model source used by the paper companion. It is an access registry, not a redistribution of third-party weights.

## Status Legend

| Status | Meaning |
| --- | --- |
| Official release | Use the upstream authors' checkpoint |
| Trained in this study | Final checkpoint produced by the controlled study |
| Pending upload | Admitted result; Hugging Face upload/link is not yet frozen |
| Pending final gate | Experiment or checkpoint selection is still being validated |
| Excluded after final gate | Execution completed, but the registered intervention-to-endpoint gate failed |
| Released-output analysis | Analysis uses authors' prediction records, not a local checkpoint |
| Not redistributed | Licensing or size policy requires use of the upstream host |

## Checkpoints Trained in This Study

Only final paper-supporting checkpoints will be uploaded. Optimizer states, redundant intermediate epochs, datasets, and caches are intentionally omitted.

| Method | Study | Training unit | Planned artifact | Status | Link |
| --- | --- | --- | --- | --- | --- |
| Bayes-PFL | E2 | seeds 333/444/555; 30 epochs | three final checkpoints and compact configs | Pending upload | -- |
| PromptAD | E3 | three independent runs; K=4 | three final checkpoints and configs | Pending upload | -- |
| IIPAD | E3 | seed 4; K=1; 20 epochs | final checkpoint and config | Pending upload | -- |
| BTP-3DAD | E4 | three independently trained checkpoints | three selected checkpoints and configs | Pending upload | -- |
| PointAD | E4 | three-checkpoint RGB-identity $\times$ correspondence factorial | three final checkpoints and compact configs | Pending upload | -- |
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

The intended single repository contains a root README and manifest, followed by one directory for each paper-supporting trained method: Bayes-PFL, PromptAD, IIPAD, BTP-3DAD, and PointAD. GS-CLIP's compact audit record is retained with the results, but its checkpoints are not selected for upload because its registered endpoint-path gate failed.

Each method directory should contain the final weight file(s), the minimal evaluation configuration, and a short model card recording dataset protocol, training seed, source commit, and the paper table supported by the artifact.
