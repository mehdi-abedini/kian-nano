# Architecture

## System boundary

The public Research Agent is a capability and research-infrastructure layer within the broader Kian Nano Karno ecosystem. It is deliberately not presented as the complete KHWARIZMI AI OS.

## Execution flow

Research question
-> problem decomposition
-> capability routing
-> specialist workstreams
-> evidence collection
-> validation
-> reconciliation
-> synthesis
-> reproducible report

The architecture separates discovery, evidence, computation, validation, and synthesis so that model output is not silently treated as evidence.

## Layers

### 1. Model gateway

OmniRoute provides model routing and abstraction. It is not the agent registry and does not define scientific authority.

### 2. Capability / skill layer

This repository provides public research capabilities, domain references, contracts, and deterministic utilities.

### 3. Specialist layer

Specialists can be added for science, bioinformatics, drug discovery, petroleum, IP, finance, quantitative research, and business.

### 4. Evidence layer

Each workstream is expected to return dated sources, methods, assumptions, calculations, applicability, uncertainty, and provenance.

### 5. Validation layer

Validation checks the structural and behavioral claims that can be tested locally. Scientific or empirical claims remain subject to domain-appropriate external evidence.

### 6. Orchestration layer

The orchestrator decomposes tasks, runs independent workstreams where dependencies permit, reconciles findings, and produces one final report.

### 7. Knowledge layer

Public workflow logic is separated from confidential Kian knowledge, unpublished experimental data, customer information, credentials, and patent-sensitive implementation.

## Evidence model

Research outputs distinguish:

- observed evidence;
- derived analysis;
- model output;
- hypothesis;
- human-reviewed decision.

This distinction is a core architectural boundary rather than a documentation convention.

## Reviewability

The public repository is designed so a reviewer can move from:

README -> architecture -> executable examples -> tests -> CI -> change history

without requiring access to confidential infrastructure.

See [REVIEWER_GUIDE.md](REVIEWER_GUIDE.md) for the verification path and [KHWARIZMI_PUBLIC_EVIDENCE.md](KHWARIZMI_PUBLIC_EVIDENCE.md) for the public/private AI OS boundary.

## Design principles

Prefer a modular skill chain and specialist capabilities over one monolithic prompt. Use progressive disclosure and deterministic scripts where exact validation matters. Capability claims should remain bounded by executable evidence and explicit uncertainty.
