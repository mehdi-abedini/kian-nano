import unittest

from biomedical_validation import claim_supported_by_evidence


class EvidenceGateTests(unittest.TestCase):
    def test_public_data_cannot_support_physical_bench_claim(self):
        self.assertFalse(claim_supported_by_evidence("PUBLIC_SYNCHRONIZED_DATA", "PHYSICAL_BENCH"))

    def test_public_data_supports_public_data_claim(self):
        self.assertTrue(claim_supported_by_evidence("PUBLIC_SYNCHRONIZED_DATA", "PUBLIC_SYNCHRONIZED_DATA"))

    def test_physical_bench_cannot_support_human_claim(self):
        self.assertFalse(claim_supported_by_evidence("PHYSICAL_BENCH", "CONTROLLED_HUMAN"))

    def test_higher_evidence_can_support_lower_level_claim(self):
        self.assertTrue(claim_supported_by_evidence("CONTROLLED_HUMAN", "PHYSICAL_BENCH"))


if __name__ == "__main__":
    unittest.main()
