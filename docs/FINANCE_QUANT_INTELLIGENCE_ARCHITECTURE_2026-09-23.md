# Finance & Quantitative Intelligence Architecture — 2026-09-23

## Objective
Build a research-grade financial/commodity intelligence subsystem for analysis rather than autonomous trading.

## Data model
Every observation should preserve:
source_id, instrument_id, observation_time, release_time, vintage, timezone, calendar, units, currency, adjustment_state, retrieval_time, source_version.

## Information-set discipline
For historical analysis, the system must reconstruct what was knowable at the decision timestamp. Current revised macro data must not be silently substituted for the historical vintage. Corporate disclosures use publication/release time rather than period-end alone.

## Iran-specific layer
The Iran module separates TSE/IFB market data, Codal disclosures, IME commodity instruments, and FX/gold supplementary context. It must explicitly handle Persian calendars, market holidays, price limits, trading halts, corporate actions, symbol changes, splits/rights issues, and instrument-specific microstructure.

## Commodity layer
Track physical/reference commodities, futures, options, inventory/supply indicators, freight/geopolitical variables where sourced, and local-vs-global basis relationships. Do not mix spot, futures settlement, indicative quotes and producer prices without explicit semantic mapping.

## Analytical layers
1. Data quality and provenance
2. Fundamental analysis
3. Market microstructure
4. Technical/statistical features
5. Cross-asset/commodity relationships
6. Risk and scenario analysis
7. Backtesting
8. Event studies
9. Forecasting
10. Decision-support synthesis

## Validation
Backtests require walk-forward or otherwise time-ordered validation, explicit transaction costs/slippage, corporate-action handling, survivorship controls, no leakage, and benchmark comparisons. Forecasts must report uncertainty and calibration rather than only point estimates.

## Governance
No autonomous order placement. Consequential financial analysis should retain a human-review gate. Public artifacts must not contain private portfolios, credentials, broker information or transaction instructions.

## Current source verification
Official/primary sources are preferred. Community TSETMC API documentation is useful for endpoint discovery but explicitly describes itself as unofficial; current access may be geographically constrained. Official FRED/ALFRED supports real-time periods/vintages; IMF and World Bank provide dated commodity datasets; EIA provides open energy data; SEC provides public XBRL/filing APIs. These properties are encoded as routing metadata rather than assumptions.
