from datetime import datetime, timedelta
import pandas as pd
from readable_number import ReadableNumber

# A standard structure for Policy - this will help standardize the code
class Policy:
    def __init__(self, policy_id, insured_amount, start_date, end_date, admin_fee, business_description,
                 business_event, client_type, client_ref, commission, effective_date, insurer_policy_number,
                 ipt_amount, premium, policy_fee, policy_type, insurer, product, renewal_date, root_policy_ref, broker_id):
        self.policy_id = policy_id
        self.insured_amount = insured_amount or 0
        self.start_date = pd.to_datetime(start_date, errors='coerce', dayfirst=True) if start_date else None
        self.end_date = pd.to_datetime(end_date, errors='coerce', dayfirst=True) if end_date else None
        self.admin_fee = admin_fee or 0
        self.business_description = business_description or "Unknown"
        self.business_event = business_event or "Unknown"
        self.client_type = client_type or "Unknown"
        self.client_ref = client_ref or "Unknown"
        self.commission = commission or 0.0
        self.effective_date = pd.to_datetime(effective_date, errors='coerce', dayfirst=True) if effective_date else None
        self.insurer_policy_number = insurer_policy_number or "Unknown"
        self.ipt_amount = ipt_amount or 0.0
        self.premium = premium or 0.0
        self.policy_fee = policy_fee or 0.0
        self.policy_type = policy_type or "Unknown"
        self.insurer = insurer or "Unknown"
        self.product = product or "Unknown"
        self.renewal_date = pd.to_datetime(renewal_date, errors='coerce', dayfirst=True) if renewal_date else None
        self.root_policy_ref = root_policy_ref or "Unknown"
        self.broker_id = broker_id

    def is_active(self, as_of_date=datetime.today()):
        return self.start_date <= as_of_date <= self.renewal_date
    
    def __str__(self):
        return (f"\nBroker ID: {self.broker_id}"
                f"\n================="
                f"\nActive: {self.is_active()}"
                f"\nPolicy ID: {self.policy_id}, Insured Amount: {ReadableNumber(str(self.insured_amount))}, Start Date: {self.start_date}, "
                f"End Date: {self.end_date}, Admin Fee: {ReadableNumber(str(self.admin_fee))}, Business Description: {self.business_description}, "
                f"Business Event: {self.business_event}, Client Type: {self.client_type}, Client Ref: {self.client_ref}, "
                f"Commission: {ReadableNumber(str(self.commission))}, Effective Date: {self.effective_date}, Insurer Policy Number: {self.insurer_policy_number}, "
                f"IPT Amount: {ReadableNumber(str(self.ipt_amount))}, Premium: {self.premium}, Policy Fee: {ReadableNumber(str(self.policy_fee))}, Policy Type: {self.policy_type}, "
                f"Insurer: {self.insurer}, Product: {self.product}, Renewal Date: {self.renewal_date}, "
                f"Root Policy Ref: {self.root_policy_ref}")