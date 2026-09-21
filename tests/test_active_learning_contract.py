import unittest
from active_learning_contract import validate_active_learning_record
class T(unittest.TestCase):
 def base(self): return {'cycle_id':'AL1','candidate_ids':['C1','C2'],'selection_policy':'uncertainty_plus_diversity','acquisition_budget':2,'observations_added':2,'prior_data_id':'DS1','posterior_data_id':'DS2','experiment_linkage':['E1','E2'],'stopping_rule':'predefined','provenance_id':'public:test'}
 def test_valid(self): self.assertEqual(validate_active_learning_record(self.base()),[])
 def test_budget_mismatch_rejected(self): r=self.base(); r['observations_added']=3; self.assertTrue(validate_active_learning_record(r))
 def test_stopping_rule_required(self): r=self.base(); r['stopping_rule']=''; self.assertTrue(validate_active_learning_record(r))
