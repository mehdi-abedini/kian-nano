import unittest
from validation_package_contract import validate_validation_record
class T(unittest.TestCase):
 def base(self): return {'validation_id':'V1','claim_type':'physicochemical_prediction','evidence_class':'public_data','dataset_ids':['DS1'],'split_strategy':'scaffold','external_validation':False,'replicates':5,'metrics':{'mae':0.2},'uncertainty_reported':True,'failure_cases_recorded':True,'provenance_id':'public:test'}
 def test_valid(self): self.assertEqual(validate_validation_record(self.base()),[])
 def test_no_uncertainty_rejected(self): r=self.base(); r['uncertainty_reported']=False; self.assertTrue(validate_validation_record(r))
 def test_zero_replicates_rejected(self): r=self.base(); r['replicates']=0; self.assertTrue(validate_validation_record(r))
