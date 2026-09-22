# Model Gateway Phase

LiteLLM is being used as the implementation candidate for the internal model gateway because its current documentation supports a unified OpenAI-style interface, routing/retry/fallback, spend tracking, budgets, authentication and a Docker-based proxy deployment. It remains an implementation layer; KNN scientific contracts and routing policy remain upstream.

No provider credential is stored in the repository. All endpoints and secrets are environment variables.

Current config is intentionally non-production: provider models are placeholders until each provider adapter is individually verified for endpoint semantics, authentication, privacy/retention, pricing and reliability.

Deployment gate:

1. Docker runtime healthy.
2. LiteLLM container starts.
3. `/health` responds.
4. Each provider adapter passes a minimal authenticated smoke test.
5. Cost attribution and failure/fallback behavior are verified.
6. Only then may a provider be enabled in `gateway_policy.json`.
