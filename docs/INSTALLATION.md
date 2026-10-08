# Installation

## Python package

Requirements:
- Python 3.11 or newer.
- A virtual environment is recommended for local development.

Install the package and its test dependencies from the repository root:

```powershell
python -m pip install -e ".[test]"
```

Run the complete validation suite:

```powershell
python -m pytest
```

The package declares runtime dependencies in `[project.dependencies]` and development/test dependencies in `[project.optional-dependencies]` in `pyproject.toml`. Do not install undeclared scientific libraries into the project environment unless the source code requires them and the dependency is added to project metadata.

## Codex
Place the directory under a supported skills path such as:
C:\\Users\\X\\.agents\\skills\\kian-nano-karno-research-agent

Repository-local alternative:
<repo>\\.agents\\skills\\kian-nano-karno-research-agent

## Verification
1. Confirm SKILL.md exists.
2. Confirm YAML frontmatter is valid.
3. Start Codex.
4. Ask a trigger prompt from evals.
5. Confirm the skill is selected.
6. Request a report and verify evidence, uncertainty, and references are present.

Codex supports repository and user skill locations and loads skill metadata before the full skill body.

## OmniRoute
OmniRoute remains the model gateway. Do not place third-party agent code directly into the routing database. Maintain a separate Kian Agent Registry and let the orchestrator invoke compatible skills through the host runtime.
