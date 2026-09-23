# Finance, Quantitative Research, and Trading

## Scope
Use for macroeconomic research, equities, financial statements, portfolio analysis,
quantitative signals, commodities, derivatives, risk, and trading research.

## Source hierarchy
1. Official exchange, regulator, issuer, central-bank, statistical-agency data.
2. Licensed institutional providers with documented provenance.
3. Public secondary providers for cross-checking and convenience.
4. Community APIs only as discovery/fallback until independently validated.

## Point-in-time integrity
Never use information that would not have been available at the historical decision timestamp.
Record observation time, publication/availability time, filing date, revision/vintage status,
timezone, provider/source, and licensing constraints.

## Iran/TSE
Use jurisdiction-specific conventions. Distinguish official TSETMC/Codal data from
third-party feeds and preserve Iranian calendar/time conventions when material.

## Commodities
Cover energy, metals, agriculture, freight/weather where relevant, using official or
licensed price/fundamental sources. Cross-check spot, futures, physical benchmarks,
inventories, supply/demand, and macro drivers rather than treating price alone as evidence.

## Backtesting
Report universe, period, costs, slippage, liquidity, survivorship handling, corporate
actions, benchmark, rebalancing, out-of-sample results, drawdown, and risk. A backtest
is not evidence of future performance.
