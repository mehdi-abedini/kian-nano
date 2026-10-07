# Contributing

## Scope

Contributions should improve public research infrastructure without weakening evidence provenance, reproducibility, security, privacy, or intellectual-property boundaries.

## Before changing the project

- Keep routing and workflow policy focused in `SKILL.md`.
- Put detailed domain knowledge in `references/`.
- Put deterministic validation in scripts or testable modules.
- Add or update evaluation assets when trigger or routing behavior changes.
- Do not add secrets, credentials, confidential company information, customer records, or patent-sensitive material.
- Keep public capability claims aligned with executable evidence.

## Change design

For non-trivial changes, describe:

1. the problem or contract being changed;
2. the expected behavior;
3. the evidence supporting the change;
4. the affected modules and boundaries;
5. the validation strategy;
6. known limitations and unresolved risks.

Prefer small, reviewable changes over broad refactors without an explicit acceptance criterion.

## Validation

At minimum, review:

1. YAML/frontmatter where applicable;
2. referenced files and links;
3. evaluation prompts or fixtures affected by routing behavior;
4. unit/regression tests;
5. security and secret hygiene;
6. documentation consistency;
7. deterministic CLI behavior where relevant;
8. the final Git diff and repository status.

For Python changes, a clean-environment check should include:

```bash
python -m pip install -e ".[test]"
python -m compileall -q .
python -m pytest -q
```

## Pull requests

A pull request should state:

- what behavior or documentation changed;
- why the change is needed;
- what evidence supports it;
- tests and validation performed;
- known limitations;
- whether the public/private boundary is affected.

Do not describe unimplemented or unverified capabilities as production-ready.

## Review standard

Reviewers should check behavioral correctness, determinism, provenance, uncertainty handling, dependency/security boundaries, reproducibility, and whether the claim made by the documentation is supported by the implementation.

Consequential or irreversible actions remain subject to explicit human authorization.

## Public evidence boundary

The public repository is not a substitute for access-controlled review of private Kian Nano Karno systems. Public documentation may expose architecture and validation principles without disclosing confidential implementation.

See [docs/REVIEWER_GUIDE.md](docs/REVIEWER_GUIDE.md) and [docs/KHWARIZMI_PUBLIC_EVIDENCE.md](docs/KHWARIZMI_PUBLIC_EVIDENCE.md).
