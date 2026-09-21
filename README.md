# Kian Nano Karno Research Agent

A portable Agent Skill for evidence-grounded scientific research, industrial R&D, technology intelligence, IP research, business analysis, finance, quantitative research, and trading research.

## What it does
The agent acts as an orchestration layer. It decomposes complex questions, assigns research workstreams, gathers dated evidence, checks conflicts, and produces reproducible reports.

It is designed for Codex and other Agent-Skills-compatible runtimes. The portable skill format uses a SKILL.md entry point and progressive disclosure through reference files.

## Domains
- Nanotechnology and materials
- Drug discovery and drug delivery
- Protein engineering and bioinformatics
- Genomics and biomedical research
- Petroleum, energy, process engineering, and wastewater
- Instrumentation, scale-up, manufacturing, and QC
- Patents, prior art, and technology intelligence
- Market intelligence and commercialization
- Finance, quantitative research, risk, and trading research

## Architecture
User task -> orchestrator -> specialist research workstreams -> evidence ledger -> validation -> synthesis -> report.

Company-confidential knowledge is intentionally separated from this public repository.

## Installation
Copy the skill directory into a compatible user or repository skills directory, for example:
- Codex user scope: ~/.agents/skills/
- Codex repository scope: .agents/skills/

Then start a new Codex session if the skill list does not refresh automatically.

## Example requests
- "Review the evidence for a new drug-delivery mechanism."
- "Compare pilot-scale reactor options and define acceptance tests."
- "Build a prior-art landscape for this invention."
- "Analyze a historical trading strategy without look-ahead bias."
- "Produce a research report with sources, uncertainty, and reproducibility notes."

## Safety
Third-party skills and repositories are executable capability bundles and must be reviewed before installation. Do not place secrets, private company files, unpublished formulations, or confidential contracts in this repository. citeturn0search0

## Status
Initial public architecture: v0.1.0. The skill is a workflow foundation, not a guarantee of research correctness or financial performance.
