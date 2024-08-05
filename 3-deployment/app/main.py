from app.api.forcast import endpoints
from app.api.pipelines_triggers import endpoints_mage
from app.api.system_monitoring import system_health_check
from app.database import endpoints_db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Forcast Energy Comsumption",
    description= "Mlop course project"
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(endpoints.router)
app.include_router(system_health_check.router)
app.include_router(endpoints_db.router)
app.include_router(endpoints_mage.router)
