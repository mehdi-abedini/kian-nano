# Biomedical Measurement Validation Controls

## Evidence ladder

The research agent treats biomedical evidence as typed states:

SYNTHETIC -> PUBLIC_SYNCHRONIZED_DATA -> PHYSICAL_BENCH -> CONTROLLED_HUMAN -> INTENDED_USE/CLINICAL

A lower evidence class must not silently satisfy a higher-risk claim.

## Data-Evidence Manifest

Before statistical or ML evaluation, record:

- source and dataset version/license;
- subject IDs and subject-independent split assignment;
- acquisition modalities and nominal sampling rates;
- timestamp source and synchronization evidence;
- calibration metadata availability;
- missingness and signal-quality coverage;
- rejected records/windows and reason codes;
- preprocessing operations;
- reference/ground-truth definition;
- evidence class;
- reproducibility/version identifier.

## Required controls

The public research-agent implementation provides deterministic helpers for:

- manifest construction;
- subject-split overlap rejection;
- timestamp/timebase characterization;
- explicit accepted/rejected coverage accounting.

Incomplete or malformed observations must remain visible in accounting. Valid rows may be analyzed, but failed rows must not be silently repaired, imputed, or deleted.

## Evaluation gate

A downstream model/fusion evaluation should be blocked when subject overlap exists, reference pairing is absent/ambiguous, synchronization is unverified for synchronization-dependent tasks, or quality/missingness exclusions are unquantified.

These controls govern evidence and reproducibility. They do not establish hardware accuracy, calibration traceability, clinical validity, or regulatory compliance by themselves.
