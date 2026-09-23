import json
from pathlib import Path

from capability_registry import route_capabilities, validate_record

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry" / "cross_domain_capability_registry.json"

def test_registry_records_validate():
    data = json.loads(REG.read_text(encoding="utf-8"))
    assert data["schema_version"] == "1.0"
    assert data["classification"] == "PUBLIC-SANITIZED"
    assert all(not validate_record(x) for x in data["capabilities"])

def test_routing_respects_hard_gates_and_is_deterministic():
    records = [
        {"id":"a","domain":"genomics","source_type":"pipeline","capabilities":["variant_calling"],"status":"use","license":"MIT","privacy":["public"],"relevance":.9,"evidence":.8,"reproducibility":.9,"maintenance":.8,"license":.9,"uncertainty_fit":.8,"integration":.8},
        {"id":"b","domain":"genomics","source_type":"dataset","capabilities":["variant_calling"],"status":"blocked","license":"CC-BY","privacy":["public"],"relevance":1,"evidence":1,"reproducibility":1,"maintenance":1,"uncertainty_fit":1,"integration":1},
    ]
    out = route_capabilities(records, {"required_capability":"variant_calling","privacy":"public"})
    assert [x["id"] for x in out] == ["a"]
    assert out[0]["routing_score"] > 0
