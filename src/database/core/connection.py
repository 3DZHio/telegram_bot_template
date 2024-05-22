from psycopg_pool import AsyncConnectionPool
from pydantic import PostgresDsn

from src.config import settings

DSN: PostgresDsn = (
    "postgresql"
    f"://{settings.USER.get_secret_value()}"
    f":{settings.PASSWORD.get_secret_value()}"
    f"@{settings.HOST.get_secret_value()}"
    f":{settings.PORT.get_secret_value()}"
    f"/{settings.DATABASE.get_secret_value()}"
)  # Connection String

pool = AsyncConnectionPool(conninfo=DSN, open=False)
