# Provider and Gateway Matrix

| Provider/gateway | Intended role | Initial status | Gate |
|---|---|---|---|
| LiteLLM | Internal model gateway/router | Candidate | protocol + cost + security test |
| KIE Market | image/video/audio + selected chat | Candidate | API reliability + retention + unit economics |
| NVIDIA NIM | biomedical/scientific models | Candidate | model-specific benchmark + license + GPU economics |
| Experiential Labs | gateway/provider comparison | Candidate | retention + latency + pricing verification |
| Conduit | integration/gateway experiments | Ambiguous | identify exact service + API contract |
| Direct providers | fallback/reference | Candidate | credentials + cost + policy |

## Provider admission criteria
- OpenAI-compatible or a small, isolated adapter.
- Authentication stays server-side.
- Explicit data-retention and training posture.
- Model/version discovery is reproducible.
- Timeout, retry and rate-limit behavior is known.
- Cost can be attributed per task/user/project.
- Scientific claims are never accepted merely because a provider advertises a model.

## Routing policy
Provider selection is capability-first, then privacy, reliability, latency and cost. No global "best model" score is stored. Benchmarks are task-specific and time-stamped.
