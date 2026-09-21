# Evaluation Prompts

## Should trigger
1. Review the literature on nanoparticle drug delivery for a specified target.
2. Compare reactor designs for [redacted-process] production.
3. Build a prior-art landscape for a new [redacted-project] process.
4. Analyze a historical equity strategy with point-in-time controls.
5. Design an experimental plan for scale-up.
6. Assess the evidence behind a biomedical mechanism.
7. Compare commercialization pathways for a patented technology.
8. Produce a research report with uncertainty and reproducibility.
9. Design a WGS/WES or long-read variant-analysis workflow with benchmark validation.
10. Analyze single-cell or spatial omics data with an executable, reproducible workflow.
11. Compare genomic foundation models for a specified downstream task.
12. Audit an AI agent for genomics research, including provenance, tool permissions, leakage controls, and benchmark performance.
13. Build a genomics reference/database registry with versions, dates, access constraints, and provenance.

## Should not trigger as the primary workflow
1. Rewrite a casual email.
2. Translate one sentence.
3. Create a simple arithmetic calculation.
4. Change a WordPress button color without research requirements.
5. Write generic prose with no research task.

## Acceptance criteria
A valid run should:
- identify the research objective;
- identify evidence and distinguish evidence from interpretation;
- cite dated sources;
- expose missing evidence;
- avoid fabricated results;
- preserve point-in-time constraints for historical finance;
- for genomics, lock reference/annotation versions and preserve sample/data provenance;
- for agentic genomics, require executable analysis for data-derived conclusions and report benchmark/grader evidence when available;
- separate model predictions from experimental evidence;
- end with reproducible next steps.
