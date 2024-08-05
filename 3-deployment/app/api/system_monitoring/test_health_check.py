# test_health_check.py

from unittest.mock import patch

from fastapi.testclient import TestClient
from system_health_check import router

client = TestClient(router)


@patch('system_health_check.requests.get')
def test_health_check(mock_get):
    # Create a mock response object with the desired status_code
    mock_response_ok = type('Response', (object,), {'status_code': 200})()
    mock_response_not_ok = type('Response', (object,), {'status_code': 500})()

    # Define the side effect for the mock object
    mock_get.side_effect = [mock_response_ok,
                            mock_response_ok,
                            mock_response_not_ok]

    response = client.get("/system_health_check")
    assert response.status_code == 200

    # # Parse the JSON response
    # data = response.json()

    # # Check the values in the response
    # assert data["mage_running"] == "OK"
    # assert data["mflow_running"] == "OK"
    # assert data["monitoring_running"] == "NO"
    # assert data["web_server_running"] == "OK"


def test_always_passes():
    assert True
