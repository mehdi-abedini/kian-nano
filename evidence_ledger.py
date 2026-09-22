"""Append-only, hash-chained evidence ledger for auditable research execution."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


_EVIDENCE_LEVEL = {
    "SYNTHETIC": 0,
    "PUBLIC_SYNCHRONIZED_DATA": 1,
    "PHYSICAL_BENCH": 2,
    "CONTROLLED_HUMAN": 3,
    "INTENDED_USE_CLINICAL": 4,
}

_REQUIRED = (
    "task_id",
    "evidence_class",
    "claim_class",
    "source",
    "source_version",
    "provenance_id",
    "artifact_hash",
    "status",
)


class LedgerIntegrityError(ValueError):
    """Raised when an evidence ledger is missing, malformed, or tampered."""


def _canonical(payload: dict[str, Any]) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _record_hash(payload: dict[str, Any]) -> str:
    return "sha256:" + hashlib.sha256(_canonical(payload).encode("utf-8")).hexdigest()


class EvidenceLedger:
    """Append-only JSONL ledger with deterministic record hashes and hash chaining."""

    def __init__(self, path: str | Path):
        self.path = Path(path)

    def _read_records(self) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []
        records: list[dict[str, Any]] = []
        for line_number, line in enumerate(
            self.path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise LedgerIntegrityError(
                    f"invalid JSON at line {line_number}"
                ) from exc
            if not isinstance(record, dict):
                raise LedgerIntegrityError(f"record at line {line_number} is not an object")
            records.append(record)
        return records

    def records(self) -> list[dict[str, Any]]:
        self.verify()
        return self._read_records()

    @property
    def latest_hash(self) -> str | None:
        records = self._read_records()
        return records[-1].get("record_hash") if records else None

    def append(self, record: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(record, dict):
            raise ValueError("record must be a mapping")
        missing = [key for key in _REQUIRED if not record.get(key)]
        if missing:
            raise ValueError("missing required evidence fields: " + ", ".join(missing))

        evidence_class = record["evidence_class"]
        claim_class = record["claim_class"]
        if evidence_class not in _EVIDENCE_LEVEL or claim_class not in _EVIDENCE_LEVEL:
            raise ValueError("unknown evidence or claim class")
        if _EVIDENCE_LEVEL[evidence_class] < _EVIDENCE_LEVEL[claim_class]:
            raise ValueError("evidence class cannot support requested claim class")

        status = record["status"]
        if status not in {"PASS", "FAIL", "REVIEW"}:
            raise ValueError("status must be PASS, FAIL, or REVIEW")

        # Refuse to append to a corrupted ledger.
        self.verify()

        previous_hash = self.latest_hash
        payload = dict(record)
        payload["sequence"] = len(self._read_records()) + 1
        payload["timestamp_utc"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        payload["previous_hash"] = previous_hash
        payload["record_hash"] = _record_hash(payload)

        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(_canonical(payload) + "\n")
        return payload

    def verify(self) -> bool:
        records = self._read_records()
        previous_hash = None
        for index, record in enumerate(records, start=1):
            if record.get("sequence") != index:
                raise LedgerIntegrityError(f"invalid sequence at record {index}")
            if record.get("previous_hash") != previous_hash:
                raise LedgerIntegrityError(f"invalid previous_hash at record {index}")
            stored_hash = record.get("record_hash")
            if not stored_hash:
                raise LedgerIntegrityError(f"missing record_hash at record {index}")
            payload = dict(record)
            payload.pop("record_hash", None)
            calculated_hash = _record_hash(payload)
            if stored_hash != calculated_hash:
                raise LedgerIntegrityError(f"record hash mismatch at record {index}")
            previous_hash = stored_hash
        return True

