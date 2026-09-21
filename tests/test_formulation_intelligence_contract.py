import unittest
from formulation_intelligence_contract import validate_formulation_record
class T(unittest.TestCase):
 def base(self): return {'formulation_id':'F1','carrier_class':'lipid_nanoparticle','components':[{'id':'L1','ratio':0.7},{'id':'L2','ratio':0.3}],'process':{'method':'microfluidic','cpp':{'flow_rate':10}},'cqa':{'size_nm':90,'pdi':0.12,'encapsulation_pct':92},'measurement_context':{'method':'DLS','replicates':3},'provenance_id':'public:test'}
 def test_valid(self): self.assertEqual(validate_formulation_record(self.base()),[])
 def test_pdi_out_of_range_rejected(self): r=self.base(); r['cqa']['pdi']=1.2; self.assertTrue(validate_formulation_record(r))
 def test_missing_process_rejected(self): r=self.base(); del r['process']; self.assertTrue(validate_formulation_record(r))
