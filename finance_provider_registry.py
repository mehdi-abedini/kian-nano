PROVIDERS = [
    {
        "id": "tsetmc-rest", "market_scope": ["TSE", "IFB", "IME"],
        "asset_classes": ["equity", "fund", "derivative", "commodity"],
        "source_class": "official", "realtime": True, "point_in_time": True,
        "privacy": ["public"], "region": ["IR"],
        "capabilities": ["quotes", "history", "market-watch", "order-book"],
    },
    {
        "id": "codal", "market_scope": ["IR"],
        "asset_classes": ["equity", "fund", "company"],
        "source_class": "official", "realtime": False, "point_in_time": True,
        "privacy": ["public"], "region": ["IR"],
        "capabilities": ["filings", "financial-statements", "disclosures"],
    },
    {
        "id": "eia-api", "market_scope": ["global"],
        "asset_classes": ["energy", "macro"],
        "source_class": "official", "realtime": False, "point_in_time": True,
        "privacy": ["public"], "region": ["US", "global"],
        "capabilities": ["energy", "oil", "gas", "electricity", "inventories"],
    },
]
PROVIDERS += [
    {
        "id": "imf-pcps", "market_scope": ["global"],
        "asset_classes": ["commodity", "energy", "metals", "agriculture"],
        "source_class": "official", "realtime": False, "point_in_time": True,
        "privacy": ["public"], "region": ["global"],
        "capabilities": ["commodity-prices", "price-indices"],
    },
    {
        "id": "worldbank-commodity", "market_scope": ["global"],
        "asset_classes": ["commodity", "energy", "metals", "agriculture"],
        "source_class": "official", "realtime": False, "point_in_time": True,
        "privacy": ["public"], "region": ["global"],
        "capabilities": ["commodity-prices", "forecasts", "monthly-data"],
    },
    {
        "id": "fred-alfred", "market_scope": ["global"],
        "asset_classes": ["macro", "rates", "fx"],
        "source_class": "official", "realtime": False, "point_in_time": True,
        "privacy": ["public"], "region": ["US", "global"],
        "capabilities": ["macro", "rates", "revisions", "vintages"],
    },
    {
        "id": "cme-market-data", "market_scope": ["global"],
        "asset_classes": ["commodity", "futures", "options", "fx"],
        "source_class": "licensed", "realtime": True, "point_in_time": True,
        "privacy": ["public"], "region": ["global"],
        "capabilities": ["futures", "options", "streaming", "historical"],
    },
]
PROVIDERS += [
    {
        "id": "twelve-data", "market_scope": ["global"],
        "asset_classes": ["equity", "fx", "commodity", "crypto"],
        "source_class": "licensed", "realtime": True, "point_in_time": False,
        "privacy": ["public"], "region": ["global"],
        "capabilities": ["quotes", "history", "technical", "commodities"],
    },
    {
        "id": "streamdata-ir", "market_scope": ["IR", "global"],
        "asset_classes": ["equity", "fx", "commodity", "crypto"],
        "source_class": "licensed", "realtime": True, "point_in_time": False,
        "privacy": ["public"], "region": ["IR", "global"],
        "capabilities": ["TSE", "gold", "fx", "CME", "global-markets"],
    },
]


def select_finance_providers(market, asset_class, realtime=False, point_in_time=False):
    candidates = []
    for provider in PROVIDERS:
        if market not in provider["market_scope"] and "global" not in provider["market_scope"]:
            continue
        if asset_class not in provider["asset_classes"]:
            continue
        if realtime and not provider["realtime"]:
            continue
        if point_in_time and not provider["point_in_time"]:
            continue
        candidates.append(provider)
    return sorted(
        candidates,
        key=lambda p: (p["source_class"] != "official",
                       p["source_class"] != "licensed",
                       not p["point_in_time"])
    )
