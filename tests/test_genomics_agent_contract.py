import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class GenomicsAgentContractTests(unittest.TestCase):
    def test_genomics_module_exists_and_defines_required_controls(self):
        module = (ROOT / "references" / "genomics.md").read_text(encoding="utf-8")
        for phrase in (
            "reference lock",
            "sample identity",
            "benchmark-first",
            "single-cell",
            "spatial",
            "foundation model",
            "claim-evidence ledger",
            "clinical interpretation",
        ):
            self.assertIn(phrase, module.lower())

    def test_skill_routes_genomics_to_specialized_module(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8").lower()
        self.assertIn("references/genomics.md", skill)
        self.assertIn("genomics / ngs", skill)
        self.assertIn("agentic genomics", skill)


if __name__ == "__main__":
    unittest.main()
