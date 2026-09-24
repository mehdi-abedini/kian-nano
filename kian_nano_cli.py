from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

from capability_registry import route_capabilities
from portfolio_orchestrator import plan_cycle


def validate_registry_files(paths: Iterable[Path]) -> list[str]:
    errors: list[str] = []
    for path in paths:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{path}: invalid JSON: {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{path}: root must be an object")
        if "schema_version" not in data:
            errors.append(f"{path}: missing schema_version")
    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="kian-nano", description="Kian Nano Karno research-agent utilities")
    sub = parser.add_subparsers(dest="command", required=True)
    plan = sub.add_parser("plan-cycle", help="Plan independently executable research lanes")
    plan.add_argument("--input", required=True, type=Path)
    route = sub.add_parser("route", help="Route a capability request against a registry")
    route.add_argument("--registry", required=True, type=Path)
    route.add_argument("--capability", required=True)
    route.add_argument("--privacy", default="public")
    validate = sub.add_parser("validate-registries", help="Validate JSON registry files")
    validate.add_argument("paths", nargs="+", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "plan-cycle":
        lanes = json.loads(args.input.read_text(encoding="utf-8"))
        print(json.dumps(plan_cycle(lanes), indent=2, ensure_ascii=False))
        return 0
    if args.command == "route":
        data = json.loads(args.registry.read_text(encoding="utf-8"))
        records = data.get("capabilities", data if isinstance(data, list) else [])
        result = route_capabilities(records, {"required_capability": args.capability, "privacy": args.privacy})
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    errors = validate_registry_files(args.paths)
    for error in errors:
        print(error)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
