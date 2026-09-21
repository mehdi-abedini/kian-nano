import unittest
from translation_ip_contract import validate_translation_record
class T(unittest.TestCase):
 def base(self): return {'candidate_id':'C1','development_stage':'preclinical_r_and_d','intended_use':'research_only','manufacturing_status':'development','regulatory_jurisdiction':'unspecified','ip_status':'screening_only','fto_status':'not_assessed','claim_boundaries':['no clinical efficacy claim'],'evidence_ledger_id':'E1','confidentiality':'controlled'}
 def test_valid(self): self.assertEqual(validate_translation_record(self.base()),[])
 def test_unassessed_fto_blocks_product_claim(self): r=self.base(); r['intended_use']='commercial_product'; self.assertTrue(validate_translation_record(r))
 def test_confidentiality_required(self): r=self.base(); r['confidentiality']=''; self.assertTrue(validate_translation_record(r))
