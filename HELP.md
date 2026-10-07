# Help

## Quick start

Install the package in a clean Python environment:

```bash
python -m pip install -e .
```

For development and regression testing:

```bash
python -m pip install -e ".[test]"
python -m pytest -q
```

## Deterministic public examples

Validate the public capability registry:

```bash
kian-nano validate-registries registry/cross_domain_capability_registry.json
```

Build a dependency-aware portfolio plan:

```bash
kian-nano plan-cycle --input examples/portfolio_cycle.json
```

Route a capability through the public registry:

```bash
kian-nano route --registry registry/cross_domain_capability_registry.json --capability variant_calling
```

These examples are intentionally bounded. They do not require company credentials or authorize consequential external actions.

## Research requests

A useful request should specify the question, scope, evidence standard, date boundary, and desired output.

Example:

> Investigate [question]. Search primary and authoritative sources, compare conflicting evidence, identify uncertainty and applicability limits, and produce a reproducible report with an evidence table.

## Industrial R&D

Example:

> Analyze [process]. Define the objective, KPIs, critical process parameters, instrumentation, scale-up risks, acceptance criteria, and validation experiments. Separate measured data from model-derived recommendations.

## Genomics / bioinformatics

Example:

> Analyze [dataset or workflow]. Pin the reference and workflow versions, define the benchmark, specify QC gates, preserve provenance, and report failure modes before interpreting biological results.

## IP / technology intelligence

Example:

> Map the prior art for [technology]. Separate factual patent evidence, claim interpretation, novelty analysis, and legal/FTO conclusions. Flag where specialist legal review is required.

## Finance / quantitative research

Example:

> Analyze [company/market]. Use dated primary financial and market data, preserve point-in-time assumptions, model costs and slippage, control survivorship and look-ahead bias, and separate observations from interpretation.

## Output controls

Ask for one or more of:

- executive summary;
- full technical report;
- evidence table;
- provenance ledger;
- uncertainty analysis;
- reproducibility package;
- experiment plan;
- patent/prior-art matrix;
- investment research memo;
- explicit list of unresolved evidence gaps.

## Evidence discipline

If evidence is missing, contradictory, stale, inaccessible, or outside the applicability domain, the correct behavior is to state the gap and reduce the claim scope rather than fill the gap with plausible assumptions.

## Further documentation

- [Reviewer Guide](docs/REVIEWER_GUIDE.md)
- [Architecture](docs/ARCHITECTURE.md)
- [FAQ](FAQ.md)
- [Security Policy](SECURITY.md)
- [Contributing](CONTRIBUTING.md)
