import requests
from fastapi import APIRouter
from requests.exceptions import RequestException

router = APIRouter()


def check_service(url: str) -> str:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "OK"
        else:
            return f"FAIL (Status code: {response.status_code})"
    except RequestException as e:
        return f"FAIL (Exception: {str(e)})"


@router.get("/system_health_check")
def health_check():
    # Define the service URLs
    services = {
        "mage_running": "http://172.17.0.1:6789",
        "mflow_running": "http://172.17.0.1:5000",
        # "monitoring_running": "http://172.17.0.1:7777",
    }

    # Check the status of each service
    report = {service: check_service(url) for service, url in services.items()}
    report["web_server_running"] = "OK"  # Assuming the web server is running

    return {"system health check": report}
