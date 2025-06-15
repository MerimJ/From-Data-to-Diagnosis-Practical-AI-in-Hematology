import pandas as pd

class ReportGenerator:
    def __init__(self, analysis_result):
        self.result = analysis_result

    def to_text(self, filename="hematology_report.txt"):
        with open(filename, "w") as f:
            for key, value in self.result.items():
                f.write(f"{key}: {value}\n")
        return filename

    def to_dataframe(self):
        return pd.DataFrame.from_dict(self.result, orient="index", columns=["Value"])

    def to_html(self, filename="hematology_report.html"):
        df = self.to_dataframe()
        df.to_html(filename)
        return filename

    def to_pdf(self, filename="hematology_report.pdf"):
        try:
            import pdfkit
        except ImportError:
            raise ImportError("pdfkit is required for PDF export. Install via pip install pdfkit")

        html_file = self.to_html("temp_report.html")
        pdfkit.from_file(html_file, filename)
        return filename
