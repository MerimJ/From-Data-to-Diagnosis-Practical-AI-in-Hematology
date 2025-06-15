import unittest
import pandas as pd
import os
from src.hematology.analyzer import Analyzer

class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            "Hemoglobin": [10.2],
            "RDW": [16.1],
            "Platelets": [48000]
        }
        self.csv_path = "test_labs.csv"
        pd.DataFrame(self.sample_data).to_csv(self.csv_path, index=False)
        self.analyzer = Analyzer(self.csv_path)

    def test_analysis_keys(self):
        result = self.analyzer.analyze().generate_report()
        self.assertIn("Diagnosis", result)
        self.assertIn("Confidence", result)
        self.assertIn("Comment", result)

    def tearDown(self):
        os.remove(self.csv_path)

if __name__ == "__main__":
    unittest.main()
