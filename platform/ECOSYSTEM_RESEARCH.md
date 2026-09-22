# Ecosystem Research Snapshot — 2026-09-22

## Genomics execution ecosystem

### nf-core / Nextflow
- nf-core/sarek 3.10.0 is the current stable release for WGS/WES/targeted germline and somatic variant analysis.
- nf-core/variantbenchmarking 1.5.0 is the current stable benchmark workflow for variant-calling evaluation.
- nf-core documentation explicitly recommends pinning numeric pipeline releases for reproducibility.
- A recent community AI-agent pattern uses runtime retrieval of nextflow_schema.json and samplesheet schemas instead of hardcoding every pipeline interface. This is the pattern adopted for KNN: registry metadata is versioned, while pipeline parameter schemas should be fetched and validated at execution time.

Primary references:
- https://nf-co.re/sarek
- https://nf-co.re/variantbenchmarking
- https://github.com/NathanSkene/claude-nextflow-skill

### NVIDIA BioNeMo Agent Toolkit
NVIDIA's BioNeMo Agent Toolkit packages life-science capabilities as callable agent skills, including genomics analysis, sequence analysis, protein design, molecular docking and biomarker workflows. This is relevant to KNN as an external tool/skill adapter rather than as the core orchestrator.

Primary reference:
- https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit

### NVIDIA Genomic Analysis
NVIDIA's current Genomic Analysis developer example combines GPU-accelerated alignment/variant calling through Parabricks with CodonFM-based variant-effect prediction. This should be treated as a candidate acceleration backend and benchmark target, not as an unqualified default.

Primary reference:
- https://build.nvidia.com/nvidia/genomics-analysis

## Agent architecture implications

1. KNN should own the scientific contract, evidence ledger, governance and claim gates.
2. Nextflow/nf-core should own reproducible workflow execution where appropriate.
3. Domain tools and model services should be adapters behind the KNN tool/model gateway.
4. NVIDIA BioNeMo should enter through an audited skill/tool adapter.
5. Runtime pipeline schemas should be fetched from the pinned pipeline release and validated before execution.
6. Public benchmark execution must remain separate from confidential/company data paths.
7. Benchmark results are evidence for a task/regime; they are not universal model rankings.

## Current blockers

- Windows host has Java 17 but no Docker Desktop, Nextflow or nf-core executable on PATH.
- Therefore the genomics execution planner is operational and tested, but a real Nextflow containerized smoke run is not yet verified.
- The platform gateway and n8n compose definitions exist as scaffolding; Docker runtime availability is still an environment gate.

## Next platform phase

A. Stabilize the provider/model gateway contract.
B. Add provider adapters without coupling agent logic to any provider.
C. Add capability/privacy/cost/reliability routing and budget enforcement.
D. Add benchmark records and regression tests for routing decisions.
E. Connect n8n only to approved control-plane operations.
F. Add GitHub ecosystem discovery and provider catalog monitoring as proposal-producing workflows.
G. Keep all external writes, publication, production prompt changes and tool-permission changes behind human approval.
