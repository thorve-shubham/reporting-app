
# These are the mapping for the brokers based on their iDs

broker_mappings = {
    "1": {
        "PolicyNumber": "PolicyNumber", "InsuredAmount": "InsuredAmount", "StartDate": "StartDate",
        "EndDate": "EndDate", "AdminFee": "AdminFee", "BusinessDescription": "BusinessDescription",
        "BusinessEvent": "BusinessEvent", "ClientType": "ClientType", "ClientRef": "ClientRef",
        "Commission": "Commission", "EffectiveDate": "EffectiveDate", "InsurerPolicyNumber": "InsurerPolicyNumber",
        "IPTAmount": "IPTAmount", "Premium": "Premium", "PolicyFee": "PolicyFee", "PolicyType": "PolicyType",
        "Insurer": "Insurer", "Product": "Product", "RenewalDate": "RenewalDate", "RootPolicyRef": "RootPolicyRef"
    },
    "2": {
        "PolicyRef": "PolicyNumber", "CoverageAmount": "InsuredAmount", "InitiationDate": "StartDate",
        "ExpirationDate": "EndDate", "AdminCharges": "AdminFee", "CompanyDescription": "BusinessDescription",
        "ContractEvent": "BusinessEvent", "ConsumerCategory": "ClientType", "ConsumerID": "ClientRef",
        "BrokerFee": "Commission", "ActivationDate": "EffectiveDate", "InsuranceCompanyRef": "InsurerPolicyNumber",
        "TaxAmount": "IPTAmount", "CoverageCost": "Premium", "ContractFee": "PolicyFee",
        "ContractCategory": "PolicyType", "Underwriter": "Insurer", "InsurancePlan": "Product",
        "NextRenewalDate": "RenewalDate", "PrimaryPolicyRef": "RootPolicyRef"
    }
}