from fastapi import APIRouter
import requests

router = APIRouter()


@router.post("/mage_trigger_etl")
def health_check():
    # use docker's default docker0 bridge address ip
    # find  endpoint setting  in Mage : http://localhost:6789/pipelines/mlops_project/triggers/2 
    # adjust to  the proper network adress
    mage_request = requests.post("http://172.17.0.1:6789/api/pipeline_schedules/2/pipeline_runs/6fb0b6ed082946f8a8128bf93d7bb828")
    mage_request.status_code
    return {"status_code": mage_request.status_code}