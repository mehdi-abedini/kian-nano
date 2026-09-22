import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
POLICY = ROOT / "platform" / "gateway_policy.json"

class GatewayRouteError(ValueError):
    pass

def _priority(provider):
    order = {"scientific": 0, "reference": 1, "routing-experiment": 2, "standard": 3, "cost-sensitive": 4}
    return order.get(provider.get("priority"), 99)

def choose_provider(config=None, capability="chat", budget_class="standard", privacy="public"):
    if config is None:
        config = json.loads(POLICY.read_text(encoding="utf-8-sig"))
    budget = config.get("budgets", {}).get(budget_class)
    if budget is None:
        raise GatewayRouteError(f"unknown budget class: {budget_class}")
    candidates=[]
    for provider in config.get("providers", []):
        if not provider.get("enabled"): continue
        if capability not in provider.get("capabilities", []): continue
        allowed_privacy = provider.get("privacy", ["public", "private"])
        if privacy not in allowed_privacy: continue
        candidates.append(provider)
    if not candidates:
        raise GatewayRouteError(f"no provider satisfies capability={capability}, privacy={privacy}")
    candidates.sort(key=_priority)
    return {"provider": candidates[0]["id"], "budget_class": budget_class, "privacy": privacy}
