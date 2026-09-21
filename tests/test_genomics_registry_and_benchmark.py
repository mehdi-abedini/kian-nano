import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class GenomicsRegistryTests(unittest.TestCase):
    def test_registry_files_exist_and_have_stable_fields(self):
        required = (
            "references.yaml",
            "datasets.yaml",
            "pipelines.yaml",
            "tools.yaml",
            "agents.yaml",
            "foundation_models.yaml",
            "schema.md",
        )
        for name in required:
            self.assertTrue((ROOT / "registry" / name).exists(), name)

    def test_registry_schema_documents_evidence_and_governance(self):
        schema = (ROOT / "registry" / "schema.md").read_text(encoding="utf-8").lower()
        for phrase in ("last_verified", "benchmark_evidence", "license", "privacy", "failure_modes"):
            self.assertIn(phrase, schema)

    def test_public_benchmark_harness_has_deterministic_contract(self):
        manifest = ROOT / "benchmarks" / "genomics_public_smoke" / "manifest.json"
        grader = ROOT / "benchmarks" / "genomics_public_smoke" / "grader.py"
        self.assertTrue(manifest.exists())
        self.assertTrue(grader.exists())
        data = json.loads(manifest.read_text(encoding="utf-8"))
        self.assertEqual(data["privacy"], "public-data-only")
        self.assertIn("expected", data)


if __name__ == "__main__":
    unittest.main()
