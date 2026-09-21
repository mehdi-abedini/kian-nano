"""Deterministic synchronized ECG/PPG reference emulator for software verification."""


def build_synchronized_reference(*, duration_s, hz, bpm):
    if duration_s <= 0 or hz <= 0 or bpm <= 0:
        raise ValueError("duration_s, hz and bpm must be positive")
    n = int(round(duration_s * hz))
    time_s = [i / float(hz) for i in range(n)]
    beat_index = [int(t * bpm / 60.0) for t in time_s]
    signal = [1.0 if b != beat_index[i - 1] else 0.0
              for i, b in enumerate(beat_index)]
    return {
        "time_s": time_s,
        "ecg": signal,
        "ppg": signal.copy(),
        "beat_index": beat_index,
        "nominal_hz": hz,
        "bpm": bpm,
    }


def estimate_rate(time_s, beat_index):
    if len(time_s) != len(beat_index) or len(time_s) < 2:
        raise ValueError("time_s and beat_index must have equal length >= 2")
    beats = len(set(beat_index))
    duration = float(time_s[-1] - time_s[0] + (time_s[1] - time_s[0]))
    if duration <= 0 or beats < 2:
        raise ValueError("insufficient reference duration or beats")
    return beats / duration * 60.0
