from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

_ALLOWED_ANALYSES = {"snapshot", "historical", "fundamental", "technical",
                     "macro", "commodity", "backtest", "risk", "screening"}
_ALLOWED_SOURCE_CLASSES = {"official", "licensed", "public-secondary", "community"}
_ALLOWED_ACCESS = {"api", "file", "web", "database"}

@dataclass(frozen=True)
class MarketAnalysisRequest:
    market: str
    asset_class: str
    instrument: str
    analysis: str
    decision_timestamp: str | None = None
    require_point_in_time: bool = False
    currency: str | None = None
    timezone: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class FinanceDataPoint:
    instrument: str
    observed_at: str
    value: float
    source_id: str
    available_at: str | None = None
    revised_at: str | None = None
    currency: str | None = None

    def __post_init__(self) -> None:
        validate_datapoint(self)

@dataclass(frozen=True)
class ProviderRecord:
    id: str
    market_scope: list[str]
    source_class: str
    access: str
    point_in_time: bool
    requires_key: bool = False
    licensing: str = "verify"
    region_restrictions: list[str] = field(default_factory=list)
    capabilities: list[str] = field(default_factory=list)
    fallback_only: bool = False

def _valid_timestamp(value: str | None) -> bool:
    if not value:
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False

def validate_market_request(req: MarketAnalysisRequest) -> dict[str, Any]:
    if not req.market or not req.asset_class or not req.instrument:
        raise ValueError("market, asset_class and instrument are required")
    if req.analysis not in _ALLOWED_ANALYSES:
        raise ValueError(f"unsupported analysis: {req.analysis}")
    if req.decision_timestamp and not _valid_timestamp(req.decision_timestamp):
        raise ValueError("decision_timestamp must be ISO-8601")
    if req.analysis == "backtest" and not req.require_point_in_time:
        raise ValueError("backtests require point-in-time integrity")
    return {"market": req.market, "asset_class": req.asset_class,
            "instrument": req.instrument, "analysis": req.analysis,
            "point_in_time_required": req.require_point_in_time}
def validate_datapoint(point: FinanceDataPoint) -> None:
    if not point.instrument or not point.source_id:
        raise ValueError("instrument and source_id are required")
    if not _valid_timestamp(point.observed_at):
        raise ValueError("observed_at must be ISO-8601")
    if point.available_at and not _valid_timestamp(point.available_at):
        raise ValueError("available_at must be ISO-8601")
    if point.revised_at and not _valid_timestamp(point.revised_at):
        raise ValueError("revised_at must be ISO-8601")

def validate_provider(provider: ProviderRecord) -> None:
    if provider.source_class not in _ALLOWED_SOURCE_CLASSES:
        raise ValueError("unsupported source_class")
    if provider.access not in _ALLOWED_ACCESS:
        raise ValueError("unsupported access mode")
    if not provider.id or not provider.market_scope:
        raise ValueError("provider id and market_scope are required")
