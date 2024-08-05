import requests
from fastapi import APIRouter

router = APIRouter()


@router.post("/mage_trigger_etl")
def health_check():
    # use docker's default docker0 bridge address ip
    # find  endpoint setting  in Mage :
    # http://localhost:6789/pipelines/mlops_project/triggers/2
    # adjust to  the proper network adress
    token = "6fb0b6ed082946f8a8128bf93d7bb828"
    url_base = "http://172.17.0.1:6789"
    mage_request = requests.post(
        f"{url_base}/api/pipeline_schedules/2/pipeline_runs/{token}"
    )
    mage_request.status_code
    return {"status_code": mage_request.status_code}
