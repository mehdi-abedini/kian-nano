import unittest
from genomics_agent import build_genomics_plan, GenomicsPlanError

class GenomicsAgentTests(unittest.TestCase):
    def request(self):
        return {
            "project_id":"KNN-GX-001", "modality":"WGS",
            "question_id":"Q1", "estimand":"germline SNV/indel discovery",
            "data_access":"public", "sample_manifest_id":"manifest:sha256:abc",
            "raw_input_checksums":["sha256:raw1"],
            "reference_lock":{"assembly":"GRCh38","reference_id":"ref:sha256:ref1","annotation":"GENCODE50"},
            "workflow":{"engine":"Nextflow","workflow_id":"nf-core/sarek","version":"3.10.0"},
            "qc_requirements":["identity","contamination","coverage"],
            "benchmark_plan":{"dataset_id":"GIAB.HG002","version":"v5.0q","truth_set":"small-variants"},
            "provenance":{"container_digest":"sha256:img1","parameters_hash":"sha256:param1"},
            "governance":{"human_genomic_data":"excluded","consent_status":"public-dataset"},
            "claim_gate":"research-only"
        }
    def test_builds_deterministic_plan(self):
        plan = build_genomics_plan(self.request())
        self.assertEqual(plan["pipeline"]["id"], "nfcore-sarek")
        self.assertEqual(plan["pipeline"]["version"], "3.10.0")
        self.assertEqual(plan["execution"]["mode"], "benchmark-first")
        self.assertIn("-resume", plan["execution"]["nextflow_command"])
        self.assertEqual(plan["claim_gate"], "research-only")

    def test_rejects_confidential_data_for_public_mode(self):
        r=self.request(); r["data_access"]="public"; r["governance"]["human_genomic_data"]="included"
        with self.assertRaises(GenomicsPlanError): build_genomics_plan(r)

    def test_rejects_unpinned_workflow(self):
        r=self.request(); r["workflow"]["version"]="latest"
        with self.assertRaises(GenomicsPlanError): build_genomics_plan(r)

    def test_rejects_clinical_claim(self):
        r=self.request(); r["claim_gate"]="clinical"
        with self.assertRaises(GenomicsPlanError): build_genomics_plan(r)

if __name__=="__main__": unittest.main()
