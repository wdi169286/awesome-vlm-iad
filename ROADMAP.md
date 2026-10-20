# Roadmap

The repository is maintained as a lightweight research resource. Priority is given to useful records and reproducible artifacts rather than repository infrastructure.

## Current Revision

- Align the repository with the paper's five non-exclusive evidence questions.
- Separate source-reported evidence from controlled E1--E4 results.
- Verify paper, code, dataset, official-weight, and released-output links.
- Maintain a checkpoint registry without storing weights in Git.
- Prepare compact manuscript-to-artifact and result records.

## Current Artifact Freeze

- PointAD is admitted as an implementation-scoped E4 factorial and its aggregate is public under `results/E4/`.
- GS-CLIP is retained as a completed endpoint-path boundary audit under `results/E4/`; no numerical E4 effect is claimed.
- The selected study-trained checkpoint bundle is published on Hugging Face; links are frozen in `MODEL_ZOO.md` and `data/checkpoints.yml`.
- Add compact E1--E3 aggregate records and plotting inputs without mirroring raw predictions.
- Add the final paper citation and table/figure index.

## Ongoing Maintenance

- Add newly published VLM-IAD papers with explicit protocol and numerical provenance.
- Correct broken upstream links and method metadata.
- Expand dataset and metric notes when new modalities or evaluation settings appear.
- Keep large checkpoints, datasets, caches, and raw outputs outside Git.
