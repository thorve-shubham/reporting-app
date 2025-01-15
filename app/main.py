import os
import logging
import argparse

from app.PolicyAnalyzer import PolicyAnalyzer
from app.PolicyLoader import PolicyLoader
from app.mappings.broker_mapping import broker_mappings

# Parse command line arguments
parser = argparse.ArgumentParser(description="Set logging level.")
parser.add_argument(
    "--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    help="Set the logging level"
)
args = parser.parse_args()

# Configure logging based on command line argument
logging.basicConfig(level=args.log_level)


loader = PolicyLoader(broker_mappings)

broker_ids = ["1", "2"]  # List of broker IDs
logging.info(f"Available Brokers : {broker_ids}")
all_policies = []

for broker_id in broker_ids:
    logging.info(f"Loading Broker {broker_id} details")
    file_path = os.path.join("app", "data", f"broker{broker_id}.csv")
    policies = loader.load_and_standardize(broker_id, file_path)
    all_policies.extend(policies)  # Add the policies to the all_policies list

analyzer = PolicyAnalyzer()

# Analysis on all policies from brokers
analysis_results = analyzer.analyze(all_policies)
print("\nOverall Report of All Brokers...")
print("=================================")
print("Total Policies:", analysis_results["Total Policies"])
print("Active Policies:", analysis_results["Active Policies"])
print("Total Customers:", analysis_results["Total Customers"])
print("Sum of Insured Amounts:", analysis_results["Sum of Insured Amounts"])
print("Average Policy Duration (days):", analysis_results["Average Policy Duration (days)"])

while True:
    broker_id = input("\nEnter Broker Id ('exit' to Exit): ")

    if broker_id.lower() == 'exit':
        logging.info("Exiting Command Line Reporting Tool...")
        break
    try:
        broker_policies = PolicyAnalyzer.filter_by_broker(all_policies,broker_id)

        for policy in broker_policies:
            print(str(policy))
    except Exception as e:
        logging.error(f"Unexpected Error Occurred : {str(e)}")
        print(str(e))
    

    