import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))

def grade(record):
    required = manifest["expected"]["required_fields"]
    missing = [field for field in required if field not in record]
    return {"status": "PASS" if not missing else "FAIL", "missing": missing}

if __name__ == "__main__":
    sample = {
        "id": "smoke-record",
        "category": "benchmark",
        "confidence": "high",
        "last_verified": "2026-09-21",
    }
    print(json.dumps(grade(sample), sort_keys=True))
