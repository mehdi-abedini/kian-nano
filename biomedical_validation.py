import math


def build_data_evidence_manifest(*, source, version, evidence_class, subject_ids, calibration_metadata, preprocessing):
    if not source or not version or not evidence_class:
        raise ValueError("source, version and evidence_class are required")
    return {
        "source": source,
        "version": version,
        "evidence_class": evidence_class,
        "subject_ids": sorted(set(subject_ids)),
        "calibration_metadata": bool(calibration_metadata),
        "preprocessing": list(preprocessing),
    }


def validate_subject_split(train_subjects, test_subjects):
    overlap = set(train_subjects) & set(test_subjects)
    if overlap:
        raise ValueError("train and test subjects overlap")
    return True


def summarize_timebase(times_s, nominal_hz, tolerance_fraction=0.1):
    times = [float(x) for x in times_s]
    if len(times) < 2:
        raise ValueError("at least two timestamps are required")
    intervals = [b - a for a, b in zip(times, times[1:])]
    if any(dt <= 0 for dt in intervals):
        raise ValueError("timestamps must be strictly increasing")
    ordered = sorted(intervals)
    mid = len(ordered) // 2
    median = ordered[mid] if len(ordered) % 2 else (ordered[mid - 1] + ordered[mid]) / 2
    target = 1.0 / float(nominal_hz)
    anomalous = sum(abs(dt - target) > target * tolerance_fraction for dt in intervals)
    return {
        "median_interval_s": median,
        "effective_hz": 1.0 / median,
        "n_intervals": len(intervals),
        "anomalous_intervals": anomalous,
    }


def coverage_report(accepted_flags):
    flags = [bool(x) for x in accepted_flags]
    if not flags:
        raise ValueError("accepted_flags must not be empty")
    accepted = sum(flags)
    return {"total": len(flags), "accepted": accepted, "rejected": len(flags) - accepted}


_EVIDENCE_LEVEL = {
    "SYNTHETIC": 0,
    "PUBLIC_SYNCHRONIZED_DATA": 1,
    "PHYSICAL_BENCH": 2,
    "CONTROLLED_HUMAN": 3,
    "INTENDED_USE_CLINICAL": 4,
}


def claim_supported_by_evidence(evidence_class, claim_class):
    """Return whether evidence is mature enough for the requested claim class."""
    if evidence_class not in _EVIDENCE_LEVEL or claim_class not in _EVIDENCE_LEVEL:
        raise ValueError("unknown evidence or claim class")
    return _EVIDENCE_LEVEL[evidence_class] >= _EVIDENCE_LEVEL[claim_class]
