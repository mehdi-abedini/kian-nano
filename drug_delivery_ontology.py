_REQUIRED = (
    "record_id",
    "evidence_class",
    "source_id",
    "drug_id",
    "carrier_class",
    "formulation_inputs",
    "process_parameters",
    "cqa",
    "biological_context",
    "measurement_context",
    "preprocessing_hash",
)

def required_fields():
    return list(_REQUIRED)

def validate_record(record):
    errors = []
    if not isinstance(record, dict):
        return ["record"]
    for field in _REQUIRED:
        if field not in record:
            errors.append(field)
    cqa = record.get("cqa", {})
    if isinstance(cqa, dict) and "pdi" in cqa:
        pdi = cqa["pdi"]
        if not isinstance(pdi, (int, float)) or not 0 <= pdi < 1:
            errors.append("cqa.pdi")
    return errors
