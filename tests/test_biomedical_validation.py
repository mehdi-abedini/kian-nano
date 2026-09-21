import unittest

from biomedical_validation import (
    build_data_evidence_manifest,
    validate_subject_split,
    summarize_timebase,
    coverage_report,
)


class BiomedicalValidationTests(unittest.TestCase):
    def test_manifest_requires_evidence_class_and_source_version(self):
        manifest = build_data_evidence_manifest(
            source="PhysioNet",
            version="1.1.0",
            evidence_class="PUBLIC_SYNCHRONIZED_DATA",
            subject_ids=["S1", "S2"],
            calibration_metadata=True,
            preprocessing=[],
        )
        self.assertEqual(manifest["evidence_class"], "PUBLIC_SYNCHRONIZED_DATA")
        self.assertEqual(manifest["version"], "1.1.0")

    def test_subject_split_rejects_overlap(self):
        with self.assertRaises(ValueError):
            validate_subject_split({"S1", "S2"}, {"S2", "S3"})

    def test_timebase_detects_nominal_rate(self):
        out = summarize_timebase([0.0, 0.002, 0.004, 0.006], nominal_hz=500)
        self.assertEqual(out["anomalous_intervals"], 0)
        self.assertAlmostEqual(out["effective_hz"], 500.0)

    def test_coverage_preserves_rejected_windows(self):
        out = coverage_report([True, False, True, False])
        self.assertEqual(out["total"], 4)
        self.assertEqual(out["accepted"], 2)
        self.assertEqual(out["rejected"], 2)


if __name__ == "__main__":
    unittest.main()
