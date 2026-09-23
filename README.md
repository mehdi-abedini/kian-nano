# Kian Nano Karno Research Agent

An evidence-grounded scientific research agent and orchestration framework for reproducible literature review, patent research, technology intelligence, biomedical research, industrial R&D, process engineering, and quantitative research.

**Core keywords:** scientific AI, research agent, AI agent, agent skills, evidence-based research, literature review, systematic review, patent research, prior-art analysis, technology intelligence, reproducible research, scientific workflow orchestration.

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

`User task -> portfolio orchestrator -> capability router -> specialist workstreams -> evidence ledger -> validation gates -> synthesis -> report`

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

The framework emphasizes:

- source and version tracking
- dated evidence
- benchmark and test gates
- uncertainty and failure-mode recording
- deterministic validation where possible
- explicit applicability domains
- point-in-time controls for historical quantitative research
- human review for high-impact or irreversible decisions

## Public / private boundary

This repository is the **public capability and architecture layer**. Company-confidential project records, unpublished formulations, experimental parameters, private datasets, customer information, patent-sensitive strategy, and internal research documents are maintained outside this public repository.

Do not commit secrets, credentials, unpublished experimental data, private contracts, or confidential technical parameters.

## Installation

Copy the skill directory into a compatible Agent-Skills directory, for example:

- Codex user scope: `~/.agents/skills/`
- Codex repository scope: `.agents/skills/`

Then start a new Codex session if the skill list does not refresh automatically.

## Example research tasks

- Review evidence for a drug-delivery mechanism and identify validation gaps.
- Build a systematic literature and patent landscape for a technology.
- Compare process-simulation approaches and define scale-up acceptance tests.
- Design a formulation optimization workflow using DoE and Bayesian optimization.
- Build a reproducible genomics workflow with benchmark and leakage controls.
- Analyze a historical quantitative strategy without look-ahead or survivorship bias.
- Produce a technical report with citations, uncertainty, reproducibility notes, and explicit validation gates.

## Academic and technical scope

The framework is intended for research support across peer-reviewed literature, authoritative databases, patent offices, open scientific software, benchmark datasets, university research, industrial process knowledge, and validated computational tools.

Source quality is assessed before adoption. Third-party agents, MCP servers, repositories, datasets, and executable tools are treated as untrusted until provenance, license, security, versioning, reproducibility, and applicability have been reviewed.

## Project status

**Public architecture:** v0.1.x research-agent foundation.

The project is a research workflow and orchestration framework. It does not guarantee scientific correctness, clinical efficacy, manufacturing performance, financial returns, or autonomous decision quality.

## Citation and contribution

Please use the repository documentation and citation metadata when referencing this software. Contributions should preserve evidence provenance, validation contracts, security boundaries, and reproducibility requirements.
