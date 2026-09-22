# Genomics Agent Execution Layer

The genomics module is now an execution-planning layer, not a text-only genomics advisor.

## Implemented

- Contract validation for project, data access, reference lock, workflow version, QC, benchmark, provenance and claim gate.
- Deterministic pipeline selection from a versioned JSON registry.
- Pinned nf-core/sarek and nf-core/variantbenchmarking execution plans.
- Benchmark-first execution mode with -resume.
- Public-data boundary: public execution rejects included human genomic data.
- Clinical-claim boundary: clinical claims are rejected by the research execution layer.
- Unit tests covering the new execution behavior.

## Current verified pipeline records

- nf-core/sarek 3.10.0 — WGS/WES/targeted germline/somatic variant analysis.
- nf-core/variantbenchmarking 1.5.0 — variant-calling benchmark workflow.

Versions are pinned deliberately. The upstream nf-core documentation identifies Sarek 3.10.0 as the current stable release and recommends specifying a numeric release for reproducibility. The variantbenchmarking documentation identifies 1.5.0 as its current stable release.

## Runtime boundary

The agent can generate a reproducible plan and can now reach the local workflow/container runtime through Ubuntu/WSL2. The controlled environment observed in the latest validation is Java 17, Nextflow 26.04.6 and Docker Engine 29.1.3, with approximately 4 vCPU, 3.8 GiB RAM and 1 GiB swap.

A controlled Sarek 3.10.0 smoke reached the intended preprocessing and germline-Strelka orchestration stages, but the current orchestration gate remains open because a clean exit-0 rerun after the disposable smoke patch has not yet been captured. No human genomic data should be used until that gate is explicitly passed.

## Expected execution sequence

1. Validate execution contract.
2. Resolve and pin workflow version.
3. Lock reference/annotation and input checksums.
4. Run the pipeline's public/test dataset.
5. Run independent benchmark evaluation against an appropriate truth set.
6. Preserve logs, parameters, container/runtime identity and output hashes.
7. Permit publication/IP interpretation only after the relevant validation gates are met.

This module does not make clinical interpretations and does not treat model scores, generated code or automated annotations as experimental evidence.
