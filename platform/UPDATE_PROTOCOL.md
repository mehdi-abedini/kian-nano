# Continuous Agent Improvement Protocol

## Objective
Keep the Kian agent current without allowing autonomous drift.

### Daily discovery
- Scan approved GitHub repositories, model catalogs, scientific APIs and agent/tool registries.
- Detect new releases, breaking changes, security notices and useful capabilities.
- Store candidates with source URL, date, version, license and evidence.

### Weekly evaluation
- Run a fixed regression suite.
- Benchmark candidate providers/models on representative Kian tasks.
- Measure quality, citation integrity, latency, failure rate and estimated cost.
- Generate a change proposal; do not auto-merge.

### Monthly architecture review
- Review provider concentration risk.
- Review tool permissions and secrets.
- Remove stale integrations.
- Review benchmark drift and task coverage.
- Produce an architecture decision record when a material change is accepted.

### Safety boundary
Automatic discovery may create a proposal. It may not publish, alter production prompts, grant tool permissions, expose confidential data, send external messages or deploy code without an approval gate.
