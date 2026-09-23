"""Pure planning logic for multi-project portfolio cycles.

This module decides which lanes are independently executable in the current
cycle. It does not execute tools, mutate project data, or bypass approvals.
"""
from __future__ import annotations


_TERMINAL = {"completed", "failed", "blocked"}


def plan_cycle(lanes: list[dict]) -> dict:
    by_id = {str(lane["project_id"]): lane for lane in lanes}
    executable: list[str] = []
    blocked: list[str] = []
    failed: list[str] = []
    waiting: dict[str, list[str]] = {}

    for lane in sorted(lanes, key=lambda item: str(item["project_id"])):
        project_id = str(lane["project_id"])
        status = str(lane.get("status", "ready"))
        dependencies = [str(dep) for dep in lane.get("dependencies", [])]

        if status == "failed":
            failed.append(project_id)
            continue
        if status == "blocked":
            blocked.append(project_id)
            continue

        unresolved = []
        for dep in dependencies:
            dependency = by_id.get(dep)
            if dependency is None:
                unresolved.append(dep)
                continue
            dep_status = str(dependency.get("status", "ready"))
            if dep_status != "completed":
                unresolved.append(dep)

        if unresolved:
            waiting[project_id] = unresolved
        elif status not in _TERMINAL:
            executable.append(project_id)

    return {
        "executable": executable,
        "blocked": blocked,
        "failed": failed,
        "waiting_on_dependency": waiting,
    }
