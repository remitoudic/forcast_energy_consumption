from app.database.create_table import create_table_energy_data
from fastapi import APIRouter

router = APIRouter()


@router.get("/create_database")
def create_table_postgres():
    return create_table_energy_data()
