# KNN n8n Automation Plane

This directory contains the automation layer for the Kian agent platform.

n8n is deliberately outside the agent reasoning core. It triggers and coordinates bounded jobs through HTTP/MCP/API interfaces.

## Planned workflows
1. provider_health_and_catalog_sync
2. github_agent_ecosystem_discovery
3. weekly_regression_and_benchmark
4. update_proposal_and_approval
5. faq_candidate_generation
6. support_message_triage
7. daily_company_digest
8. monthly_agent_architecture_review

## Deployment
The intended deployment is self-hosted n8n with PostgreSQL persistence. Docker is the preferred production runtime. The current Windows workstation does not yet expose Docker on PATH, so only the workflow/configuration scaffold is installed here.

## Secrets
Never commit provider keys, messaging tokens, cookies or private webhook secrets. Configure credentials in n8n's credential store or an external secret manager.
