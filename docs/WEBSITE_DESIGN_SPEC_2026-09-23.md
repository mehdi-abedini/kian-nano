# Kian Nano Karno Website Design Specification

**Scope:** Landing page + Academy
**Status:** Design architecture baseline

## Design thesis

Present Kian Nano Karno as a scientific technology engine, not a generic consulting site and not a SaaS clone.

The central visual idea is:
Evidence → Mechanism → Engineering → Validation → Deployment

The interface uses scientific structure as a visual grammar: measured hierarchy, modular grids, evidence metadata, controlled information density, restrained motion, technical notation where useful, human authorship, and bilingual RTL/LTR correctness.
## Landing page

### 01 — Hero
Narrative: "From Scientific Insight to Deployed Technology".

Use an original scientific visual system, not a copied brand motif. Communicate nanotechnology, biomedical engineering, industrial R&D, and technology deployment within seconds.

Primary CTA: Explore Technologies.
Secondary CTA: Enter Academy.

### 02 — Research-to-Technology Engine
Show:
Question → Evidence → Mechanism → Engineering → Validation → Deployment

### 03 — Technology Domains
Use high-information modules for:
- Nanotechnology & Advanced Materials
- Drug Delivery & Molecular Design
- Biomedical Engineering & Instrumentation
- Energy, Petroleum & Water Technologies
- AI-Assisted Scientific Research
### 04 — Selected Technologies

Each item exposes technology/product, application, verified evidence status, public maturity information when available, and a CTA.

### 05 — Evidence Layer

Use publications, patents, standards, pilots, and benchmarks as structured evidence. Avoid vanity counters.

### 06 — Research Agent

Present the Research Intelligence Platform as infrastructure:
evidence retrieval, specialist agents, provenance, reproducibility, validation, and controlled automation.

### 07 — Academy

Feature curated technical content with domain and evidence metadata.

### 08 — Collaboration / Company

Research collaboration, industrial deployment, technology licensing, and contact.
## Academy

Academy is a technical knowledge platform rather than a chronological blog archive.

Primary taxonomy:
Research Notes | Scientific Explainers | Methods | Technology Intelligence | Drug Delivery | Nanotechnology | Genomics/NGS | Biomedical Engineering | Energy/Petroleum/Water | Instrumentation | IP | AI for Science

Article page:
title, abstract, author/review status, date, domain, evidence level, reading time, body, figures, references, related technologies, related articles, and material update history.

Content states:
Draft → Evidence Checked → Human Reviewed → Published → Superseded
## Responsive and bilingual requirements

- Persian is RTL; English is LTR.
- Technical identifiers, citations, code, units, gene symbols, chemical formulas, URLs, and Latin names require controlled bidi handling.
- Mobile preserves evidence hierarchy.
- Touch targets and keyboard navigation are required.
- Reduced-motion mode is respected.

## SEO and performance

Use semantic HTML, stable metadata, canonical URLs, structured data where applicable, optimized image delivery, and measured LCP/INP/CLS/accessibility/SEO before publication.

## Production boundary

This is a design proposal. No production website mutation is authorized by this document alone.

## Language and direction — mandatory

The primary website experience is Persian (fa-IR) and RTL. English is the secondary language (en) and LTR.

Design and implementation must therefore be authored RTL-first rather than translating an LTR layout after the fact.

Requirements:
- Persian/Vazir is the primary UI typography.
- English typography is a separate token set and must not alter Persian metrics.
- Navigation, grids, cards, CTA hierarchy, breadcrumbs, article metadata, and Academy taxonomy are RTL in Persian.
- Technical strings such as DOI, URLs, code, gene symbols, chemical formulas, units, Latin species names, and identifiers use controlled bidi isolation where necessary.
- Language switching changes document language/direction and preserves semantic page relationships.
- The English version uses the same KKN design system but is independently laid out LTR.
- Figma validation must include Persian RTL frames before implementation handoff.

## Motion system

Motion is part of KKN's scientific storytelling, but it is not decoration without a narrative purpose.

Allowed hero concept families:
1. A restrained rotating DNA double helix.
2. A molecular/atomic network responding subtly to pointer proximity.
3. A scientific field/grid whose particles reorganize as the pointer moves.
4. A mechanism-to-deployment path where nodes activate sequentially.
5. A slow orbital system suggesting molecular/engineering relationships.

Motion rules:
- Hero motion must remain secondary to headline, CTA, and evidence.
- Pointer interaction is progressive enhancement; content and navigation must work without a pointer.
- No motion should cause layout shift.
- Prefer transform/opacity/compositor-friendly animation.
- Use prefers-reduced-motion to provide a reduced/static mode; an explicit site-level Motion toggle may also be provided.
- Avoid continuous high-frequency particle movement.
- Avoid excessive parallax, flashing, rapid zoom, or competing motion fields.
- Motion should serve orientation, feedback, transition, or narrative.
- Mobile receives a lower-complexity motion profile.

Performance gate:
- Target LCP < 2.5 s, INP < 200 ms, CLS < 0.1 at the 75th percentile.
- Heavy WebGL/canvas is not allowed in the critical rendering path without a measured performance justification.
- Static poster/fallback imagery must exist for reduced-motion, low-power, or unsupported contexts.

## Accessibility and SEO

Use semantic HTML landmarks, logical heading hierarchy, keyboard-visible focus, sufficient contrast, functional alt text, accessible labels, and a coherent tab order.

SEO architecture must include:
- unique title/meta description strategy
- canonical URLs
- XML sitemap
- robots directives
- Open Graph/social metadata
- JSON-LD where applicable
- semantic HTML
- internal linking
- multilingual hreflang relationships
- Persian and English page-specific metadata
- stable, crawlable URLs

Core Web Vitals are release gates rather than post-launch diagnostics.
