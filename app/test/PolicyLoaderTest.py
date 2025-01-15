import pytest
import pandas as pd
from app.model.Policy import Policy
from app.PolicyLoader import PolicyLoader
from unittest.mock import patch, MagicMock


class TestPolicyLoader:
    """Test suite for the PolicyLoader class."""

    # Sample data for testing
    MOCK_BROKER_MAPPINGS = {
        "1": {
            "PolicyNumber": "PolicyNumber",
            "InsuredAmount": "InsuredAmount",
            "StartDate": "StartDate",
            "EndDate": "EndDate",
            "AdminFee": "AdminFee",
            "BusinessDescription": "BusinessDescription",
            "BusinessEvent": "BusinessEvent",
            "ClientType": "ClientType",
            "ClientRef": "ClientRef",
            "Commission": "Commission",
            "EffectiveDate": "EffectiveDate",
            "InsurerPolicyNumber": "InsurerPolicyNumber",
            "IPTAmount": "IPTAmount",
            "Premium": "Premium",
            "PolicyFee": "PolicyFee",
            "PolicyType": "PolicyType",
            "Insurer": "Insurer",
            "Product": "Product",
            "RenewalDate": "RenewalDate",
            "RootPolicyRef": "RootPolicyRef",
        }
    }

    MOCK_POLICY_DATA = {
        "PolicyNumber": ["P12345"],
        "InsuredAmount": [1000.0],
        "StartDate": ["2023-01-01"],
        "EndDate": ["2024-01-01"],
        "AdminFee": [50.0],
        "BusinessDescription": ["Description"],
        "BusinessEvent": ["Event"],
        "ClientType": ["Type"],
        "ClientRef": ["Ref"],
        "Commission": [10.0],
        "EffectiveDate": ["2023-01-01"],
        "InsurerPolicyNumber": ["IP12345"],
        "IPTAmount": [5.0],
        "Premium": [200.0],
        "PolicyFee": [20.0],
        "PolicyType": ["TypeA"],
        "Insurer": ["InsurerA"],
        "Product": ["ProductA"],
        "RenewalDate": ["2024-12-31"],
        "RootPolicyRef": ["Root12345"],
    }

    @pytest.fixture
    def mock_policy_class(self):
        """Patch the Policy class."""
        with patch("app.model.Policy.Policy", side_effect=MagicMock(spec=Policy)) as mock:
            yield mock

    def test_load_and_standardize_success(self, mock_policy_class):
        """Test successful loading and standardization."""
        loader = PolicyLoader(self.MOCK_BROKER_MAPPINGS)
        file_path = "mock.csv"

        with patch("pandas.read_csv", return_value=pd.DataFrame(self.MOCK_POLICY_DATA)) as mock_read_csv:
            policies = loader.load_and_standardize("1", file_path)

        mock_read_csv.assert_called_once_with(file_path)
        assert len(policies) == 1

    def test_load_and_standardize_unknown_broker(self):
        """Test handling of unknown broker ID."""
        loader = PolicyLoader(self.MOCK_BROKER_MAPPINGS)

        with pytest.raises(ValueError, match="Unknown broker ID: invalid_broker"):
            loader.load_and_standardize("invalid_broker", "mock.csv")

    def test_load_and_standardize_file_not_found(self):
        """Test handling of missing CSV file."""
        loader = PolicyLoader(self.MOCK_BROKER_MAPPINGS)
        file_path = "nonexistent.csv"

        with patch("pandas.read_csv", side_effect=FileNotFoundError):
            with pytest.raises(FileNotFoundError, match=f"CSV file not found at path: {file_path}"):
                loader.load_and_standardize("1", file_path)

