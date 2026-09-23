# Design Repository Collection Protocol

**Status:** v0.2 operational baseline
**Date:** 2026-09-23
**Classification:** PUBLIC-SANITIZED

## Objective
Collect public design-system, DESIGN.md, website-extraction, and design-agent repositories as research evidence without allowing an external repository to overwrite Kian Nano Karno identity.

## Collection pipeline

1. Discover candidates from GitHub repository search and approved registries.
2. Normalize repository identity and collapse duplicates.
3. Capture description, topics, source class, license state, archive state, default branch, update date, and URL.
4. Assign provenance class before any content extraction.
5. Score intake priority using relevance, provenance, license clarity, and recency.
6. Apply risk penalties for clone/copy language, archived repositories, and unresolved licensing.
7. Keep every candidate in inspect_only until repository contents and license are independently reviewed.
8. Extract principles, not brand signatures or pixel-level clones.
9. Store evidence and rationale with retrieval date and version/commit where available.
10. Generate a proposal/diff for any KKN token or component change; require human approval before adoption.

## Intake score

0.40 relevance + 0.25 provenance + 0.15 license clarity + 0.20 recency

Risk penalties are applied after the base score:
- clone/similarity signal: -0.20
- brand-signature signal: -0.15
- archived repository: -0.20

The score is an inspection priority, not a quality ranking or adoption decision.

## Separation of concerns

- Discovery: GitHub search / curated registries.
- Intake: design_repository_collector.py.
- Evidence: provenance-tagged candidate manifest.
- Synthesis: KKN Design Contract + DESIGN.md.
- Implementation: Design Agent / Figma / Website Agent.
- Production: human approval only.

## Current evidence cycle

Search themes used on 2026-09-23:
- design.md web design system agent
- DESIGN.md frontend design system
- web design intelligence agent workflow
- design system extraction website

Initial candidates include official-design-md, iFurySt/DESIGN.md, website/design-system extraction projects, and design-system skill projects. They remain inspect_only; no external repository was cloned into the KKN project and no KKN design token was overwritten.

## Synchronization rule

The design lane publishes only sanitized evidence objects to the portfolio layer:
candidate_id → provenance → inspection status → extracted principles → proposed changes → validation → approval state

Confidential scientific/IP information from KNN R&D lanes must never be used as public design-repository evidence.
