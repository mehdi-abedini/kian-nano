import unittest

from biomedical_validation import validate_evidence_contract


class EvidenceContractTests(unittest.TestCase):
    def test_valid_contract_passes(self):
        self.assertTrue(validate_evidence_contract({
            "evidence_class": "PUBLIC_SYNCHRONIZED_DATA",
            "claim_class": "PUBLIC_SYNCHRONIZED_DATA",
            "source_version": "1.1.0",
            "provenance_id": "physionet-ptt-v1.1.0",
        }))

    def test_missing_provenance_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_evidence_contract({
                "evidence_class": "PUBLIC_SYNCHRONIZED_DATA",
                "claim_class": "PUBLIC_SYNCHRONIZED_DATA",
                "source_version": "1.1.0",
            })

    def test_incompatible_claim_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_evidence_contract({
                "evidence_class": "PUBLIC_SYNCHRONIZED_DATA",
                "claim_class": "PHYSICAL_BENCH",
                "source_version": "1.1.0",
                "provenance_id": "physionet-ptt-v1.1.0",
            })


if __name__ == "__main__":
    unittest.main()
