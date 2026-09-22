import json
import tempfile
import unittest
from pathlib import Path

from evidence_ledger import EvidenceLedger, LedgerIntegrityError


class EvidenceLedgerTests(unittest.TestCase):
    def test_append_creates_hash_chained_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ledger.jsonl"
            ledger = EvidenceLedger(path)
            first = ledger.append({
                "task_id": "T1",
                "evidence_class": "PUBLIC_SYNCHRONIZED_DATA",
                "claim_class": "PUBLIC_SYNCHRONIZED_DATA",
                "source": "nf-core/sarek",
                "source_version": "3.10.0",
                "provenance_id": "prov-a",
                "artifact_hash": "sha256:a",
                "status": "PASS",
            })
            second = ledger.append({
                "task_id": "T2",
                "evidence_class": "PUBLIC_SYNCHRONIZED_DATA",
                "claim_class": "PUBLIC_SYNCHRONIZED_DATA",
                "source": "nf-core/variantbenchmarking",
                "source_version": "1.5.0",
                "provenance_id": "prov-b",
                "artifact_hash": "sha256:b",
                "status": "PASS",
            })
            self.assertIsNone(first["previous_hash"])
            self.assertEqual(second["previous_hash"], first["record_hash"])
            self.assertTrue(ledger.verify())
            self.assertEqual(len(path.read_text(encoding="utf-8").splitlines()), 2)

    def test_missing_required_provenance_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger = EvidenceLedger(Path(tmp) / "ledger.jsonl")
            with self.assertRaises(ValueError):
                ledger.append({
                    "task_id": "T1",
                    "evidence_class": "PUBLIC_SYNCHRONIZED_DATA",
                    "claim_class": "PUBLIC_SYNCHRONIZED_DATA",
                    "source": "example",
                    "source_version": "1",
                    "artifact_hash": "sha256:a",
                    "status": "PASS",
                })

    def test_tampering_breaks_verification(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ledger.jsonl"
            ledger = EvidenceLedger(path)
            ledger.append({
                "task_id": "T1",
                "evidence_class": "PUBLIC_SYNCHRONIZED_DATA",
                "claim_class": "PUBLIC_SYNCHRONIZED_DATA",
                "source": "example",
                "source_version": "1",
                "provenance_id": "prov-a",
                "artifact_hash": "sha256:a",
                "status": "PASS",
            })
            raw = json.loads(path.read_text(encoding="utf-8"))
            raw["status"] = "FAIL"
            path.write_text(json.dumps(raw) + "\n", encoding="utf-8")
            with self.assertRaises(LedgerIntegrityError):
                ledger.verify()

    def test_invalid_claim_level_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            ledger = EvidenceLedger(Path(tmp) / "ledger.jsonl")
            with self.assertRaises(ValueError):
                ledger.append({
                    "task_id": "T1",
                    "evidence_class": "PUBLIC_SYNCHRONIZED_DATA",
                    "claim_class": "PHYSICAL_BENCH",
                    "source": "example",
                    "source_version": "1",
                    "provenance_id": "prov-a",
                    "artifact_hash": "sha256:a",
                    "status": "PASS",
                })


if __name__ == "__main__":
    unittest.main()

