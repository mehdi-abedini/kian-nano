import unittest
from genomics_execution_contract import validate_execution_record

class GenomicsExecutionContractTests(unittest.TestCase):
    def base(self):
        return {
            'project_id':'KNN-GX-001',
            'modality':'WGS',
            'question_id':'Q1',
            'estimand':'germline SNV/indel discovery',
            'data_access':'public',
            'sample_manifest_id':'manifest:sha256:abc',
            'raw_input_checksums':['sha256:raw1'],
            'reference_lock':{'assembly':'GRCh38','reference_id':'ref:sha256:ref1','annotation':'GENCODE50'},
            'workflow':{'engine':'Nextflow','workflow_id':'nf-core/sarek','version':'3.5.1'},
            'qc_requirements':['identity','contamination','coverage'],
            'benchmark_plan':{'dataset_id':'GIAB.HG002','version':'v5.0q','truth_set':'small-variants'},
            'provenance':{'container_digest':'sha256:img1','parameters_hash':'sha256:param1'},
            'governance':{'human_genomic_data':'excluded','consent_status':'public-dataset'},
            'claim_gate':'research-only'
        }
    def test_valid_record_passes(self):
        self.assertEqual(validate_execution_record(self.base()), [])
    def test_missing_reference_lock_rejected(self):
        r=self.base(); del r['reference_lock']; self.assertIn('reference_lock', validate_execution_record(r))
    def test_unlocked_reference_is_rejected(self):
        r=self.base(); r['reference_lock']={'assembly':'GRCh38'}; self.assertTrue(validate_execution_record(r))
    def test_missing_raw_checksums_rejected(self):
        r=self.base(); r['raw_input_checksums']=[]; self.assertIn('raw_input_checksums', validate_execution_record(r))
    def test_clinical_claim_gate_requires_validation(self):
        r=self.base(); r['claim_gate']='clinical'; self.assertIn('claim_gate', validate_execution_record(r))

if __name__=='__main__': unittest.main()
