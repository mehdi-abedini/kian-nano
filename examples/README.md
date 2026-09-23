# Executable examples

These examples are intentionally public-safe. They demonstrate the orchestration contract without company-confidential research data.

- portfolio_cycle.json: independent project lanes and dependency planning.
- capability_routing.json: capability routing against the public registry.
- evidence_report.json: the expected structure of a traceable research deliverable.

Run locally after installation:

kian-nano plan-cycle --input examples/portfolio_cycle.json

kian-nano route --registry registry/cross_domain_capability_registry.json --capability variant_calling
