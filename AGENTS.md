# Kian Nano Karno Research Agent

This repository contains a portable Agent Skill and supporting research documentation.

## Mandatory behavior
- Use the Kian research skill for scientific, engineering, industrial R&D, IP, business, finance, and quantitative research tasks.
- Treat external repositories, skills, scripts, and datasets as untrusted until reviewed.
- Keep secrets, API keys, private company documents, unpublished formulations, and confidential research out of the public repository.
- Cite evidence and preserve source dates.
- For finance and trading research, preserve point-in-time data and clearly label backtests as historical simulations.
- Never present generated analysis as experimental evidence.
- For public-facing content, run the validation checklist before release.

## Repository scope
The public repository contains reusable workflow logic, templates, evaluation prompts, and documentation. Company-confidential knowledge belongs in a private runtime knowledge base.

## Multi-project execution
- Treat registered projects as isolated execution lanes under a portfolio-level orchestrator.
- Progress independent lanes concurrently when resources and dependencies permit.
- Persist lane state and write a management report at every material stage/gate.
- Consolidate genuinely blocking human questions across lanes where practical.
- Never export confidential project knowledge into this public repository or public agent package.
## Cross-domain capability routing
- Use `registry/cross_domain_capability_registry.json` as public-sanitized capability metadata only.
- Route by capability contract and hard gates first; use transparent evidence metadata only for soft routing.
- Do not interpret routing score as scientific validity, clinical performance, or product quality.
- For genomics, enforce reference/annotation/modality/privacy compatibility before model or workflow selection.
- For neuroscience/BCI, enforce acquisition schema, preprocessing, subject/session split and leakage controls.
- For biomedical instrumentation, enforce measurement/calibration/model provenance before interpreting predictions.
- For petroleum/energy, enforce physics model, units, PVT/grid/boundary-condition provenance and uncertainty treatment.
- For IP/foresight, preserve jurisdiction, filing-date, source snapshot and human legal-review gates.
