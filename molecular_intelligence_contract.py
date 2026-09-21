_REQUIRED = (
    "molecule_id",
    "canonical_smiles",
    "source_id",
    "source_version",
    "properties",
    "assay_context",
    "split_role",
    "provenance_id",
)

_ALLOWED_SPLITS = {"train", "validation", "test", "external"}

def validate_molecule_record(record):
    errors = []
    if not isinstance(record, dict):
        return ["record"]
    for field in _REQUIRED:
        if field not in record:
            errors.append(field)
    if record.get("split_role") not in _ALLOWED_SPLITS:
        errors.append("split_role")
    smiles = record.get("canonical_smiles")
    if not isinstance(smiles, str) or not smiles.strip():
        errors.append("canonical_smiles")
    return errors
