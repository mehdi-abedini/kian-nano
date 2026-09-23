import unittest

from finance_market_contract import (
    FinanceDataPoint,
    MarketAnalysisRequest,
    ProviderRecord,
    validate_market_request,
)


class FinanceMarketContractTests(unittest.TestCase):
    def test_request_requires_point_in_time_integrity_for_backtests(self):
        req = MarketAnalysisRequest(
            market="TSE",
            asset_class="equity",
            instrument="IRO1TEST0001",
            analysis="backtest",
            decision_timestamp="2026-01-15T10:00:00+03:30",
        )
        with self.assertRaises(ValueError):
            validate_market_request(req)

    def test_valid_research_request_preserves_provenance_requirements(self):
        req = MarketAnalysisRequest(
            market="TSE",
            asset_class="equity",
            instrument="IRO1TEST0001",
            analysis="historical",
            decision_timestamp="2026-01-15T10:00:00+03:30",
            require_point_in_time=True,
        )
        result = validate_market_request(req)
        self.assertTrue(result["point_in_time_required"])
        self.assertEqual(result["market"], "TSE")

    def test_datapoint_rejects_missing_source_timestamp(self):
        with self.assertRaises(ValueError):
            FinanceDataPoint(
                instrument="CL",
                observed_at="",
                value=70.0,
                source_id="eia",
            )

    def test_provider_record_distinguishes_primary_and_secondary_sources(self):
        p = ProviderRecord(
            id="tsetmc-rest",
            market_scope=["TSE", "IFB"],
            source_class="official",
            access="api",
            point_in_time=True,
        )
        self.assertEqual(p.source_class, "official")
        self.assertTrue(p.point_in_time)


if __name__ == "__main__":
    unittest.main()
