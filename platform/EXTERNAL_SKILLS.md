# External Skills and Ecosystem Integration

## Adopted references

### nextflow-io/agent-skills
Repository: https://github.com/nextflow-io/agent-skills

Integrated locally under `platform/external/nextflow-agent-skills` and copied into the Codex skills directory as:

- `nextflow-install-nextflow`
- `nextflow-create-workflow`
- `nextflow-run-module`
- `nextflow-launch-workflow`
- `nextflow-migrate-nextflow-code`

The project is Apache-2.0 and explicitly supports skills-compatible agents including Codex CLI. Its current requirements state Nextflow 26.04+.

### NathanSkene/claude-nextflow-skill
Repository: https://github.com/NathanSkene/claude-nextflow-skill

Used as an architectural reference for schema-at-runtime operation. KNN does not hard-code all nf-core pipeline interfaces; it resolves a pinned pipeline release and retrieves its machine-readable parameter/input schemas.

### UKDRI/informatics_pipeline_skills
Repository: https://github.com/UKDRI/informatics_pipeline_skills

Used as a reference for separating pipeline-specific logic from environment-specific execution, centralizing reference maps, validating parameters, and keeping resource/HPC configuration outside the scientific pipeline contract. It is not installed as a local runtime because it is designed around a UKDRI SLURM environment.

## Integration rule

External skills are references/adapters, not authorities. KNN retains its own execution contract, provenance, governance, evidence gates and human approval boundaries.

Pipeline schemas and versions are treated as external evidence and are cached locally with their source URL/version. A schema change must not silently mutate an existing approved run.
