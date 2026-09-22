import json
from pathlib import Path
from genomics_execution_contract import validate_execution_record

ROOT = Path(__file__).resolve().parent
class GenomicsPlanError(ValueError):
    pass

def _load_registry():
    return json.loads((ROOT / "registry" / "genomics_pipelines.json").read_text(encoding="utf-8-sig"))

def _select_pipeline(request):
    modality = str(request.get("modality", "")).lower()
    estimand = str(request.get("estimand", "")).lower()
    candidates = []
    for p in _load_registry()["pipelines"]:
        text = " ".join([p["id"], *p["modalities"], *p["tasks"]]).lower()
        if modality in text or any(t in estimand for t in p["tasks"]):
            candidates.append(p)
    if not candidates:
        raise GenomicsPlanError(f"No audited pipeline registered for modality={request.get("modality")!r}")
    candidates.sort(key=lambda p: p["id"])
    return candidates[0]

def build_genomics_plan(request):
    if not isinstance(request, dict):
        raise GenomicsPlanError("request must be a dict")
    errors = validate_execution_record(request)
    if errors:
        raise GenomicsPlanError("invalid execution contract: " + ", ".join(errors))
    if request["data_access"] == "public" and request["governance"].get("human_genomic_data") != "excluded":
        raise GenomicsPlanError("public execution cannot include human genomic data")
    if request["workflow"].get("version") in (None, "", "latest"):
        raise GenomicsPlanError("workflow version must be pinned")
    if request["claim_gate"] == "clinical":
        raise GenomicsPlanError("clinical claims require a separate validated clinical pathway")
    pipeline = _select_pipeline(request)
    if request["workflow"]["workflow_id"].lower() != pipeline["repository"].lower():
        raise GenomicsPlanError("requested workflow is not the registered pipeline")
    if request["workflow"]["version"] != pipeline["version"]:
        raise GenomicsPlanError(f"workflow version mismatch: request={request["workflow"]["version"]} registry={pipeline["version"]}")
    command = f"nextflow run {pipeline["repository"]} -r {pipeline["version"]} -profile {pipeline["profile"]} --input samplesheet.csv --outdir results -resume"
    benchmark_command = f"nextflow run {pipeline["repository"]} -r {pipeline["version"]} -profile {pipeline["profile"]} --outdir benchmark_results -resume"
    return {
        "project_id": request["project_id"], "claim_gate": request["claim_gate"],
        "reference_lock": request["reference_lock"],
        "pipeline": {"id":pipeline["id"],"engine":pipeline["engine"],"repository":pipeline["repository"],"version":pipeline["version"]},
        "execution": {"mode":"benchmark-first","nextflow_command":command,"benchmark_command":benchmark_command,"resume":True,"human_genomic_data":request["governance"]["human_genomic_data"]},
        "quality_gates": request["qc_requirements"], "provenance": request["provenance"], "benchmark": request["benchmark_plan"]
    }

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Build a governed genomics execution plan")
    parser.add_argument("request_json", type=Path)
    args = parser.parse_args()
    request = json.loads(args.request_json.read_text(encoding="utf-8-sig"))
    print(json.dumps(build_genomics_plan(request), indent=2, sort_keys=True))
