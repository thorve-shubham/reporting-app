from app.model.Policy import Policy
import pandas as pd
from app.utils import default_values

# Utility Class for loading, normalizing CSV from differnet broker based on their mappings
class PolicyLoader:

    def __init__(self, broker_mappings):
        """
        Initializes the PolicyLoader with mappings for broker column names to standardized names.
        :param broker_mappings: Dictionary mapping broker names to their column mappings.
        """
        self.broker_mappings = broker_mappings

    def load_and_standardize(self, broker_id, file_path):
        """
        Loads and standardizes the policy data for a given broker.
        :param broker_id: ID of the broker.
        :param file_path: Path to the CSV file.
        :return: List of Policy objects.
        """

        try:
            if broker_id not in self.broker_mappings:
                raise ValueError(f"Unknown broker ID: {broker_id}")

            column_mapping = self.broker_mappings[broker_id]

            # Try loading the CSV file and renaming columns
            try:
                df = pd.read_csv(file_path).rename(columns=column_mapping)
            except FileNotFoundError:
                raise FileNotFoundError(f"CSV file not found at path: {file_path}")
            except pd.errors.ParserError:
                raise ValueError(f"Error parsing CSV file at path: {file_path}")
            
            # Fill missing values with default values
            df.fillna(default_values, inplace=True)

            #if columns are not present add them for consistency
            for col, default in default_values.items():
                if col not in df.columns:
                    df[col] = default

            # Create Policy objects
            policies = []
            for _, row in df.iterrows():
                policy = Policy(
                    row["PolicyNumber"], row["InsuredAmount"], row["StartDate"], row["EndDate"], row["AdminFee"],
                    row["BusinessDescription"], row["BusinessEvent"], row["ClientType"], row["ClientRef"], row["Commission"],
                    row["EffectiveDate"], row["InsurerPolicyNumber"], row["IPTAmount"], row["Premium"], row["PolicyFee"],
                    row["PolicyType"], row["Insurer"], row["Product"], row["RenewalDate"], row["RootPolicyRef"], broker_id
                )
                policies.append(policy)
                
            return policies

        except ValueError as ve:
            # Handle any ValueError related to invalid broker ID or CSV parsing
            print(f"ValueError: {ve}")
            raise ValueError(str(ve))
        except FileNotFoundError as fnf:
            # Handle file not found error
            print(f"FileNotFoundError: {fnf}")
            raise FileNotFoundError(str(fnf))
        except Exception as e:
            # Handle any other exceptions
            print(f"An unexpected error occurred: {e}")
            raise Exception(str(e))