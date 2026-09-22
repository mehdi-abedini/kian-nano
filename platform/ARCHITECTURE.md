# Kian Nano Karno Agent Platform Architecture v0.2

## Decision
Use a provider-agnostic agent core with a separate model gateway and an automation plane.

- Agent core: deterministic orchestration + specialist agents + evidence ledger.
- Model gateway: OpenAI-compatible abstraction; provider adapters are replaceable.
- Automation plane: self-hosted n8n for schedules, integrations, notifications and proposal workflows.
- Research execution: audited tools, APIs and reproducible compute; n8n must not become the scientific reasoning core.
- Knowledge: public registry is sanitized; confidential company knowledge remains private.
- Governance: every external write, publication, customer reply, code change or registry mutation is approval-gated.

## Provider strategy
Primary gateway candidate: LiteLLM, because it exposes a unified OpenAI-style interface across many providers and supports routing, spend tracking and load balancing. It is an implementation candidate, not a scientific dependency.

KIE is an economical media/task provider candidate for image, video, audio and selected chat models. It should be isolated behind an adapter and used only where its economics, retention and reliability pass a provider gate.

NVIDIA NIM is a strategic provider for high-value biomedical/scientific workloads and for future self-hosting. Its hosted and self-hosted APIs are OpenAI-compatible, and its catalog includes healthcare, genomics and molecular-design services.

Experiential Labs is a gateway candidate for provider comparison, zero-retention-aware routing and cost/throughput experiments. Do not make it the sole dependency.

Conduit is treated as an integration/gateway family, not a single assumed product. The exact Conduit instance must be identified before production integration because similarly named services have materially different purposes.

## Runtime layers
1. Web/API layer: authentication, tenancy, quotas, billing, file intake and user-facing chat.
2. Agent runtime: task decomposition, state, tools, evidence ledger, validation and synthesis.
3. Model gateway: provider routing, retries, budgets, health and cost accounting.
4. Tool/MCP layer: databases, search, GitHub, scientific APIs, code execution and private tools.
5. Automation layer: n8n schedules, inbound/outbound communication and maintenance loops.
6. Data layer: Postgres/object storage/vector retrieval/observability.

## n8n role
n8n owns event-driven automation, not core reasoning. It may trigger research jobs, poll provider health, discover new repositories/models, prepare update proposals, route support messages, generate FAQ candidates and request approval. It must never silently publish or mutate the agent definition.

## Update loop
Discover -> normalize -> audit -> benchmark -> propose -> human approval -> merge/deploy -> smoke test -> monitor -> rollback if needed.

## Cost control
Every request receives a budget class. Router selection considers task capability, context, latency, provider health, privacy posture and estimated cost. Cheap models handle classification/extraction; stronger models handle synthesis, difficult reasoning and adjudication. Provider outages fail over only within an approved capability class.

## Resume-safe execution
Long jobs persist state and provenance. Every artifact records model/provider, version when known, tool versions, source dates, prompt/contract identifier, execution timestamp and validation status.
