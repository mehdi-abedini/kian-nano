import json
from pathlib import Path
from finance_quant_router import validate_finance_task, route_finance_sources

ROOT=Path(__file__).resolve().parents[1]

def test_finance_registry_is_valid_json():
    d=json.loads((ROOT/"registry"/"finance_ecosystem_registry.json").read_text(encoding="utf-8"))
    assert d["schema_version"]=="1.0"
    assert d["classification"]=="PUBLIC-SANITIZED"
    assert len(d["capabilities"])>=10

def test_backtest_is_blocked_without_bias_and_point_in_time_gates():
    errors=validate_finance_task({"analysis_type":"backtest"})
    assert "missing_gate:point_in_time" in errors
    assert "missing_gate:lookahead_bias" in errors

def test_primary_point_in_time_routing():
    records=json.loads((ROOT/"registry"/"finance_ecosystem_registry.json").read_text(encoding="utf-8"))["capabilities"]
    out=route_finance_sources(records,{"domain":"macro_finance","requires_primary":True,"requires_pit":True,"market_calendar":True})
    assert out["status"]=="ready"
    assert out["candidates"]
    assert out["candidates"][0]["provenance"]=="primary"
