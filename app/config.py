from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings, case_sensitive=True, env_file="docker/.env"):
	# PREREQUISITES
	# Bot
	BOT_TOKEN: SecretStr
	
	# DataBase
	DB_USER: SecretStr
	DB_PASSWORD: SecretStr
	DB_HOST: SecretStr
	DB_PORT: SecretStr
	DB_NAME: SecretStr
	
	# ReDiS
	RDS_HOST: SecretStr
	RDS_PORT: SecretStr
	RDS_NAME: SecretStr
	
	# MAIN
	# Logging
	LOG_LEVEL: int
	
	# Admin
	ADMIN_IDS: SecretStr


settings = Settings()
