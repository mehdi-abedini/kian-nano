import unittest
from gateway_router import choose_provider, GatewayRouteError

class GatewayRouterTests(unittest.TestCase):
    def test_scientific_genomics_prefers_enabled_scientific_provider(self):
        cfg={"budgets":{"deep":{},"standard":{}}, "providers":[
            {"id":"kie","enabled":True,"capabilities":["chat"],"priority":"cost-sensitive"},
            {"id":"nvidia-nim","enabled":True,"capabilities":["chat","genomics"],"priority":"scientific"}
        ]}
        route=choose_provider(cfg, capability="genomics", budget_class="deep", privacy="public")
        self.assertEqual(route["provider"],"nvidia-nim")

    def test_disabled_provider_is_never_selected(self):
        cfg={"budgets":{"deep":{},"standard":{}}, "providers":[{"id":"nvidia-nim","enabled":False,"capabilities":["genomics"],"priority":"scientific"}]}
        with self.assertRaises(GatewayRouteError): choose_provider(cfg,"genomics","deep","public")

    def test_private_data_rejects_public_only_provider(self):
        cfg={"budgets":{"deep":{},"standard":{}}, "providers":[{"id":"x","enabled":True,"capabilities":["chat"],"priority":"standard","privacy":["public"]}]}
        with self.assertRaises(GatewayRouteError): choose_provider(cfg,"chat","standard","private")

if __name__=="__main__": unittest.main()
