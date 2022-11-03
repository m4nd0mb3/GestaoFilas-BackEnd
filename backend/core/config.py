import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "Sistema de Gestão de Filas"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = """
    O presente projecto é o 'Core' do Sistema de Gestão de Filas que tem como obejectivo agilizar e facilitar o processo de atendimento ao público (público esse composto por estudante) na Secretaria da Universidade Católica de Angola.
    """

    API_V1_STR: str = '/api/v1'

    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","DB_SGF")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()