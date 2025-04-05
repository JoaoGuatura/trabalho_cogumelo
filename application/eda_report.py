import pandas as pd
import sweetviz as sv
import os

class GenerateEDAReportUseCase:
    def generate_report(self, file_name):
        print(f"📊 Carregando {file_name}...")

        file_path = os.path.join("data", file_name)

        df = pd.read_csv(file_path)

        report = sv.analyze(df)

        report_file = os.path.join("reports", "sweetviz_report.html")

        os.makedirs("reports", exist_ok=True)

        report.show_html(report_file)

        print(f"📄 Relatório gerado: {report_file}")
