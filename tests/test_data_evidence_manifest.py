import unittest

from evidence_contract import validate_data_evidence_manifest


class DataEvidenceManifestTests(unittest.TestCase):
    def test_complete_manifest_passes(self):
        manifest = {
            "contract_version": "1.0",
            "evidence_class": "PUBLIC_SYNCHRONIZED_DATA",
            "claim_class": "PUBLIC_SYNCHRONIZED_DATA",
            "source_version": "ptt-1.1.0",
            "provenance_id": "physionet-ptt-1.1.0-s1",
            "source_uri": "https://physionet.org/content/pulse-transit-time-ppg/1.1.0/",
            "subject_scope": {"subjects": ["s1"]},
            "preprocessing_hash": "none",
            "calibration_state": "not_applicable_public_dataset",
            "quality_coverage": {"total": 100, "accepted": 95, "rejected": 5},
            "reference_id": "ecg-r-peaks",
            "artifact_hash": "sha256:example",
        }
        self.assertTrue(validate_data_evidence_manifest(manifest))

    def test_missing_provenance_is_rejected(self):
        manifest = {
            "contract_version": "1.0",
            "evidence_class": "PUBLIC_SYNCHRONIZED_DATA",
            "claim_class": "PUBLIC_SYNCHRONIZED_DATA",
            "source_version": "ptt-1.1.0",
        }
        with self.assertRaises(ValueError):
            validate_data_evidence_manifest(manifest)

    def test_invalid_coverage_is_rejected(self):
        manifest = {
            "contract_version": "1.0",
            "evidence_class": "PUBLIC_SYNCHRONIZED_DATA",
            "claim_class": "PUBLIC_SYNCHRONIZED_DATA",
            "source_version": "ptt-1.1.0",
            "provenance_id": "x",
            "source_uri": "https://example.org",
            "subject_scope": {"subjects": ["s1"]},
            "preprocessing_hash": "none",
            "calibration_state": "not_applicable_public_dataset",
            "quality_coverage": {"total": 10, "accepted": 11, "rejected": -1},
            "reference_id": "ref",
            "artifact_hash": "sha256:x",
        }
        with self.assertRaises(ValueError):
            validate_data_evidence_manifest(manifest)


if __name__ == "__main__":
    unittest.main()
