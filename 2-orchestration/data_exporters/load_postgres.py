from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from pandas import DataFrame
from os import path
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_postgres(data: DataFrame, **kwargs) -> None:
  
        # Get database connection parameters from environment variables
        POSTGRES_USER = os.getenv('POSTGRES_USER', "postgres")
        POSTGRES_PASSWORD =   os.getenv('POSTGRES_PASSWORD', "postgres")
        POSTGRES_DB = os.getenv('POSTGRES_DB',"mlops_project")
        POSTGRES_HOST =  os.getenv('POSTGRES_HOST', 'postgres')
        POSTGRES_PORT =  os.getenv('POSTGRES_PORT', '5432')

        # Create the database connection URL
        DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

        # Create a SQLAlchemy engine
        engine = create_engine(DATABASE_URL)

        try:
            data.to_sql('energy_data', engine, if_exists='replace', index=False)
            # if_exists='replace' => avodid bugg during dev.... to change 
            return "DataFrame exported successfully to PostgreSQL."
        except Exception as e:
            return f"An error occurred: {e}"



