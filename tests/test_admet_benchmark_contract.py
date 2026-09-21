import unittest
from admet_benchmark_contract import validate_benchmark_record, link_molecule_to_benchmark

class AdmetBenchmarkContractTests(unittest.TestCase):
    def base(self):
        return {'dataset_id':'TDC.Caco2_Wang','dataset_version':'public-current','task_type':'regression','target':'Caco2','unit':'cm/s','representation':'SMILES','split_strategy':'scaffold','source_id':'TDC','provenance_id':'tdc:Caco2_Wang','counts':{'train':700,'validation':100,'test':106},'metric':'MAE','uncertainty':'required','applicability_domain':'required','leakage_controls':['scaffold','duplicate_check']}
    def test_valid_benchmark_passes(self): self.assertEqual(validate_benchmark_record(self.base()), [])
    def test_missing_leakage_control_rejected(self):
        r=self.base(); r['leakage_controls']=[]; self.assertTrue(validate_benchmark_record(r))
    def test_linkage_keeps_formulation_distinct(self):
        r=link_molecule_to_benchmark('m1','TDC.Caco2_Wang'); self.assertEqual(r['molecule_id'],'m1'); self.assertEqual(r['benchmark_id'],'TDC.Caco2_Wang'); self.assertNotIn('formulation_outcome',r)
if __name__=='__main__': unittest.main()
