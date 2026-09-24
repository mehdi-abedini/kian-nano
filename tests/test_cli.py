from pathlib import Path

from kian_nano_cli import build_parser, validate_registry_files


def test_cli_exposes_plan_cycle_and_route_commands():
    parser = build_parser()
    assert parser.parse_args(["plan-cycle", "--input", "lanes.json"]).command == "plan-cycle"
    assert parser.parse_args(["route", "--registry", "registry.json", "--capability", "variant_calling"]).command == "route"


def test_registry_validator_accepts_public_json_registry(tmp_path: Path):
    registry = tmp_path / "registry.json"
    registry.write_text('{"schema_version":"1.0","classification":"PUBLIC-SANITIZED","capabilities":[]}', encoding="utf-8")
    errors = validate_registry_files([registry])
    assert errors == []
