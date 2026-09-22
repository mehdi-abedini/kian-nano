# Kian Nano Karno - Platform Infrastructure Integration Baseline
Date: 2026-09-23
Status: INTERNAL DRAFT

Target topology:
WordPress public CMS/presentation
    |
Laravel Application Layer
    |-- Academy
    |-- Identity/RBAC
    |-- Dashboard
    |-- Commercial/Usage
    |-- Agent Gateway client
    |
Authenticated Agent Gateway
    |
Research Agent Platform
    |-- Research agents
    |-- Genomics workflows
    |-- Evidence Ledger
    |-- Evaluation/Benchmarking

Required controls:
- authenticated service-to-service calls
- RBAC and tenant/data boundaries
- usage and cost metering
- audit/event trail
- rate limits and budget limits
- evidence/provenance linkage
- explicit public/private/confidential data classes
- human approval for irreversible/public actions
