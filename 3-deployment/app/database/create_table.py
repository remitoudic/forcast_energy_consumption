import psycopg2

# from dotenv import load_dotenv
# import os


def create_table_energy_data():
    # # Load environment variables
    # load_dotenv("../../../.env.dev")

    # Access environment variables as if they came from the actual environment
    # POSTGRES_USER = os.getenv('POSTGRES_USER')
    # # Database connection parameters
    # POSTGRES_USER =   os.getenv('POSTGRES_USER')
    # POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    # POSTGRES_DB = os.getenv('POSTGRES_DB')
    # POSTGRES_PORT = "5432"  # to no conflict with local db running on  5432
    # # host = "http://172.17.0.1:5432"
    # POSTGRES_HOST="postgres"

    DATABASE_URL = "postgresql://postgres:postgres@postgres:5432/mlops_project"

    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()

        # Example query to create a table
        create_table_command = """
        CREATE TABLE IF NOT EXISTS energy_data (
            date DATE NOT NULL,
            MWH INTEGER NOT NULL
        );
        """
        cur.execute(create_table_command)
        conn.commit()
        print("Table created successfully.")
        # Close the cursor and connection
        cur.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
