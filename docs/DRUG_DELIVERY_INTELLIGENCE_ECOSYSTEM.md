# Drug Delivery Intelligence Ecosystem — Sanitized Source Map

Version: 0.1 — 2026-09-23

This document contains public-source architecture only. It contains no Kian Nano Karno formulation, candidate, experimental, IP, or private dataset.

## Core source classes

1. Therapeutics datasets and benchmarks
2. Nanoparticle/LNP databases
3. Molecular property and ADME tools
4. Molecular simulation
5. Formulation/QbD/optimization
6. AI/LLM scientific agents
7. High-throughput and autonomous laboratories
8. Nanotoxicology/nanoinformatics
9. Regulatory/CMC evidence
10. Primary literature and systematic reviews

## High-priority public assets

- TDC — therapeutic datasets, tasks, evaluators, splits, benchmarks and oracles.
- LNPDB — lipid nanoparticle database.
- LNPBO — Bayesian optimization for LNP formulation.
- LANTERN — LNP computational resource.
- M3_Ionizable_Lipids — ionizable-lipid simulation resources.
- CLADD — RAG-enhanced collaborative agents for drug discovery.
- ChemCrow — chemistry tool-using agent.
- CoScientist — multi-agent scientific discovery architecture.
- Robochem_Flex — modular self-driving chemistry laboratory.
- eNanoMapper — nanomaterial characterization and biological/toxicological data.
- NanoCommons — integrated nanoinformatics knowledge/data infrastructure.

## Agent architecture implication

The Drug Delivery Agent should be a routed system, not one monolithic model:

Evidence/RAG
→ TPP
→ molecular intelligence
→ ADME/PK
→ nanocarrier/formulation
→ CQA/release
→ nano-bio interaction
→ simulation
→ optimization/active learning
→ experiment design
→ automation
→ validation
→ CMC/regulatory
→ IP/translation

Every stage must preserve provenance and uncertainty.

## Safety and governance

External code is untrusted until license, provenance, security, maintenance and reproducibility review.

External scientific claims require source-level verification.

Computational predictions never become experimental evidence automatically.

Private KKN project data must never enter this public layer.
