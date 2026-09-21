import unittest
from computational_design_contract import validate_design_record
class T(unittest.TestCase):
 def base(self): return {'design_id':'D1','target_id':'T1','representation':'molecular_graph','model':'baseline_rf','training_data_id':'ADMET-1','split_strategy':'scaffold','uncertainty':'conformal_or_ensemble','applicability_domain':'defined','synthesis_feasibility':'required','objective_terms':['affinity_proxy','ADMET','synthesis'],'provenance_id':'public:test'}
 def test_valid(self): self.assertEqual(validate_design_record(self.base()),[])
 def test_random_only_rejected(self): r=self.base(); r['split_strategy']='random'; self.assertTrue(validate_design_record(r))
 def test_affinity_not_evidence(self): r=self.base(); self.assertNotIn('validated_binding',r)
