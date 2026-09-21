"""Generic typed evidence contracts for research orchestration."""

_REQUIRED = (
    "contract_version", "evidence_class", "claim_class", "source_version",
    "provenance_id", "source_uri", "subject_scope", "preprocessing_hash",
    "calibration_state", "quality_coverage", "reference_id", "artifact_hash",
)
_LEVEL = {
    "SYNTHETIC": 0,
    "PUBLIC_SYNCHRONIZED_DATA": 1,
    "PHYSICAL_BENCH": 2,
    "CONTROLLED_HUMAN": 3,
    "INTENDED_USE_CLINICAL": 4,
}


def validate_data_evidence_manifest(manifest):
    if not isinstance(manifest, dict):
        raise ValueError("manifest must be a mapping")
    missing = [key for key in _REQUIRED if not manifest.get(key)]
    if missing:
        raise ValueError("missing manifest fields: " + ", ".join(missing))
    evidence = manifest["evidence_class"]
    claim = manifest["claim_class"]
    if evidence not in _LEVEL or claim not in _LEVEL:
        raise ValueError("unknown evidence or claim class")
    if _LEVEL[evidence] < _LEVEL[claim]:
        raise ValueError("evidence class cannot support requested claim class")
    coverage = manifest["quality_coverage"]
    if not isinstance(coverage, dict):
        raise ValueError("quality_coverage must be a mapping")
    total = coverage.get("total")
    accepted = coverage.get("accepted")
    rejected = coverage.get("rejected")
    if not all(isinstance(x, int) and not isinstance(x, bool)
               for x in (total, accepted, rejected)):
        raise ValueError("coverage counts must be integers")
    if total < 0 or accepted < 0 or rejected < 0:
        raise ValueError("coverage counts must be non-negative")
    if accepted + rejected != total:
        raise ValueError("coverage counts must sum to total")
    scope = manifest["subject_scope"]
    if not isinstance(scope, dict) or not scope.get("subjects"):
        raise ValueError("subject_scope.subjects is required")
    return True
