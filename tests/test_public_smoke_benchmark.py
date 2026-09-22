import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PublicSmokeBenchmarkTests(unittest.TestCase):
    def test_sarek_run_evidence_passes_deterministic_grader(self):
        from benchmarks.genomics_public_smoke.grader import grade_sarek_run
        evidence = {
            "workflow": {"repository": "nf-core/sarek", "version": "3.10.0"},
            "status": "PASS",
            "exit_code": 0,
            "processes": {"succeeded": 23, "failed": 0},
            "artifacts": {
                "trace": {"exists": True, "non_empty": True},
                "report": {"exists": True, "non_empty": True},
                "timeline": {"exists": True, "non_empty": True},
            },
            "outputs": {"non_empty_file_count": 1},
            "privacy": "public-data-only",
        }
        result = grade_sarek_run(evidence)
        self.assertEqual(result["status"], "PASS")

    def test_sarek_run_evidence_rejects_failed_execution(self):
        from benchmarks.genomics_public_smoke.grader import grade_sarek_run
        evidence = {
            "workflow": {"repository": "nf-core/sarek", "version": "3.10.0"},
            "status": "PASS",
            "exit_code": 1,
            "processes": {"succeeded": 22, "failed": 1},
            "artifacts": {},
            "outputs": {"non_empty_file_count": 0},
            "privacy": "public-data-only",
        }
        result = grade_sarek_run(evidence)
        self.assertEqual(result["status"], "FAIL")
        self.assertIn("exit_code", result["failed_checks"])


if __name__ == "__main__":
    unittest.main()
