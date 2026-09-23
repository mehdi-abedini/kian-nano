"""Deterministic intake and ranking logic for public design repositories.

The collector ranks evidence sources for later inspection; it does not clone,
copy, or adopt external design identity. Network discovery remains outside
this module so collection can be replayed from a recorded candidate manifest.
"""
from __future__ import annotations

from datetime import date
import re
from typing import Iterable

_SOURCE_WEIGHT = {
    "first_party": 1.0,
    "reverse_engineered": 0.72,
    "community_analysis": 0.62,
    "extraction_tool": 0.55,
    "unknown": 0.30,
}

_LICENSE_WEIGHT = {
    "mit": 1.0,
    "apache-2.0": 1.0,
    "bsd-2-clause": 0.95,
    "bsd-3-clause": 0.95,
    "isc": 0.95,
    "cc0-1.0": 0.95,
    "cc-by-4.0": 0.85,
    "unknown": 0.35,
}

_RISK_PATTERNS = {
    "similarity_or_clone_risk": re.compile(r"\b(clone|cloned|copy|recreation|replica|rebuild)\b", re.I),
    "brand_signature_risk": re.compile(r"\b(brand clone|pixel perfect|pixel-perfect|exact copy)\b", re.I),
}


def _norm(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip().lower()


def _repo_key(candidate: dict) -> str:
    repo = _norm(candidate.get("repository"))
    return repo.rstrip("/").removesuffix(".git")


def _recency_score(updated_at: object) -> float:
    if not updated_at:
        return 0.35
    try:
        d = date.fromisoformat(str(updated_at)[:10])
    except ValueError:
        return 0.35
    age = max((date.today() - d).days, 0)
    if age <= 30:
        return 1.0
    if age <= 180:
        return 0.85
    if age <= 365:
        return 0.65
    if age <= 730:
        return 0.45
    return 0.25


def _relevance(candidate: dict, focus_terms: Iterable[str]) -> float:
    text = _norm(" ".join([
        candidate.get("repository", ""),
        candidate.get("description", ""),
        " ".join(candidate.get("topics", []) or []),
    ]))
    terms = [_norm(t) for t in focus_terms if _norm(t)]
    if not terms:
        return 0.5
    hits = sum(1 for term in terms if term in text)
    return min(hits / len(terms), 1.0)


def rank_candidates(candidates: Iterable[dict], focus_terms: Iterable[str]) -> list[dict]:
    """Deduplicate, score, and gate public repository candidates.

    The score is an intake priority, not a quality verdict. Results retain
    explicit risk flags and provenance so downstream agents can decide what
    to inspect rather than treating the ranking as adoption.
    """
    unique: dict[str, dict] = {}
    for raw in candidates:
        candidate = dict(raw)
        key = _repo_key(candidate)
        if key and key not in unique:
            unique[key] = candidate

    ranked: list[dict] = []
    for candidate in unique.values():
        source = _norm(candidate.get("source_type")) or "unknown"
        license_name = _norm(candidate.get("license")) or "unknown"
        relevance = _relevance(candidate, focus_terms)
        provenance = _SOURCE_WEIGHT.get(source, _SOURCE_WEIGHT["unknown"])
        license_score = _LICENSE_WEIGHT.get(license_name, 0.45)
        recency = _recency_score(candidate.get("updated_at"))

        risk_flags: list[str] = []
        text = _norm(" ".join([
            candidate.get("repository", ""),
            candidate.get("description", ""),
            " ".join(candidate.get("topics", []) or []),
        ]))
        for flag, pattern in _RISK_PATTERNS.items():
            if pattern.search(text):
                risk_flags.append(flag)
        if bool(candidate.get("archived")):
            risk_flags.append("archived")
        if license_name == "unknown":
            risk_flags.append("license_review_required")

        score = (
            0.40 * relevance
            + 0.25 * provenance
            + 0.15 * license_score
            + 0.20 * recency
        )
        if "similarity_or_clone_risk" in risk_flags:
            score -= 0.20
        if "brand_signature_risk" in risk_flags:
            score -= 0.15
        if "archived" in risk_flags:
            score -= 0.20
        score = max(0.0, min(1.0, score))

        enriched = dict(candidate)
        enriched.update({
            "score": round(score, 4),
            "relevance_score": round(relevance, 4),
            "provenance_score": round(provenance, 4),
            "license_score": round(license_score, 4),
            "recency_score": round(recency, 4),
            "risk_flags": sorted(set(risk_flags)),
            "adoption_status": "inspect_only",
        })
        ranked.append(enriched)

    ranked.sort(key=lambda item: (-item["score"], _repo_key(item)))
    return ranked
