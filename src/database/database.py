import psycopg2
import sys 

from src.core.config import settings

def connect():
    """
    Connect to database and return connection
    """
    print("Connecting to PostgreSQL Database...")
    try:
        conn = psycopg2.connect(
                host = settings.POSTGRES_HOST,
                dbname = settings.POSTGRES_DB,
                user = settings.POSTGRES_USER,
                password = settings.POSTGRES_PASSWORD,
                port = settings.POSTGRES_PORT
            )
    except psycopg2.OperationalError as e:
        print(f"Could not connect to Database: {e}")
        sys.exit(1)

    return conn
