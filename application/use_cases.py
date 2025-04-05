class MLUseCases:
    def __init__(self, profiler_adapter):
        self.profiler_adapter = profiler_adapter
    
    def profile_data(self, csv_filename):
        """Generate a profiling report for the dataset"""
        return self.profiler_adapter.generate_profile(csv_filename)