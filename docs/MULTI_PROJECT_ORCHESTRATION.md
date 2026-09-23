# Multi-Project Orchestration Architecture

Version: 0.4.0

## Objective
The platform supports multiple independent research, engineering, product, and infrastructure lanes under one portfolio-level orchestrator.

## Architecture
```text
Portfolio Orchestrator
  ├─ Scheduler / dependency manager
  ├─ Project State Registry
  ├─ Worker / specialist agents
  ├─ Evidence & provenance layer
  ├─ Validation / quality gates
  ├─ Human approval queue
  └─ Management reporting
        │
        ├─ Website / Digital Platform
        ├─ Biomedical / Drug Delivery
        ├─ Petroleum / Energy
        ├─ Chemical / Process Engineering
        ├─ Genomics / NGS
        └─ other registered project lanes
```

## Execution model
Projects are isolated by state and classification. Independent tasks may run concurrently when resources and dependencies permit. A blocked lane does not block unrelated lanes.

The first executable planning primitive is implemented in `portfolio_orchestrator.py`. It computes executable, blocked, failed, and dependency-waiting lanes without executing side effects.

Each material stage ends with a persisted checkpoint and management report.
Questions that genuinely block multiple lanes are consolidated into a single human decision batch where practical.

## Evidence discipline
Research outputs retain provenance, dates, assumptions, uncertainty, limitations, and validation status. Generated analysis is not treated as experimental evidence.

## Security boundary
Public repository content is sanitized and reusable. Confidential company knowledge, unpublished IP, proprietary formulations, private datasets, credentials, and experimental records remain in the private runtime.

Private-to-public synchronization is never implicit. Export requires classification, sanitization, and human approval.

## [redacted-project] boundary
Sensitive [redacted-project] research is outside the public repository and public agent package. Only non-sensitive orchestration concepts may be documented publicly.

## Stage completion
A stage is complete only when acceptance criteria are satisfied, state is persisted, the management report is written, and required approval gates are recorded.

## Current implementation status
- Portfolio cycle planning: implemented and unit-tested.
- Design repository intake/ranking: implemented and unit-tested.
- Evidence ledger, validation contracts, and domain modules: existing and tested.
- Persistent state store, worker pool, full dependency engine, gate engine, and automated management-report writer: not yet claimed as fully operational.

## Next implementation layer
Connect the pure planning primitives to the project registry/state store, then add checkpoint persistence, dependency transitions, approval queues, and report generation. Keep execution adapters separate from planning logic so the same plan can be replayed and audited.
