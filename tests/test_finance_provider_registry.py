import unittest

from finance_provider_registry import select_finance_providers


class FinanceProviderRegistryTests(unittest.TestCase):
    def test_tehran_equity_prefers_official_tsetmc(self):
        providers = select_finance_providers(
            market="TSE", asset_class="equity", realtime=True, point_in_time=True
        )
        self.assertEqual(providers[0]["id"], "tsetmc-rest")
        self.assertEqual(providers[0]["source_class"], "official")

    def test_energy_commodity_prefers_official_eia_for_us_energy_series(self):
        providers = select_finance_providers(
            market="global", asset_class="energy", realtime=False, point_in_time=True
        )
        ids = [p["id"] for p in providers]
        self.assertIn("eia-api", ids)
        self.assertIn("imf-pcps", ids)

    def test_global_realtime_can_use_licensed_provider_as_fallback(self):
        providers = select_finance_providers(
            market="global", asset_class="commodity", realtime=True, point_in_time=False
        )
        self.assertTrue(any(p["id"] == "twelve-data" for p in providers))


if __name__ == "__main__":
    unittest.main()
