import math
from readable_number import ReadableNumber

# A Utility class for analyzing, filtering the policies
class PolicyAnalyzer:

    @staticmethod
    def analyze(policies):
        """
        Analyzes the list of policies.
        :param policies: List of Policy objects.
        :return: Dictionary with analysis / aggregate results.
        """
        try:
            if not policies:
                raise ValueError("No policies provided for analysis.")

            active_policies = [p for p in policies if p.is_active()]
            total_policies = len(policies)
            total_customers = len(set(p.client_ref for p in active_policies))
            total_insured_amount = ReadableNumber(str(sum(p.insured_amount for p in active_policies)))

            if len(active_policies) == 0:
                raise ValueError("No active policies available for calculating average duration.")

            avg_policy_duration = sum((p.renewal_date - p.start_date).days for p in active_policies) / len(active_policies)

            return {
                "Total Policies": total_policies,
                "Active Policies" : len(active_policies),
                "Total Customers": total_customers,
                "Sum of Insured Amounts": total_insured_amount,
                "Average Policy Duration (days)": math.floor(avg_policy_duration)
            }

        except ValueError as ve:
            # Handle any ValueError related to missing or invalid data
            print(f"ValueError: {ve}")
            raise ValueError(str(ve))
        except Exception as e:
            # Handle any other exceptions
            print(f"An unexpected error occurred: {e}")
            raise Exception(str(e))

    @staticmethod
    def filter_by_broker(policies, broker_id):
        """
        Filters policies by broker name.
        :param policies: List of Policy objects.
        :param broker_name: Broker name to filter by.
        :return: List of filtered Policy objects.
        """
        try:
            if not policies:
                raise ValueError("No policies provided to filter.")

            filtered_policies = [p for p in policies if p.broker_id == broker_id]

            if not filtered_policies:
                raise ValueError(f"No policies found for broker: {broker_id}")

            return filtered_policies

        except ValueError as ve:
            # Handle any ValueError related to missing or invalid data
            print(f"ValueError: {ve}")
            raise ValueError(str(ve))
        except Exception as e:
            # Handle any other exceptions
            print(f"An unexpected error occurred: {e}")
            raise Exception(str(e))
