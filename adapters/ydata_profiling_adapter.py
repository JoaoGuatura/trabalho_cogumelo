import pandas as pd
from ydata_profiling import ProfileReport

class YDataProfilingAdapter:
    def generate_profile(self, data_path, output_file="profile_report.html"):
        """Generate a ydata-profiling report"""
        df = pd.read_csv(data_path)
        profile = ProfileReport(df, title="Mushroom Dataset Profiling")
        profile.to_file(output_file)
        return output_file