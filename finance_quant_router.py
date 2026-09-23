"""Financial/market intelligence routing primitives.

This module is analytical only. It explicitly blocks routes that cannot reconstruct
the information set required for a defensible historical or point-in-time claim.
"""
from __future__ import annotations

REQUIRED_FOR_BACKTEST = {
    "point_in_time", "corporate_action_adjustment", "survivorship_bias",
    "lookahead_bias", "transaction_costs"
}

def validate_finance_task(task: dict) -> list[str]:
    errors=[]
    if task.get("analysis_type") in {"backtest","historical_signal"}:
        missing=[x for x in REQUIRED_FOR_BACKTEST if not task.get(x, False)]
        errors.extend(f"missing_gate:{x}" for x in missing)
    if task.get("market") in {"iran_equity","iran_commodities"} and not task.get("market_calendar"):
        errors.append("missing_gate:market_calendar")
    if task.get("decision_impact") == "high" and not task.get("human_review", False):
        errors.append("missing_gate:human_review")
    return errors

def route_finance_sources(records, task):
    errors=validate_finance_task(task)
    if errors:
        return {"status":"blocked","errors":errors,"candidates":[]}
    candidates=[]
    for r in records:
        if r.get("status") in {"blocked","reject"}:
            continue
        if task.get("domain") and task["domain"] not in r.get("domain","") and r.get("domain") not in task.get("compatible_domains",[]):
            continue
        if task.get("requires_primary") and r.get("provenance") != "primary":
            continue
        if task.get("requires_pit") and not r.get("point_in_time",False):
            continue
        candidates.append(r)
    candidates.sort(key=lambda x:(x.get("provenance")!="primary",x.get("status")!="use",x["id"]))
    return {"status":"ready","errors":[],"candidates":candidates}

def evidence_key(source_id, instrument_id, observation_time, release_time=None, vintage=None):
    return {
        "source_id":source_id,
        "instrument_id":instrument_id,
        "observation_time":observation_time,
        "release_time":release_time,
        "vintage":vintage,
    }
