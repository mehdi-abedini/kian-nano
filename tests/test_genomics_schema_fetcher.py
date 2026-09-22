import unittest
from genomics_schema_fetcher import schema_url, SchemaFetchError

class SchemaFetcherTests(unittest.TestCase):
    def test_pinned_url(self):
        self.assertEqual(schema_url("nf-core/sarek","3.10.0","nextflow_schema.json"),"https://raw.githubusercontent.com/nf-core/sarek/3.10.0/nextflow_schema.json")
    def test_main_rejected(self):
        with self.assertRaises(SchemaFetchError): schema_url("nf-core/sarek","main","nextflow_schema.json")
    def test_unknown_file_rejected(self):
        with self.assertRaises(SchemaFetchError): schema_url("nf-core/sarek","3.10.0","README.md")

if __name__=="__main__": unittest.main()
