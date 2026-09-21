import unittest

from drug_delivery_ontology import validate_record, required_fields


class DrugDeliveryOntologyTests(unittest.TestCase):
    def test_valid_record_has_core_provenance_and_measurement_fields(self):
        record = {
            "record_id": "DD-001",
            "evidence_class": "PUBLIC_DATASET",
            "source_id": "doi:example",
            "drug_id": "CHEMBL1",
            "carrier_class": "PLGA_NP",
            "formulation_inputs": {"drug_loading": 0.12},
            "process_parameters": {"method": "nanoprecipitation"},
            "cqa": {"particle_size_nm": 120.0, "pdi": 0.18},
            "biological_context": {"model": "in_vitro"},
            "measurement_context": {"method": "DLS"},
            "preprocessing_hash": "sha256:abc",
        }
        self.assertEqual(validate_record(record), [])

    def test_missing_core_field_is_rejected(self):
        record = {"record_id": "DD-002"}
        errors = validate_record(record)
        self.assertIn("source_id", errors)

    def test_invalid_cqa_value_is_rejected(self):
        record = {
            "record_id": "DD-003",
            "evidence_class": "PUBLIC_DATASET",
            "source_id": "doi:example",
            "drug_id": "CHEMBL1",
            "carrier_class": "LNP",
            "formulation_inputs": {},
            "process_parameters": {},
            "cqa": {"pdi": 1.2},
            "biological_context": {},
            "measurement_context": {},
            "preprocessing_hash": "sha256:abc",
        }
        errors = validate_record(record)
        self.assertIn("cqa.pdi", errors)

    def test_required_fields_are_explicit_and_stable(self):
        self.assertIn("drug_id", required_fields())
        self.assertIn("carrier_class", required_fields())
        self.assertIn("preprocessing_hash", required_fields())


if __name__ == "__main__":
    unittest.main()
