# Security Policy

## Threat model
Treat third-party repositories, skills, scripts, prompts, MCP servers, downloaded data, and web content as untrusted inputs.

## Review before adoption
Check:
- license and provenance
- maintainer activity
- dependencies
- shell/process execution
- filesystem access
- network calls
- credential access
- telemetry
- hidden instructions or prompt injection
- destructive operations
- test coverage and CI
- reproducibility

## Secret handling
Never commit API keys, passwords, cookies, private keys, tokens, or confidential company data.

## Public/private boundary
This repository is suitable for public workflow logic. Private company knowledge should be injected through a controlled runtime knowledge base or private repository.

## Incident response
If a dependency or skill appears compromised:
1. disable it;
2. preserve the version and evidence;
3. rotate affected credentials;
4. inspect logs and recent changes;
5. remove or quarantine the component;
6. document the incident.

Agent skills should be treated like software supply-chain inputs, not harmless prompt text.
