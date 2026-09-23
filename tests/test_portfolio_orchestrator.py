import unittest
from portfolio_orchestrator import plan_cycle


class PortfolioOrchestratorTests(unittest.TestCase):
    def test_independent_lanes_run_when_one_lane_is_blocked(self):
        lanes = [
            {"project_id": "L05", "status": "ready", "dependencies": []},
            {"project_id": "L13", "status": "blocked", "dependencies": [], "blocker": "server_access"},
            {"project_id": "L12", "status": "ready", "dependencies": []},
        ]
        plan = plan_cycle(lanes)
        self.assertEqual(plan["executable"], ["L05", "L12"])
        self.assertEqual(plan["blocked"], ["L13"])

    def test_dependency_blocks_only_dependent_lane(self):
        lanes = [
            {"project_id": "L12", "status": "ready", "dependencies": []},
            {"project_id": "L13", "status": "ready", "dependencies": ["L12"]},
            {"project_id": "L05", "status": "ready", "dependencies": []},
        ]
        plan = plan_cycle(lanes)
        self.assertEqual(plan["executable"], ["L05", "L12"])
        self.assertEqual(plan["waiting_on_dependency"], {"L13": ["L12"]})

    def test_failed_lane_does_not_corrupt_other_lanes(self):
        lanes = [
            {"project_id": "L12", "status": "failed", "dependencies": []},
            {"project_id": "L05", "status": "ready", "dependencies": []},
        ]
        plan = plan_cycle(lanes)
        self.assertEqual(plan["executable"], ["L05"])
        self.assertEqual(plan["failed"], ["L12"])


if __name__ == "__main__":
    unittest.main()
