# Cross-Domain Scientific Ecosystem Review — 2026-09-23

## Scope
This review repeats the Drug Delivery ecosystem discovery with stricter evidence and routing criteria, then applies the same discovery pattern to Genomics/NGS, Neuroscience/BCI, Biomedical Engineering/Advanced Instrumentation, Petroleum/Energy/Industrial R&D, and IP/Technology Foresight.

## Evidence policy
Discovery sources are separated into: primary project repositories, maintained software, benchmark/data infrastructures, peer-reviewed literature, institutional/laboratory sources, and service/tooling sources. Availability is never treated as validity. A candidate enters `use` only when provenance, reproducibility, applicability and an execution/validation path are sufficiently explicit; otherwise it remains `inspect` or `monitor`.

## Drug Delivery — second-pass result
The first ecosystem map was useful but under-modeled the routing layer. The second pass confirms a heterogeneous stack: LNP/formulation datasets and optimizers, therapeutic benchmarks, chemistry tool agents, multi-agent scientific systems, nanoinformatics, molecular simulation, autonomous experimentation, and translational/CMC literature. The architecture therefore needs capability-level routing rather than a single Drug Delivery agent.

Key refinement: every prediction route must carry an applicability domain and an evidence boundary. A formulation prediction cannot silently become a biological, PK, efficacy, safety, CMC or regulatory claim.

## Genomics / NGS
Existing local execution work already provides a strong foundation: pinned nf-core/Sarek 3.10.0 and nf-core/variantbenchmarking 1.5.0, public/test-data smoke execution, independent benchmarking, reference/version locking, and a public human-genomic-data boundary. The ecosystem pass adds explicit routing candidates such as Google DeepVariant, scverse single-cell infrastructure, and public variant/benchmark resources.

Architecture refinement: genomics routing must be reference-build/annotation aware. A model or workflow is not route-compatible merely because its task name matches; reference genome, annotation, assay modality, caller type, truth set, privacy class and compute profile are hard constraints.

## Neuroscience / BCI
The ecosystem separates signal-processing infrastructure, benchmark/challenge datasets, decoding models, BCI application repositories, and hardware/real-time control. MNE-Python is a reusable analysis substrate; PhysioNet challenge infrastructure supplies benchmark-style datasets/tasks. Public EEG/BCI repositories are useful discovery leads but require dataset-level provenance, licensing and preprocessing verification.

Architecture refinement: neuroscience routing must encode acquisition modality, sampling rate, montage/channel schema, preprocessing pipeline, subject/session split strategy and leakage controls. Cross-subject generalization is a separate evidence gate from within-subject performance.

## Biomedical Engineering / Advanced Instrumentation
The ecosystem spans medical imaging, biosignals, patient-specific simulation, biomechanics, CFD, device modeling and instrumentation. SimVascular is a concrete mechanistic simulation candidate. Biomedical signal/image repositories are discovery inputs, not automatically validated benchmarks.

Architecture refinement: instrumentation and biomedical models require a measurement model and calibration/provenance layer. Predicted signal quality, device performance or physiological state must remain distinct from measured evidence.

## Petroleum / Energy / Industrial R&D
Open research infrastructure is more simulation-centric than benchmark-centric. OPM simulators and MRST provide mechanistic reservoir-simulation capabilities; public ML-in-petroleum repositories are useful discovery sources but vary strongly in provenance and maintenance.

Architecture refinement: energy routing must encode physics model, units, PVT assumptions, grid/model provenance, boundary conditions, uncertainty treatment and field-data classification. Proprietary field data must never enter public registry artifacts.

## IP / Technology Foresight
This domain is source- and provenance-heavy rather than model-heavy. Patent databases, citation graphs, classification systems, assignee/inventor/entity resolution and technology-taxonomy tools should be routed as evidence services. Search output is not a legal conclusion.

Architecture refinement: prior-art and freedom-to-operate workflows need a legal/IP review gate, source snapshots, query reproducibility and explicit jurisdiction/filing-date constraints.

## Cross-domain algorithm change
The routing unit is now a `capability record`, not a named agent. A route is accepted only after hard constraints are satisfied and then ranked by transparent evidence metadata. The scoring layer is a routing heuristic, not a scientific validity score.

Hard gates: privacy, license, required capability, status, modality/reference compatibility and explicit safety/IP restrictions.

Soft routing factors: relevance, evidence quality, reproducibility, maintenance, license clarity, uncertainty/applicability fit and integration readiness.

The registry intentionally stores only public-safe metadata. Confidential project payloads remain outside the public repository.
