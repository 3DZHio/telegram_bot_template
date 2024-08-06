from pydantic import SecretStr
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


class Settings(BaseSettings, case_sensitive=True):
    load_dotenv()

    # PREREQUISITES
    # Bot
    BOT_TOKEN: SecretStr

    # DataBase
    DB_USER: SecretStr
    DB_PASSWORD: SecretStr
    DB_HOST: SecretStr
    DB_PORT: SecretStr
    DB_NAME: SecretStr

    # Storage
    STG_HOST: SecretStr
    STG_PORT: SecretStr
    STG_NAME: SecretStr

    # MAIN
    # Logging
    LOG_LEVEL: int

    # Admin
    ADMIN_IDS: SecretStr


settings = Settings()

STORAGE_DSN = (
    "redis"
    f"://{settings.STG_HOST.get_secret_value()}"
    f":{settings.STG_PORT.get_secret_value()}"
    f"/{settings.STG_NAME.get_secret_value()}"
)

DATABASE_DSN = (
    "postgres"
    f"://{settings.DB_USER.get_secret_value()}"
    f":{settings.DB_PASSWORD.get_secret_value()}"
    f"@{settings.DB_HOST.get_secret_value()}"
    f":{settings.DB_PORT.get_secret_value()}"
    f"/{settings.DB_NAME.get_secret_value()}"
)
