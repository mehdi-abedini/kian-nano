import unittest

from reference_emulator import build_synchronized_reference, estimate_rate


class ReferenceEmulatorTests(unittest.TestCase):
    def test_synchronized_reference_has_expected_timebase(self):
        data = build_synchronized_reference(duration_s=10, hz=500, bpm=60)
        self.assertEqual(len(data["time_s"]), 5000)
        self.assertEqual(data["time_s"][0], 0.0)
        self.assertAlmostEqual(data["time_s"][-1], 9.998, places=6)
        self.assertEqual(data["ecg"], data["ppg"])

    def test_rate_estimation_recovers_reference_rate(self):
        data = build_synchronized_reference(duration_s=30, hz=500, bpm=72)
        self.assertAlmostEqual(estimate_rate(data["time_s"], data["beat_index"]), 72.0, places=6)

    def test_invalid_rate_is_rejected(self):
        with self.assertRaises(ValueError):
            build_synchronized_reference(duration_s=10, hz=500, bpm=0)


if __name__ == "__main__":
    unittest.main()
