import unittest
from pathlib import Path
import tempfile

from scripts.validate_agent_package import validate_repository


class ValidateAgentPackageTests(unittest.TestCase):
    def test_valid_minimal_repository_passes(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'SKILL.md').write_text('---\nname: x\ndescription: y\n---\n', encoding='utf-8')
            (root / 'registry').mkdir()
            (root / 'registry' / 'agent.yaml').write_text('id: x\nversion: 0.1.0\n', encoding='utf-8')
            (root / 'evals').mkdir()
            (root / 'evals' / 'evals.md').write_text('identify evidence\ncite dated sources\n', encoding='utf-8')
            self.assertEqual(validate_repository(root), [])

    def test_secret_pattern_is_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'SKILL.md').write_text('---\nname: x\ndescription: y\n---\n', encoding='utf-8')
            (root / 'registry').mkdir()
            (root / 'registry' / 'agent.yaml').write_text('id: x\nversion: 0.1.0\n', encoding='utf-8')
            (root / 'evals').mkdir()
            (root / 'evals' / 'evals.md').write_text('sk-' + 'abcdefghijklmnopqrstuvwxyz\n', encoding='utf-8')
            self.assertTrue(any('secret' in e.lower() for e in validate_repository(root)))

    def test_ignored_runtime_environment_is_not_scanned(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'SKILL.md').write_text('---\nname: x\ndescription: y\n---\n', encoding='utf-8')
            (root / 'registry').mkdir()
            (root / 'registry' / 'agent.yaml').write_text('id: x\nversion: 0.1.0\n', encoding='utf-8')
            (root / 'evals').mkdir()
            (root / 'evals' / 'evals.md').write_text('identify evidence\ncite dated sources\n', encoding='utf-8')
            (root / '.venv' / 'Lib').mkdir(parents=True)
            (root / '.venv' / 'Lib' / 'fixture.py').write_text('sk-' + 'abcdefghijklmnopqrstuvwxyz\n', encoding='utf-8')
            self.assertEqual(validate_repository(root), [])


if __name__ == '__main__': unittest.main()
