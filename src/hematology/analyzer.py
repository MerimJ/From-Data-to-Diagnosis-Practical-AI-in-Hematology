import pandas as pd
from .report_generator import generate_report

class Analyzer:
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)

    def analyze(self):
        analysis = []
        for index, row in self.data.iterrows():
            result = {}
            hb = row.get("Hemoglobin", 0)
            plt = row.get("Platelets", 0)
            wbc = row.get("WBC", 0)

            result["Hemoglobin"] = f"{hb} g/dL"
            result["Platelets"] = f"{plt} /μL"
            result["WBC"] = f"{wbc} /μL"

            if hb < 12:
                result["Diagnosis"] = "Possible Anemia"
            elif wbc > 11:
                result["Diagnosis"] = "Leukocytosis"
            else:
                result["Diagnosis"] = "Normal"

            analysis.append(result)
        return analysis

    def generate_report(self, output_path="report.txt"):
        analysis = self.analyze()
        generate_report(analysis, output_path)
