# Genomics Agent Execution Layer

The genomics module is an execution-planning and controlled-execution layer, not a text-only genomics advisor.

## Implemented

- Contract validation for project, data access, reference lock, workflow version, QC, benchmark, provenance and claim gate.
- Deterministic pipeline selection from a versioned JSON registry.
- Pinned nf-core/sarek and nf-core/variantbenchmarking execution plans.
- Benchmark-first execution mode with `-resume`.
- Public-data boundary: public execution rejects included human genomic data.
- Clinical-claim boundary: clinical claims are rejected by the research execution layer.
- Deterministic evidence grading for validated public/test-data runs.
- Unit tests covering execution behavior and evidence grading.

## Current verified pipeline records

- nf-core/sarek **3.10.0** ºw^~)Þt WGS/WES/targeted germline/somatic variant analysis.
- nf-core/variantbenchmarking **1.5.0**"éÝyø§yÔ independent variant-calling benchmark workflow.

Versions are pinned deliberately for reproducibility.

## Runtime boundary

The authoritative execution environment is now **Ubuntu-Local / WSL2**. The validated environment uses Java 17, Docker Engine 29.1.3, approximately 4 vCPU, 3.8 GiB RAM and 1 GiB swap. Nextflow 25.04.0 is used for nf-core/variantbenchmarking 1.5.0 because the latter exhibited DSL compatibility problems under Nextflow 26.04.6; the version choice is therefore explicit and evidence-backed rather than globally changing the platform runtime.

The repository itself is maintained at `/opt/knn-research-agent` on the Linux filesystem for execution performance. The Windows copy under `C:\GPT_Project\` remains an access/synchronization surface, not the preferred workflow work directory.

## Verified public-data gates

### Sarek 3.10.0

A controlled Sarek public/test-data smoke completed successfully on Ubuntu/WSL2. The clean run exited successfully, produced trace/report/timeline artifacts and non-empty outputs, and a subsequent `-resume` validation completed with cached and executed processes. The evidence record is:

`benchmarks/genomics_public_smoke/sarek_run_evidence_2026-09-22.json`

### Variantbenchmarking 1.5.0

The independent public HG002/GRCh37 chr21 structural-variant benchmark completed successfully with exit code 0.

Verified execution state:

- 70 cached processes + 3 executed final-stage processes.
- 0 failed processes.
- 0 aborted processes.
- Trace/report/timeline artifacts present and non-empty.
- MultiQC report present.
- Benchmark summary CSV present.
- Deterministic evidence grader: **PASS**.
- Repository evidence tests: **2 passed** for the variantbenchmarking evidence gate.

Descriptive metrics from the public test dataset:

| Tool | TP_base | FP | TP_comp | FN | Recall | Precision | F1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| delly | 22 | 75 | 22 | 155 | 0.1243 | 0.2424 | 0.1643 |
| lumpy | 21 | 69 | 21 | 156 | 0.1186 | 0.2333 | 0.1573 |
| manta | 65 | 1028 | 65 | 112 | 0.3672 | 0.0595 | 0.1024 |

These values are descriptive outputs of the nf-core public test dataset. They are not clinical-performance claims and do not constitute a ranking of the callers.

Evidence record:

`benchmarks/genomics_public_smoke/variantbenchmarking_run_evidence_2026-09-23.json`

## Governance boundary

The cleared gates apply only to the documented public/test-data execution paths. Human genomic data, patient-derived data, clinical interpretation and clinical claims remain separately blocked until their dedicated privacy, validation, provenance and governance gates are explicitly passed.

## Expected execution sequence

1. Validate execution contract.
2. Resolve and pin workflow version.
3. Lock reference/annotation and input checksums.
4. Run the pipeline's public/test dataset.
5. Run independent benchmark evaluation against an appropriate truth set.
6. Preserve logs, parameters, container/runtime identity and output hashes.
7. Grade the evidence deterministically.
8. Permit publication/IP interpretation only after the relevant validation gates are met.

This module does not make clinical interpretations and does not treat model scores, generated code or automated annotations as experimental evidence.
