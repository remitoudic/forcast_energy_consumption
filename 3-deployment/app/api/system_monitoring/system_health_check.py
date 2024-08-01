from fastapi import APIRouter
import requests

router = APIRouter()


@router.get("/system_health_check")
def health_check():
    # use docker's default docker0 bridge address ip
    mage_running = requests.get("http://172.17.0.1:6789")
    mflow_running = requests.get("http://172.17.0.1:5000")
    monitoring_running = requests.get("http://172.17.0.1:7777")

    report = {
        "mage_running": "OK" if mage_running.status_code == 200 else "NO",
        "mflow_running": "OK" if mflow_running.status_code == 200 else "NO",
        "monitoring_running": "OK" if monitoring_running.status_code == 200 else "NO",
        "web_server_running": "OK",
    }

    return {"system health check": report}
