import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "benchmarks/genomics_public_smoke/variantbenchmarking_run_evidence_2026-09-23.json"

class VariantBenchmarkEvidenceTests(unittest.TestCase):
    def test_variantbenchmarking_evidence_passes_deterministic_grader(self):
        from benchmarks.genomics_public_smoke.grader import grade_variantbenchmarking_run
        record = json.loads(EVIDENCE.read_text(encoding="utf-8"))
        result = grade_variantbenchmarking_run(record)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["failed_checks"], [])

    def test_variantbenchmarking_evidence_rejects_failed_execution(self):
        from benchmarks.genomics_public_smoke.grader import grade_variantbenchmarking_run
        record = json.loads(EVIDENCE.read_text(encoding="utf-8"))
        record["exit_code"] = 1
        record["processes"]["failed"] = 1
        result = grade_variantbenchmarking_run(record)
        self.assertEqual(result["status"], "FAIL")
        self.assertIn("exit_code", result["failed_checks"])
        self.assertIn("processes_failed", result["failed_checks"])

if __name__ == "__main__":
    unittest.main()
