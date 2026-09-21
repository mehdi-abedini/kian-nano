# Architecture

## Layers

### 1. Model gateway
OmniRoute provides model routing and abstraction. It is not the agent registry.

### 2. Agent skill layer
This repository provides the Kian research skill and domain references.

### 3. Specialist layer
Specialists can be added for science, bioinformatics, drug discovery, petroleum, IP, finance, quant research, and business.

### 4. Evidence layer
Each workstream returns dated sources, methods, assumptions, calculations, and uncertainty.

### 5. Orchestration layer
The orchestrator decomposes tasks, runs independent workstreams, reconciles findings, and produces one final report.

### 6. Knowledge layer
Public workflow logic is separate from confidential Kian knowledge.

## Design principle
Prefer a modular skill chain and specialist agents over one monolithic prompt. Use progressive disclosure and deterministic scripts where exact validation matters.
