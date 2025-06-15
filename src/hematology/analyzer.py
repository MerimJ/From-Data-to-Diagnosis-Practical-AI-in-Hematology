"""
Analyzer module for processing hematology lab data
"""

import pandas as pd

class Analyzer:
    def __init__(self, dataframe):
        self.df = dataframe

    @classmethod
    def load_labs(cls, filepath):
        df = pd.read_csv(filepath)
        return cls(df)

    def analyze(self):
        # Simulated diagnosis logic
        self.analysis = {
            "Diagnosis": "Probable Iron Deficiency Anemia",
            "Confidence": "87%",
            "Comment": "Elevated RDW suggests active erythropoiesis. Recommend Ferritin test."
        }
        return self

    def generate_report(self):
        return Report(self.analysis)


class Report:
    def __init__(self, data):
        self.data = data

    def export(self, format="txt", filename="hematology_report.txt"):
        if format == "txt":
            with open(filename, "w") as f:
                for key, value in self.data.items():
                    f.write(f"{key}: {value}\n")
        else:
            raise ValueError("Unsupported format: Only 'txt' is implemented")
