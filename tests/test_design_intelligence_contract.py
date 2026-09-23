import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class DesignIntelligenceContractTests(unittest.TestCase):
    def test_design_contract_exists(self):
        p = ROOT / "design" / "KKN_DESIGN_CONTRACT.md"
        self.assertTrue(p.is_file())
        text = p.read_text(encoding="utf-8")
        self.assertIn("External references are evidence, not identity", text)
        self.assertIn("Kian Nano Karno fingerprint", text)
        self.assertTrue("human approval" in text.lower() or "human-approval" in text.lower())

    def test_agent_facing_design_md_has_required_sections(self):
        p = ROOT / "design" / "DESIGN.md"
        self.assertTrue(p.is_file())
        text = p.read_text(encoding="utf-8")
        for heading in ("## Overview", "## Colors", "## Typography", "## Layout",
                        "## Elevation & Depth", "## Shapes", "## Components",
                        "## Do's and Don'ts"):
            self.assertIn(heading, text)

    def test_design_registry_separates_provenance(self):
        p = ROOT / "registry" / "design_sources.yaml"
        self.assertTrue(p.is_file())
        text = p.read_text(encoding="utf-8")
        for value in ("first_party", "reverse_engineered", "extraction_tool", "refresh_policy"):
            self.assertIn(value, text)

    def test_skill_wires_design_workflow(self):
        p = ROOT / "SKILL.md"
        text = p.read_text(encoding="utf-8")
        self.assertIn("references/design.md", text)
        self.assertIn("Design Intelligence", text)

if __name__ == "__main__":
    unittest.main()
