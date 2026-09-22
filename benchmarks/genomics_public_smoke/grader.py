import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))


def grade(record):
    required = manifest["expected"]["required_fields"]
    missing = [field for field in required if field not in record]
    return {"status": "PASS" if not missing else "FAIL", "missing": missing}


def grade_sarek_run(record):
    failed_checks = []

    workflow = record.get("workflow", {})
    if workflow.get("repository") != "nf-core/sarek":
        failed_checks.append("workflow_repository")
    if workflow.get("version") != "3.10.0":
        failed_checks.append("workflow_version")
    if record.get("privacy") != "public-data-only":
        failed_checks.append("privacy")
    if record.get("status") != "PASS":
        failed_checks.append("status")
    if record.get("exit_code") != 0:
        failed_checks.append("exit_code")

    processes = record.get("processes", {})
    if processes.get("succeeded", 0) <= 0:
        failed_checks.append("processes_succeeded")
    if processes.get("failed", 0) != 0:
        failed_checks.append("processes_failed")

    artifacts = record.get("artifacts", {})
    for name in ("trace", "report", "timeline"):
        artifact = artifacts.get(name, {})
        if not artifact.get("exists") or not artifact.get("non_empty"):
            failed_checks.append(f"artifact_{name}")

    if record.get("outputs", {}).get("non_empty_file_count", 0) <= 0:
        failed_checks.append("non_empty_outputs")

    return {
        "status": "PASS" if not failed_checks else "FAIL",
        "failed_checks": failed_checks,
    }


def grade_variantbenchmarking_run(record):
    failed_checks = []

    workflow = record.get("workflow", {})
    if workflow.get("repository") != "nf-core/variantbenchmarking":
        failed_checks.append("workflow_repository")
    if workflow.get("version") != "1.5.0":
        failed_checks.append("workflow_version")
    if record.get("privacy") != "public-data-only":
        failed_checks.append("privacy")
    if record.get("status") != "PASS":
        failed_checks.append("status")
    if record.get("exit_code") != 0:
        failed_checks.append("exit_code")

    processes = record.get("processes", {})
    if processes.get("succeeded", 0) <= 0:
        failed_checks.append("processes_succeeded")
    if processes.get("failed", 0) != 0:
        failed_checks.append("processes_failed")
    if processes.get("aborted", 0) != 0:
        failed_checks.append("processes_aborted")

    artifacts = record.get("artifacts", {})
    for name in ("trace", "report", "timeline", "multiqc_report", "summary_csv"):
        artifact = artifacts.get(name, {})
        if not artifact.get("exists") or not artifact.get("non_empty"):
            failed_checks.append(f"artifact_{name}")

    metrics = record.get("benchmark_metrics", [])
    if not metrics:
        failed_checks.append("benchmark_metrics")
    else:
        for metric in metrics:
            if not metric.get("tool"):
                failed_checks.append("metric_tool")
                break
            for field in ("TP_base", "FP", "TP_comp", "FN", "Recall", "Precision", "F1"):
                if field not in metric:
                    failed_checks.append(f"metric_{field}")
                    break

    return {
        "status": "PASS" if not failed_checks else "FAIL",
        "failed_checks": failed_checks,
    }


if __name__ == "__main__":
    sample = {
        "id": "smoke-record",
        "category": "benchmark",
        "confidence": "high",
        "last_verified": "2026-09-21",
    }
    print(json.dumps(grade(sample), sort_keys=True))
