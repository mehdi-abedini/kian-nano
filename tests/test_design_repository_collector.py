import unittest
from design_repository_collector import rank_candidates


class DesignRepositoryCollectorTests(unittest.TestCase):
    def test_relevance_and_provenance_drive_rank(self):
        candidates = [
            {
                "repository": "org/design-system",
                "description": "Accessible responsive design system for web products",
                "source_type": "first_party",
                "license": "MIT",
                "archived": False,
                "updated_at": "2026-09-20",
            },
            {
                "repository": "user/random-ui",
                "description": "Personal UI experiments",
                "source_type": "community_analysis",
                "license": "unknown",
                "archived": False,
                "updated_at": "2026-01-01",
            },
        ]
        ranked = rank_candidates(candidates, focus_terms=["design system", "web", "accessibility"])
        self.assertEqual(ranked[0]["repository"], "org/design-system")
        self.assertGreater(ranked[0]["score"], ranked[1]["score"])

    def test_archived_and_clone_signals_are_penalized(self):
        candidates = [{
            "repository": "user/site-clone",
            "description": "Clone of a famous website",
            "source_type": "community_analysis",
            "license": "unknown",
            "archived": True,
            "updated_at": "2025-01-01",
        }]
        ranked = rank_candidates(candidates, focus_terms=["design"])
        self.assertLess(ranked[0]["score"], 0.5)
        self.assertIn("similarity_or_clone_risk", ranked[0]["risk_flags"])

    def test_duplicate_repositories_are_collapsed(self):
        candidates = [
            {"repository": "Org/Design-System", "description": "web design system", "source_type": "first_party"},
            {"repository": "org/design-system", "description": "web design system", "source_type": "first_party"},
        ]
        ranked = rank_candidates(candidates, focus_terms=["design"])
        self.assertEqual(len(ranked), 1)


if __name__ == "__main__":
    unittest.main()
