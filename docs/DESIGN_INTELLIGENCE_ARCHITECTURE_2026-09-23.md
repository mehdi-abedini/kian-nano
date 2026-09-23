# Design Intelligence Architecture

**Status:** v0.1 baseline

## Purpose

Connect Research Agent, Design Agent, and Website Agent without allowing external design ecosystems to overwrite Kian Nano Karno identity.

## Pipeline

External Design Intelligence
→ Research Agent
→ Provenance Layer
→ KKN Design Intelligence
→ Design Agent
→ Figma / Code
→ Website Agent
→ Human Approval
→ Production
## Research Agent responsibilities

- Discover relevant design systems and agent workflows.
- Monitor changes on a defined cadence.
- Capture source, version, license, date, and provenance.
- Extract reusable principles rather than visual clones.
- Separate tokens from rationale.
- Identify accessibility, responsive, interaction, and performance practices.
- Flag contradictions and propose experiments.
- Never silently mutate KKN design files.

## Design Agent responsibilities

- Maintain the KKN Design Contract.
- Translate approved principles into tokens and components.
- Produce Figma-ready structures and implementation handoffs.
- Preserve RTL/LTR and scientific-content constraints.
- Maintain visual-regression criteria.
## Website Agent responsibilities

- Map approved components to WordPress/Elementor.
- Preserve content, SEO, accessibility, performance, and maintainability.
- Build draft/previews.
- Run audits.
- Never publish without human approval.

## Refresh model

Weekly: detect source changes and new relevant systems.

Monthly: re-evaluate the registry and selected references.

Quarterly: review the KKN fingerprint and remove stale or low-value influences.

On-demand: trigger when Figma, WordPress, design-agent, or DESIGN.md ecosystem changes materially affect implementation.
## Drift controls

A proposed design change requires:

source evidence + provenance + rationale + token/component diff + visual validation + accessibility/performance checks + approval state

The system compares principles, not pixel-level similarity. Similarity to an external brand is a review signal, never a design objective.

## Integration targets

- Kian Research Agent / Codex skill
- Figma MCP
- Figma design system/library
- WordPress/Elementor draft environment
- WPVibe audits
- GitHub registry and validation
- Canva for controlled visual assets when useful
