# main.py
import argparse
import logging
from ydata_profiling import ProfileReport
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_profile(csv_path):
    df = pd.read_csv(csv_path)
    profile = ProfileReport(df, title="Mushroom Profiling")
    profile.to_file("mushroom_profile.html")
    logger.info("Profile generated as mushroom_profile.html")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["profile"], help="Command to run")
    parser.add_argument("csv_filename", help="Path to CSV file")
    args = parser.parse_args()
    
    if args.command == "profile":
        generate_profile(args.csv_filename)