# Capability Routing Contract

## Purpose
Route a scientific task to the smallest appropriate combination of datasets, software, models, simulations, benchmarks, literature and validation gates.

## Record contract
Each capability record must identify: domain, source type, capabilities, status, license/access, privacy class, provenance, version where applicable, benchmark evidence, maintenance, reproducibility, applicability/uncertainty fit, integration path and known failure modes.

## Routing sequence
1. Parse task into required capabilities and evidence class.
2. Apply hard gates: privacy, license, modality, reference/annotation, version, safety and IP restrictions.
3. Generate candidate capability records.
4. Score only the surviving candidates using transparent metadata.
5. Compose multi-capability routes when no single source satisfies the task.
6. Attach the required validation gate before any consequential claim.
7. Preserve route, versions, checksums/identifiers and evidence references in the execution record.

## Claim discipline
`prediction -> measurement -> biological/physical interpretation -> translational claim` are separate gates. A route may produce a prediction without authorizing a downstream claim.

## Failure handling
Missing provenance, stale version, unsupported applicability domain, unresolved licensing, privacy mismatch, benchmark leakage or contradictory evidence produces `inspect`, `blocked` or `hold`; it does not silently downgrade into an unsupported answer.

## Public/private boundary
Registry metadata is public-sanitized. Confidential formulations, unpublished data, proprietary field data, private genomic data, credentials and patent-sensitive strategy never enter this registry.
