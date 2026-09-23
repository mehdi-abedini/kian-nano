"""Cross-domain capability registry and evidence-aware routing primitives.
Public-safe metadata only; confidential project payloads must never enter records.
"""
from __future__ import annotations

LICENSE_SCORES = {"MIT": 0.95, "BSD-3-Clause": 0.95, "Apache-2.0": 0.95, "GPL-3.0": 0.80, "CC-BY": 0.85, "service": 0.70, "varies": 0.40}

WEIGHTS = {
    "relevance": 0.30,
    "evidence": 0.20,
    "reproducibility": 0.15,
    "maintenance": 0.10,
    "license_score": 0.10,
    "uncertainty_fit": 0.10,
    "integration": 0.05,
}

def score_capability(record, query=None):
    """Return an auditable score; this is routing utility, not scientific validity."""
    query = query or {}
    values = {}
    for key in WEIGHTS:
        value = record.get(key, 0.0)
        if key == "license_score":
            value = record.get("license_score", LICENSE_SCORES.get(record.get("license"), 0.20))
        if key == "relevance" and query.get("required_capability"):
            value = 1.0 if query["required_capability"] in record.get("capabilities", []) else value
        values[key] = max(0.0, min(1.0, float(value)))
    return round(sum(values[k] * w for k, w in WEIGHTS.items()), 6)

def route_capabilities(records, query):
    """Filter by hard gates, then sort by transparent soft evidence score."""
    candidates = []
    for record in records:
        if record.get("status") in {"reject", "blocked"}:
            continue
        if query.get("privacy") and query["privacy"] not in record.get("privacy", ["public"]):
            continue
        if query.get("required_capability") and query["required_capability"] not in record.get("capabilities", []):
            continue
        if query.get("license") and query["license"] != record.get("license"):
            continue
        item = dict(record)
        item["routing_score"] = score_capability(record, query)
        candidates.append(item)
    return sorted(candidates, key=lambda x: (-x["routing_score"], x.get("id", "")))


def validate_record(record):
    required = ("id", "domain", "source_type", "capabilities", "status", "license", "privacy")
    errors = [field for field in required if field not in record]
    if not isinstance(record.get("capabilities", []), list):
        errors.append("capabilities")
    for key in WEIGHTS:
        if key in record and not 0 <= float(record[key]) <= 1:
            errors.append(key)
    return errors
