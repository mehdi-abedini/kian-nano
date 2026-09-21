import unittest
from nanobio_interaction_contract import validate_interaction_record
class T(unittest.TestCase):
 def base(self): return {'interaction_id':'N1','formulation_id':'F1','biological_context':{'cell_model':'A549','species':'human'},'exposure':{'dose':'10 ug/mL','duration_h':24},'endpoints':{'uptake':{'value':1,'unit':'relative'},'toxicity':{'value':0.1,'unit':'fraction'}},'controls':['free_drug','empty_carrier'],'method':'flow_cytometry','provenance_id':'public:test'}
 def test_valid(self): self.assertEqual(validate_interaction_record(self.base()),[])
 def test_missing_control_rejected(self): r=self.base(); r['controls']=[]; self.assertTrue(validate_interaction_record(r))
 def test_context_required(self): r=self.base(); del r['biological_context']; self.assertTrue(validate_interaction_record(r))
