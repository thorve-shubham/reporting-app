import pytest
from unittest.mock import MagicMock
from datetime import datetime
from app.PolicyAnalyzer import PolicyAnalyzer
from readable_number import ReadableNumber

# working with only required params by creating own mock policy
@pytest.fixture
def mock_policy():
    """Fixture for creating a mock Policy object."""
    def create_mock_policy(client_ref, insured_amount, start_date, renewal_date, broker_id, active=True):
        mock = MagicMock()
        mock.client_ref = client_ref
        mock.insured_amount = insured_amount
        mock.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        mock.renewal_date = datetime.strptime(renewal_date, "%Y-%m-%d")
        mock.broker_id = broker_id
        mock.is_active.return_value = active
        return mock
    return create_mock_policy


class TestPolicyAnalyzer:

    def test_analyze_success(self, mock_policy):
        """Test the analyze method with valid policies."""
        policies = [
            mock_policy("Client1", 1000.0, "2023-01-01", "2024-01-01", "1"),
            mock_policy("Client2", 2000.0, "2023-02-01", "2024-02-01", "1"),
            mock_policy("Client1", 1500.0, "2023-03-01", "2024-03-01", "1")
        ]
        result = PolicyAnalyzer.analyze(policies)

        assert result["Total Policies"] == 3
        assert result["Active Policies"] == 3
        assert result["Total Customers"] == 2
        assert str(result["Sum of Insured Amounts"]) == str(ReadableNumber("4500.0"))
        assert result["Average Policy Duration (days)"] == 365

    def test_analyze_no_policies(self):
        """Test the analyze method with no policies."""
        with pytest.raises(ValueError, match="No policies provided for analysis."):
            PolicyAnalyzer.analyze([])

    def test_analyze_no_active_policies(self, mock_policy):
        """Test the analyze method with no active policies."""
        policies = [
            mock_policy("Client1", 1000.0, "2023-01-01", "2024-01-01", "1", active=False),
            mock_policy("Client2", 2000.0, "2023-02-01", "2024-02-01", "1", active=False)
        ]
        with pytest.raises(ValueError, match="No active policies available for calculating average duration."):
            PolicyAnalyzer.analyze(policies)

    def test_filter_by_broker_success(self, mock_policy):
        """Test the filter_by_broker method with valid data."""
        policies = [
            mock_policy("Client1", 1000.0, "2023-01-01", "2024-01-01", "1"),
            mock_policy("Client2", 2000.0, "2023-02-01", "2024-02-01", "1"),
            mock_policy("Client3", 1500.0, "2023-03-01", "2024-03-01", "2")
        ]
        result = PolicyAnalyzer.filter_by_broker(policies, "1")
        assert len(result) == 2
        assert all(p.broker_id == "1" for p in result)

    def test_filter_by_broker_no_policies(self):
        """Test the filter_by_broker method with no policies."""
        with pytest.raises(ValueError, match="No policies provided to filter."):
            PolicyAnalyzer.filter_by_broker([], "1")

    def test_filter_by_broker_no_match(self, mock_policy):
        """Test the filter_by_broker method with no matching broker."""
        policies = [
            mock_policy("Client1", 1000.0, "2023-01-01", "2024-01-01", "1"),
            mock_policy("Client2", 2000.0, "2023-02-01", "2024-02-01", "1")
        ]
        with pytest.raises(ValueError, match="No policies found for broker: 2"):
            PolicyAnalyzer.filter_by_broker(policies, "2")
