import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

#####  Work outside of the container ... use a troubleshouting tool 

# Sample DataFrame
year=2020
daily_cons = pd.read_excel(f'https://github.com/remitoudic/mlops/raw/main/project/data%20/consumption/daily_{year}.xls', skiprows=17,  usecols=lambda x: x if not x.startswith('Unnamed') else None)
daily_cons.dropna(inplace=True)
daily_cons.reset_index(inplace=True,drop=True)
daily_cons.drop(['Type de données'],inplace=True, axis=1)
daily_cons.rename(columns={'Energie journalière (MWh)': "MWh"},inplace=True)
daily_cons.rename(columns={'Date': "date"},inplace=True)
daily_cons['date'] = pd.to_datetime(daily_cons['date'], format="%d/%m/%Y", errors='coerce')




df = daily_cons


def create_engine_project():
    # Load environment variables from .env file
    load_dotenv()

    # Get database connection parameters from environment variables
    POSTGRES_USER = os.getenv('POSTGRES_USER', "postgres")
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', "postgres")
    POSTGRES_DB = os.getenv('POSTGRES_DB',"mlops_project")
    POSTGRES_HOST = os.getenv('POSTGRES_HOST', '0.0.0.0')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5430')

    # Create the database connection URL
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # Create a SQLAlchemy engine
    engine = create_engine(DATABASE_URL)
    print( "type:", engine )
    return engine

def exporter_db(data ):
    engine=create_engine_project()
    # Export the DataFrame to PostgreSQL
    try:
        data.to_sql("energy_data", engine, if_exists='append', index=False)
        print("DataFrame exported successfully to PostgreSQL.")
    except Exception as e:
        print(f"An error occurred: {e}")

exporter_db(df)

