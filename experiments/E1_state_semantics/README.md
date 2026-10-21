# E1: State-Interface Semantics

**Question.** Does the inspection decision depend on the normal--abnormal state information presented to the model?

**Interventions.** Natural-language state errors, learned-state checkpoint/source mismatches, and frozen-path fine-grained description rebinding.

**Methods represented.** WinCLIP, APRIL-GAN/VAND, AnomalyCLIP, AdaCLIP, and FiLo.

**Primary readouts.** Image ranking metrics, signed score margin where applicable, localization metrics for FiLo, and frozen-threshold error rates for explicit text interventions.

**Key control.** Query images, visual processing, prompt structure, and unaffected model paths remain matched within a contrast.

Final compact records are indexed in the [controlled-intervention ledger](../../results/controlled_intervention_ledger.csv) and [artifact index](../../results/ARTIFACT_INDEX.md). These records provide the reported effects and intervals, repeated units, validity gates, and source-artifact paths used by the frozen manuscript tables.
