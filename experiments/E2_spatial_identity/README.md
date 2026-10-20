# E2: Feature-to-Coordinate Identity

**Question.** Does localization depend on assigning preserved local evidence to the correct spatial coordinate, proposal, or query?

**Interventions.** Window, patch, dense, or token permutation; FiLo position-state and proposal-box rebinding.

**Methods represented.** WinCLIP, AnomalyCLIP, APRIL-GAN/VAND, Bayes-PFL, and FiLo.

**Primary readouts.** Pixel AUROC, local AP, AUPRO, and image AUROC when the architecture couples local and global outputs.

**Key control.** The local-value multiset is preserved and inverse recovery or an equivalent mapping check is required. Independent image branches are recorded as fixed rather than treated as additional replicates.

Compact result records and plotting inputs will be added after the manuscript tables are frozen.
