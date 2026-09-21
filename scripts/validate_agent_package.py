from pathlib import Path
import re

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"-----BEGIN (RSA|OPENSSH|EC|PRIVATE) KEY-----"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
]
REQUIRED_EVAL_PHRASES = ("identify evidence", "cite dated sources")


def validate_repository(root: Path) -> list[str]:
    errors = []
    skill = root / "SKILL.md"
    if not skill.exists():
        errors.append("missing SKILL.md")
    else:
        text = skill.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            errors.append("SKILL.md: malformed frontmatter")
        elif "name:" not in text[:text.find("\n---\n", 4)]:
            errors.append("SKILL.md: missing name")
        if "description:" not in text[:text.find("\n---\n", 4)]:
            errors.append("SKILL.md: missing description")
    registry = root / "registry" / "agent.yaml"
    if not registry.exists():
        errors.append("missing registry/agent.yaml")
    evals = root / "evals" / "evals.md"
    if not evals.exists():
        errors.append("missing evals/evals.md")
    else:
        et = evals.read_text(encoding="utf-8").lower()
        for phrase in REQUIRED_EVAL_PHRASES:
            if phrase not in et:
                errors.append(f"evals/evals.md: missing acceptance phrase: {phrase}")
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if any(rx.search(content) for rx in SECRET_PATTERNS):
            errors.append(f"secret-pattern detected: {path.relative_to(root)}")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Agent package validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
