# Papers by Evidence Dependency

This page groups representative work by its dominant evidence operation for readability. The groups are not mutually exclusive: machine-readable records may assign a paper to several evidence dependencies.

## Quick Paper and Code Index

Links marked **official** point to repositories maintained by the authors or the project. A community reproduction is shown only when no verified official implementation was found, and is labelled explicitly. “Not verified” means this catalogue does not currently claim that a public author-maintained implementation exists.

| Year | Method | Paper | Implementation |
| --- | --- | --- | --- |
| 2023 | WinCLIP | [paper](https://arxiv.org/abs/2303.14814) | [community reproduction](https://github.com/zqhang/Accurate-WinCLIP-pytorch) (unofficial) |
| 2023 | AnomalyCLIP | [paper](https://arxiv.org/abs/2310.18961) | [official code](https://github.com/zqhang/AnomalyCLIP) |
| 2024 | CLIP-AD | [paper](https://arxiv.org/abs/2311.00453) | [official code](https://github.com/xuhai-chen/CLIP-AD) |
| 2024 | PromptAD | [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Li_PromptAD_Learning_Prompts_with_only_Normal_Samples_for_Few-Shot_Anomaly_CVPR_2024_paper.html) | [official code](https://github.com/FuNz-0/PromptAD) |
| 2024 | AdaCLIP | [paper](https://arxiv.org/abs/2407.15795) | [official code](https://github.com/caoyunkang/AdaCLIP) |
| 2024 | MuSc | [paper](https://arxiv.org/abs/2401.16753) | [official code](https://github.com/xrli-U/MuSc) |
| 2024 | PointAD | [paper](https://arxiv.org/abs/2410.00320) | [official code](https://github.com/zqhang/PointAD) |
| 2024 | AnomalyGPT | [paper](https://arxiv.org/abs/2308.15366) | [official code](https://github.com/CASIA-LMC-Lab/AnomalyGPT) |
| 2025 | Bayes-PFL | [paper](https://arxiv.org/abs/2503.10080) | [official code](https://github.com/xiaozhen228/Bayes-PFL) |
| 2025 | FE-CLIP | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/Gong_FE-CLIP_Frequency_Enhanced_CLIP_Model_for_Zero-Shot_Anomaly_Detection_and_ICCV_2025_paper.html) | Not verified |
| 2025 | RareCLIP | [paper](https://openaccess.thecvf.com/content/ICCV2025/html/He_RareCLIP_Rarity-aware_Online_Zero-shot_Industrial_Anomaly_Detection_ICCV_2025_paper.html) | [official code](https://github.com/hjf02/RareCLIP) |
| 2025 | MMAD | [paper](https://arxiv.org/abs/2410.09453) | [official code and data](https://github.com/jam-cc/MMAD) |
| 2026 | S2SWCLIP | [paper](https://www.nature.com/articles/s41598-026-43044-3) | [official code](https://github.com/Huanzh111/S2SW) |
| 2026 | PromptMoE | [paper](https://arxiv.org/abs/2511.18116) | Not verified |
| 2026 | IndusAgent | [paper](https://arxiv.org/abs/2605.20682) | Not verified |

The machine-readable version of this index, including link status, is maintained in [`data/papers.yml`](data/papers.yml).

## Foundation Models and Dense Readout Precursors

| Year | Paper | Venue or source | Why it matters |
| --- | --- | --- | --- |
| 2021 | Learning Transferable Visual Models From Natural Language Supervision | ICML | CLIP foundation for image-text transfer |
| 2021 | Generic Attention-model Explainability for Interpreting Bi-modal and Encoder-Decoder Transformers | ICCV | Early transformer explanation tool relevant to VLM grounding |
| 2022 | DenseCLIP: Language-Guided Dense Prediction With Context-Aware Prompting | CVPR | Dense language-guided prediction precursor |
| 2022 | Extract Free Dense Labels From CLIP | ECCV | Shows dense supervision signals can be extracted from CLIP-like models |
| 2023 | Segment Anything | ICCV | Mask foundation model used by several auxiliary-prior IAD methods |
| 2023 | DINOv2: Learning Robust Visual Features Without Supervision | arXiv | Self-supervised visual prior for multimodal fusion |
| 2024 | Grounding DINO: Marrying DINO With Grounded Pre-training for Open-Set Object Detection | ECCV | Open-set grounding prior relevant to defect localization |

## State-Interface Semantics

| Year | Paper | Venue or source | Protocol cue |
| --- | --- | --- | --- |
| 2023 | AnomalyCLIP: Object-Agnostic Prompt Learning for Zero-Shot Anomaly Detection | arXiv | object-agnostic state prompts |
| 2023 | Random Word Data Augmentation With CLIP for Zero-Shot Anomaly Detection | arXiv | prompt perturbation and augmentation |
| 2024 | PromptAD: Learning Prompts With Only Normal Samples for Few-Shot Anomaly Detection | CVPR | normal-only prompt learning |
| 2024 | AdaCLIP: Adapting CLIP With Hybrid Learnable Prompts for Zero-Shot Anomaly Detection | ECCV | hybrid learnable prompts |
| 2024 | VCP-CLIP: A Visual Context Prompting Model for Zero-Shot Anomaly Segmentation | ECCV | visual context prompting |
| 2024 | GlocalCLIP: Object-Agnostic Global-Local Prompt Learning for Zero-Shot Anomaly Detection | arXiv | global-local prompt learning |
| 2025 | Bayesian Prompt Flow Learning for Zero-Shot Anomaly Detection | CVPR | prompt uncertainty and sampling |
| 2026 | PromptMoE: Generalizable Zero-Shot Anomaly Detection via Visually-Guided Prompt Mixtures | AAAI | mixture-based semantic prompting |

## Feature-to-Coordinate Identity

| Year | Paper | Venue or source | Protocol cue |
| --- | --- | --- | --- |
| 2023 | WinCLIP: Zero-/Few-Shot Anomaly Classification and Segmentation | CVPR | window-level image-text scoring |
| 2023 | A Zero-/Few-Shot Anomaly Classification and Segmentation Method for CVPR 2023 VAND Challenge Tracks 1 and 2 | VAND Challenge | dense CLIP adaptation |
| 2023 | Anomaly Detection in the Open World: Normality Shift Detection, Explanation, and Adaptation | NeurIPS Workshop | open-world normality and adaptation |
| 2024 | CLIP-AD: A Language-Guided Staged Dual-Path Model for Zero-Shot Anomaly Detection | IJCAI | staged dense alignment |
| 2024 | High-Fidelity Zero-Shot Texture Anomaly Localization Using Feature Correspondence Analysis | WACV | texture localization with feature correspondence |
| 2025 | DHR-CLIP: Dynamic High-Resolution Object-Agnostic Prompt Learning for Zero-Shot Anomaly Segmentation | ICAIIC | high-resolution localization |
| 2026 | S2SWCLIP: Semantic-Optimized Prompts With Spatial-Wavelet Synergy for Zero-Shot Anomaly Detection | Scientific Reports | local semantics with wavelet evidence |

## Target-Reference Validity

| Year | Paper | Venue or source | Protocol cue |
| --- | --- | --- | --- |
| 2023 | WinCLIP: Zero-/Few-Shot Anomaly Classification and Segmentation | CVPR | few-normal-shot support evidence |
| 2024 | PromptAD: Learning Prompts With Only Normal Samples for Few-Shot Anomaly Detection | CVPR | normal-shot prompt optimization |
| 2024 | MuSc: Zero-Shot Industrial Anomaly Classification and Segmentation With Mutual Scoring of the Unlabeled Images | ICLR | unlabeled context and mutual scoring |
| 2024 | FADE: Few-Shot/Zero-Shot Anomaly Detection Engine Using Large Vision-Language Model | arXiv | few-shot LVLM engine |
| 2025 | AA-CLIP: Enhancing Zero-Shot Anomaly Detection via Anomaly-Aware CLIP | CVPR | residual adapter calibration |
| 2025 | AF-CLIP: Zero-Shot Anomaly Detection via Anomaly-Focused CLIP Adaptation | arXiv | anomaly-focused adaptation |
| 2025 | Search Is All You Need for Few-Shot Anomaly Detection | arXiv | retrieval-based scarce evidence |
| 2025 | PA-CLIP: Enhancing Zero-Shot Anomaly Detection Through Pseudo-Anomaly Awareness | arXiv | pseudo-anomaly calibration |
| 2025 | RareCLIP: Rarity-Aware Online Zero-Shot Industrial Anomaly Detection | ICCV | online rarity memory |
| 2026 | Bidirectional Multimodal Prompt Learning With Scale-Aware Training for Few-Shot Multi-Class Anomaly Detection | CVPR | few-shot prompt learning |
| 2026 | AnomalySD: One-for-All Few-Shot Anomaly Detection via Pre-trained Diffusion Models | CVIU | diffusion-assisted calibration |

## Auxiliary Evidence

| Year | Paper | Venue or source | Protocol cue |
| --- | --- | --- | --- |
| 2023 | Segment Any Anomaly Without Training via Hybrid Prompt Regularization | arXiv | SAM-assisted anomaly segmentation |
| 2024 | OV-AS: Zero-Shot/Few-Shot Open-Vocabulary Anomaly Segmentation Based on CLIP | CISCE | open-vocabulary segmentation |
| 2024 | CLIP3D-AD: Extending CLIP for 3D Few-Shot Anomaly Detection With Multi-View Images Generation | arXiv | 3D few-shot with generated views |
| 2024 | PointAD: Comprehending 3D Anomalies From Points and Pixels for Zero-Shot 3D Anomaly Detection | NeurIPS | point-pixel 3D evidence |
| 2025 | CLIPSAM: CLIP and SAM Collaboration for Zero-Shot Anomaly Segmentation | Neurocomputing | CLIP-SAM collaboration |
| 2025 | SAM-LAD: Segment Anything Model Meets Zero-Shot Logic Anomaly Detection | Knowledge-Based Systems | SAM for logic anomaly segmentation |
| 2025 | FE-CLIP: Frequency Enhanced CLIP Model for Zero-Shot Anomaly Detection and Segmentation | ICCV | frequency-enhanced CLIP |
| 2025 | Zero-Shot Industrial Anomaly Segmentation With Image-Aware Prompt Generation | PAKDD | image-aware prompt and segmentation prior |
| 2025 | PointAD+: Learning Hierarchical Representations for Zero-Shot 3D Anomaly Detection | arXiv | hierarchical 3D representation |
| 2026 | SAM-IAD: Injecting Specific Knowledge Into SAM for Industrial Anomaly Detection | Knowledge-Based Systems | SAM with industrial knowledge |
| 2026 | GS-CLIP: Zero-Shot 3D Anomaly Detection by Geometry-Aware Prompt and Synergistic View Representation Learning | CVPR | geometry-aware prompt and view learning |

## Grounded Composition and Inspection Reasoning

| Year | Paper | Venue or source | Protocol cue |
| --- | --- | --- | --- |
| 2024 | AnomalyGPT: Detecting Industrial Anomalies Using Large Vision-Language Models | AAAI | LVLM inspection dialogue |
| 2025 | VMAD: Visual-Enhanced Multimodal Large Language Model for Zero-Shot Anomaly Detection | T-ASE | MLLM anomaly reasoning |
| 2025 | EIAD: Explainable Industrial Anomaly Detection via Multi-Modal Large Language Models | ICME | explainable MLLM inspection |
| 2025 | Think-to-Detect: Rationale-Driven Vision-Language Anomaly Detection | Mathematics | rationale-driven detection |
| 2025 | MMAD: A Comprehensive Benchmark for Multimodal Large Language Models in Industrial Anomaly Detection | ICLR | MLLM benchmark |
| 2025 | KANoCLIP: Zero-Shot Anomaly Detection Through Knowledge-Driven Prompt Learning and Enhanced Cross-Modal Integration | ICASSP | knowledge-driven prompts |
| 2025 | ADSeeker: A Knowledge-Infused Framework for Anomaly Detection and Reasoning | arXiv | knowledge-infused reasoning |
| 2025 | LogicAD: Explainable Anomaly Detection via VLM-Based Text Feature Extraction | AAAI | logic-oriented anomaly explanation |
| 2025 | Towards VLM-Based Hybrid Explainable Prompt Enhancement for Zero-Shot Industrial Anomaly Detection | IJCAI | explainable prompt enhancement |
| 2025 | AgentIAD: Tool-Augmented Single-Agent for Industrial Anomaly Detection | arXiv | tool-augmented agent |
| 2026 | InsightX Agent: An LMM-Based Agentic Framework With Integrated Tools for Reliable X-Ray NDT Analysis | IEEE Transactions on Reliability | agentic NDT analysis |
| 2026 | IndusAgent: Reinforcing Open-Vocabulary Industrial Anomaly Detection With Agentic Tools | arXiv | agentic tool use |

## Future-Work References

| Theme | Representative references |
| --- | --- |
| Calibration and uncertainty | Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift; A Survey of Uncertainty in Deep Neural Networks |
| Faithful localization | Sanity Checks for Saliency Maps |
| Online adaptation | A Survey on Concept Drift Adaptation; Data Stream Mining: Methods and Challenges for Handling Concept Drift; A Comprehensive Survey of Continual Learning |
| Operator feedback | Active Learning Literature Survey; Active Learning-Based Isolation Forest; Human in the AI Loop via XAI and Active Learning for Visual Inspection; Guidelines for Human-AI Interaction |
| Multimodal routing | Outrageously Large Neural Networks; Switch Transformers; Tackling Multimodal Learning Challenges With Mixture-of-Expert |
| Grounded reasoning and privacy | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks; Advances and Open Problems in Federated Learning; Membership Inference Attacks Against Machine Learning Models; Extracting Training Data From Large Language Models |
