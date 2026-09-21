import unittest

from molecular_intelligence_contract import validate_molecule_record


class MolecularIntelligenceContractTests(unittest.TestCase):
    def test_valid_molecule_record_passes(self):
        record = {
            "molecule_id": "CHEMBL1",
            "canonical_smiles": "CCO",
            "source_id": "chembl",
            "source_version": "current",
            "properties": {"logp": 0.1, "solubility_logmol_l": -0.5},
            "assay_context": {"target_id": "CHEMBL_T1"},
            "split_role": "train",
            "provenance_id": "prov-1",
        }
        self.assertEqual(validate_molecule_record(record), [])

    def test_missing_provenance_is_rejected(self):
        record = {
            "molecule_id": "CHEMBL1",
            "canonical_smiles": "CCO",
            "source_id": "chembl",
            "source_version": "current",
            "properties": {},
            "assay_context": {},
            "split_role": "train",
        }
        self.assertIn("provenance_id", validate_molecule_record(record))

    def test_unknown_split_role_is_rejected(self):
        record = {
            "molecule_id": "CHEMBL1",
            "canonical_smiles": "CCO",
            "source_id": "chembl",
            "source_version": "current",
            "properties": {},
            "assay_context": {},
            "split_role": "random",
            "provenance_id": "prov-1",
        }
        self.assertIn("split_role", validate_molecule_record(record))


if __name__ == "__main__":
    unittest.main()
