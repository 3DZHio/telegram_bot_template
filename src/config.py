from dotenv import load_dotenv
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    load_dotenv()  # Load .env
    model_config = SettingsConfigDict(case_sensitive=True)  # Model Config

    # PREREQUISITES
    # Bot
    BOT_TOKEN: SecretStr

    # DataBase
    USER: SecretStr
    PASSWORD: SecretStr
    HOST: SecretStr
    PORT: SecretStr
    DATABASE: SecretStr


    # MAIN
    # Admin
    ADMIN_IDS: SecretStr


settings = Settings()
