from psycopg_pool import AsyncConnectionPool

from app.config import settings

pool = AsyncConnectionPool(
	conninfo=(
		"postgresql"
		f"://{settings.DB_USER.get_secret_value()}"
		f":{settings.DB_PASSWORD.get_secret_value()}"
		f"@{settings.DB_HOST.get_secret_value()}"
		f":{settings.DB_PORT.get_secret_value()}"
		f"/{settings.DB_NAME.get_secret_value()}"
	),
	open=False,
)
