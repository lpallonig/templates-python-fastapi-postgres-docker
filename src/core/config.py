class Settings:
    PROJECT_NAME:str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    # pode utilizar dotenv para guardar as informações em um .env
    POSTGRES_USER : str = "root"
    POSTGRES_PASSWORD = 1234
    POSTGRES_HOST : str = "localhost"
    POSTGRES_PORT : str = 5432
    POSTGRES_DB : str = "postgres"
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()