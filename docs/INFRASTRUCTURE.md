# Infrastructure assessment

## Current state — 2026-09-21

The public agent package is deployable as a skill, but it is not yet a complete autonomous research platform.

### Verified components

- Git repository: clean main branch, public tag `v0.1.0`.
- Local skill installation: present and SHA-256 synchronized with the repository.
- Static validation: SKILL frontmatter, whitespace, and public secret-pattern scan pass.
- OmniRoute: installed and running locally on port 20128.
- OmniRoute health: reports healthy; version 3.8.50; two configured and healthy provider connections.
- OmniRoute model catalog: exposes GPT-5.6 family models.
- Conduit: API endpoint is reachable and the configured key authenticates successfully for `/v1/models`.
- Codex: can start against Conduit and receive model output with `gpt-5.6`.
- WordPress: public research-agent page renders and its CTA links were verified.

## Critical gaps

### 1. Stable model-gateway contract

The local OmniRoute OpenAI-compatible API currently returns HTTP 401 to unauthenticated `/v1/models` requests. A dedicated scoped OmniRoute API credential for Codex has not been provisioned into the Codex runtime.

Conduit connectivity is working, but Codex requests are currently intermittent: `gpt-5.6-codex` hit reconnect failures and a later `gpt-5.6` run hit HTTP 429. Therefore the gateway is not yet a deterministic production dependency.

### 2. Orchestrator

The repository defines an orchestration architecture but does not yet contain a production orchestrator that decomposes a task, runs specialists, reconciles evidence, and emits one governed report.

### 3. Evidence/retrieval layer

There is no implemented evidence service with source acquisition, DOI/PubMed/patent retrieval, date snapshots, deduplication, provenance, citation validation, and evidence grading.

### 4. Persistent knowledge boundary

Public workflow logic is separated from private knowledge, but there is not yet a dedicated private knowledge store with access control, encryption, auditability, and project-level isolation.

### 5. Evaluation harness

The repository has evaluation prompts and acceptance criteria, but no automated runtime evaluation suite that scores real model runs for citation fidelity, uncertainty handling, hallucination resistance, and reproducibility.

### 6. Governance and approval service

The skill documents approval gates, but there is no persistent approval queue for publication, external communication, financial actions, purchases, or irreversible system changes.

### 7. Observability and recovery

OmniRoute has local logs and health reporting, but the Kian agent lacks unified request IDs, agent-level metrics, failure classification, alerting, and a tested restore procedure spanning agent state and knowledge stores.

### 8. Website/API integration

The WordPress page is a public presentation layer only. There is no authenticated research-request endpoint, job queue, result store, or approval workflow connecting the website to the agent runtime.

### 9. CI/CD and supply-chain controls

A basic public-package validation workflow has now been added. Dependency review, action pinning, automated release gates, and signed release provenance remain to be added as the implementation grows.

### 10. Scheduling and automation

There is no production scheduler for recurring literature surveillance, patent monitoring, market intelligence, report generation, or human approval notifications.

## Priority order

1. Establish a stable, scoped model-gateway credential and deterministic runtime test.
2. Implement the orchestrator and specialist execution contract.
3. Implement evidence retrieval/provenance and automated evaluation.
4. Add private knowledge storage with strict public/private isolation.
5. Add approval queue, audit trail, scheduling, and observability.
6. Connect the WordPress request surface only after the runtime passes the evaluation gate.

## Security baseline

Never commit provider keys, OmniRoute credentials, private research data, unpublished formulations, contracts, or personal access tokens. GitHub recommends least-privilege workflow tokens, secret storage, dependency review, and secret scanning; WordPress recommends scoped Application Passwords for programmatic integrations over HTTPS.

## Exit criterion for production readiness

A production candidate should pass: gateway health; authenticated model call; three representative research tasks; citation/provenance checks; uncertainty and hallucination checks; failure/retry tests; private-data isolation tests; approval-gate tests; backup/restore test; and a reproducible release from a clean checkout.

## Runtime findings added during the 2026-09-21 audit

- OmniRoute was found with duplicate server/supervisor processes after repeated restart attempts. The duplicate processes caused port collisions on 20131/20132 and were cleaned up.
- A clean server instance was restored on `127.0.0.1:20128`; the dashboard root returns HTTP 307 and `/v1/models` returns HTTP 401, confirming that the HTTP gateway is alive but authenticated API access is still required.
- OmniRoute logs show a recurring cleanup error for a missing `compression_run_telemetry` table. This is a product/database migration issue and should be fixed or suppressed by the gateway vendor before production use.
- Redis is not configured; OmniRoute falls back to in-memory rate limiting. This is acceptable for a single-machine test but not sufficient for durable multi-process admission/rate-limit state.
- The current direct server recovery is not yet a durable Windows service/autostart deployment. Process supervision and reboot recovery remain open.

These findings are intentionally separated from the Kian agent package: they are gateway/runtime infrastructure issues, not research-skill logic defects.
