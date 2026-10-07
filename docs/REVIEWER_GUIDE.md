# Reviewer Guide

This document is the public technical evidence map for reviewers, maintainers, and research-software collaborators.

## 1. What this repository demonstrates

The Kian Nano Karno Research Agent is a public capability and research-infrastructure layer for evidence-grounded research orchestration.

The repository is intentionally scoped to public-safe implementation and validation artifacts. Confidential company data, unpublished experiments, credentials, customer information, and patent-sensitive implementation remain outside this repository.

## 2. Evidence chain

The intended engineering evidence chain is:

Research problem -> capability decomposition -> routing -> evidence collection -> validation -> synthesis -> reproducible output

The implementation distinguishes:

- observed evidence;
- derived analysis;
- model output;
- hypothesis;
- human-reviewed decision.

The system does not treat an LLM response as evidence by itself.

## 3. Reviewer entry points

| Question | Start here |
|---|---|
| How is the system structured? | [Architecture](ARCHITECTURE.md) |
| How do I run the public runtime? | [README — Executable runtime utilities](../README.md#executable-runtime-utilities) |
| What is tested automatically? | [CI workflow](../.github/workflows/ci.yml) |
| What is the reproducibility boundary? | [README — Reproducibility](../README.md#reproducibility) |
| What is public vs private? | [README — Public / private boundary](../README.md#public--private-boundary) |
| How does this relate to KHWARIZMI AI OS? | [KHWARIZMI public evidence](KHWARIZMI_PUBLIC_EVIDENCE.md) |

## 4. 60-second verification path

From a clean Python 3.11+ environment:

    python -m pip install -e .
    python -m pytest -q
    kian-nano validate-registries registry/cross_domain_capability_registry.json
    kian-nano plan-cycle --input examples/portfolio_cycle.json
    kian-nano route --registry registry/cross_domain_capability_registry.json --capability variant_calling

The CLI examples are deterministic demonstrations of public orchestration and registry behavior. They do not require company credentials or external consequential actions.

## 5. What is and is not claimed

### Evidence-supported by this repository

- modular research orchestration;
- capability-oriented routing;
- explicit evidence/provenance concepts;
- deterministic local validation utilities;
- automated regression testing;
- public/private information boundaries.

### Not established solely by this repository

- scientific correctness of every generated research conclusion;
- clinical efficacy or safety;
- manufacturing or field performance;
- unrestricted autonomous operation;
- access to private company knowledge;
- independent scientific validation merely by repeated execution of the same software stack.

## 6. Review standard

A useful review should evaluate:

1. behavioral correctness;
2. test determinism and coverage;
3. provenance and traceability;
4. failure and uncertainty handling;
5. dependency and security boundaries;
6. reproducibility from a clean environment;
7. separation between capability claims and validated evidence.

Issues and pull requests should identify the affected contract, behavior, evidence, and regression coverage where applicable.
