from genomics_public_execution_contract import validate_public_execution
import json, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CONTRACT=ROOT/'genomics_public_execution_contract.py'

class TestPublicExecutionContract(unittest.TestCase):
    def base(self):
        return {
          'benchmark_id':'GIAB-HG002-v5.0q', 'access':'public', 'input_manifest_hash':'sha256:input',
          'reference':{'assembly':'GRCh38','reference_id':'sha256:ref','annotation':'GENCODE50'},
          'workflow':{'engine':'Nextflow','pipeline':'nf-core/sarek','version':'3.10.0'},
          'container_digest':'sha256:image', 'parameters_hash':'sha256:param',
          'truth_set':{'id':'GIAB-HG002-v5.0q','scope':'small-variants'},
          'metrics':['precision','recall','F1'], 'outputs':{'vcf':'sha256:vcf'},
          'claim_gate':'benchmark-only'
        }
    def test_valid(self): self.assertEqual(validate_public_execution(self.base()), [])
    def test_public_only(self):
        r=self.base(); r['access']='controlled'; self.assertIn('access', validate_public_execution(r))
    def test_reference_lock(self):
        r=self.base(); del r['reference']; self.assertIn('reference', validate_public_execution(r))
    def test_workflow_pin(self):
        r=self.base(); r['workflow']['version']='latest'; self.assertIn('workflow', validate_public_execution(r))
    def test_truth_scope(self):
        r=self.base(); r['truth_set']={}; self.assertIn('truth_set', validate_public_execution(r))
    def test_claim_gate(self):
        r=self.base(); r['claim_gate']='clinical'; self.assertIn('claim_gate', validate_public_execution(r))

if __name__=='__main__': unittest.main()
