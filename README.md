# Kian Nano Karno Research Agent

An evidence-grounded scientific research agent and orchestration framework for reproducible literature review, patent research, technology intelligence, biomedical research, industrial R&D, process engineering, and quantitative research.

## Reviewer / technical evidence map

A reviewer can evaluate the public implementation without access to confidential company infrastructure:

1. **Architecture:** [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
2. **Verification path:** [docs/REVIEWER_GUIDE.md](docs/REVIEWER_GUIDE.md)
3. **Executable runtime:** [Executable runtime utilities](#executable-runtime-utilities)
4. **Automated regression:** [.github/workflows/ci.yml](.github/workflows/ci.yml)
5. **Change history:** [CHANGELOG.md](CHANGELOG.md)
6. **KHWARIZMI boundary:** [docs/KHWARIZMI_PUBLIC_EVIDENCE.md](docs/KHWARIZMI_PUBLIC_EVIDENCE.md)

The evidence path is intentionally ordered from system design to executable behavior, automated checks, and historical traceability.

## Position within KHWARIZMI AI OS

The Research Agent is a **public capability and research-infrastructure layer** within the broader Kian Nano Karno ecosystem. It is not the entire AI OS and does not replace the governed Executive Orchestrator.

The broader platform identity is **KHWARIZMI AI OS**. Its scientific heritage vocabulary maps six documented scientific traditions to methodological capability domains:

| Identity | Methodological role |
|---|---|
| **Khwarizmi** | Formal problem solving, computation, orchestration |
| **Biruni** | Observation, measurement, evidence |
| **Avicenna** | Knowledge structure, synthesis, reasoning |
| **Razi** | Experimentation, validation, falsification |
| **Khayyam** | Mathematical modeling, time, uncertainty |
| **Tusi** | Systems integration, coordination, scientific infrastructure |

The names are not automatically implemented as agents. Capability, evidence, interface, trust, validation, and governance determine implementation.

## What it does

The agent decomposes complex research questions into specialist workstreams, routes tasks by capability, collects dated and traceable evidence, validates claims, records uncertainty and failure modes, and synthesizes reproducible technical reports.

The design separates **discovery, evidence, computation, validation, and synthesis** rather than treating an LLM response as evidence.

## Research domains

- **Drug discovery and drug delivery:** molecular intelligence, ADME, formulation, nanocarriers, lipid nanoparticles, release, PK/PD, CMC, and translational research.
- **Genomics and bioinformatics:** NGS, variant analysis, workflow validation, reference builds, benchmark datasets, and reproducible pipelines.
- **Protein engineering and computational biology:** sequence analysis, structure prediction, mutation analysis, protein design, and biomolecular evidence synthesis.
- **Nanotechnology and materials science:** nanomaterials, characterization, formulation, mechanism, scale-up, and technology translation.
- **Biomedical engineering and instrumentation:** measurement models, calibration, sensors, experimental design, validation, and device-oriented research.
- **Neuroscience and brain-computer interfaces:** neural data, preprocessing, leakage controls, signal analysis, and external validation.
- **Petroleum, energy, and process engineering:** process modeling, transport, flow assurance, wastewater treatment, simulation, optimization, and scale-up.
- **Formulation and process development:** design of experiments, response-surface methods, Bayesian optimization, active learning, process analytical technology, and CQA/CPP mapping.
- **Patents and technology intelligence:** patent landscape, prior art, family analysis, claim-aware review, technology scouting, and IP evidence.
- **Finance and quantitative research:** market data provenance, point-in-time datasets, backtesting controls, risk, transaction costs, and quantitative research.

## Architecture

`User task → portfolio orchestrator → capability router → specialist workstreams → evidence ledger → validation gates → synthesis → report`

The framework supports parallel project lanes, persistent state, dependency-aware execution, consolidated clarification rounds, non-blocking workstreams, and human approval gates for consequential actions.

## Evidence and validation model

Every substantive claim should be traceable to an evidence record with source identity, date/version, applicability, uncertainty, and provenance.

Research outputs distinguish:

1. **Observed evidence** — directly supported by a primary or authoritative source.
2. **Derived analysis** — a reproducible computation or synthesis from identified inputs.
3. **Model output** — a prediction, simulation, surrogate, or optimization result.
4. **Hypothesis** — a proposed explanation or design target requiring validation.
5. **Decision** — a human-reviewed conclusion or next experimental step.

Computational prediction is not treated as proof of formulation performance, biological efficacy, safety, manufacturability, or field performance.

## Reproducibility

The framework emphasizes source and version tracking, dated evidence, benchmark and test gates, uncertainty and failure-mode recording, deterministic validation where possible, explicit applicability domains, point-in-time controls for historical quantitative research, and human review for high-impact or irreversible decisions.

## Public / private boundary

This repository is the **public capability and architecture layer**. Company-confidential project records, unpublished formulations, experimental parameters, private datasets, customer information, patent-sensitive strategy, and internal research documents are maintained outside this public repository.

Do not commit secrets, credentials, unpublished experimental data, private contracts, or confidential technical parameters.

## Academic and technical scope

The framework is intended for research support across peer-reviewed literature, authoritative databases, patent offices, open scientific software, benchmark datasets, university research, industrial process knowledge, and validated computational tools.

Source quality is assessed before adoption. Third-party agents, MCP servers, repositories, datasets, and executable tools are treated as untrusted until provenance, license, security, versioning, reproducibility, and applicability have been reviewed.

## Project status

**Public architecture:** v0.4.0 research-agent foundation.

The project is a research workflow and orchestration framework. It does not guarantee scientific correctness, clinical efficacy, manufacturing performance, financial returns, or autonomous decision quality.

## Citation and contribution

Please use the repository documentation and citation metadata when referencing this software. Contributions should preserve evidence provenance, validation contracts, security boundaries, and reproducibility requirements.

## Executable runtime utilities

The public repository includes a minimal deterministic CLI for local validation and orchestration demonstrations:

- `pip install -e .`
- `kian-nano validate-registries registry/cross_domain_capability_registry.json`
- `kian-nano plan-cycle --input examples/portfolio_cycle.json`
- `kian-nano route --registry registry/cross_domain_capability_registry.json --capability variant_calling`

The CLI is deliberately narrow: it does not grant external credentials, perform autonomous consequential actions, or bypass project privacy/approval boundaries.

## Executable examples

The examples/ directory contains public-safe examples for dependency-aware portfolio planning, capability routing, and evidence-output structure. They contain no private company research data.
