from asyncpg import create_pool

from app.config import DATABASE_DSN


async def fetchone(query: str, *params) -> dict:
    """FetchOne"""
    async with create_pool(dsn=DATABASE_DSN) as pool:
        async with pool.acquire() as connection:
            return await connection.fetchrow(query, *params)


async def fetchall(query: str, *params) -> list[dict]:
    """FetchAll"""
    async with create_pool(dsn=DATABASE_DSN) as pool:
        async with pool.acquire() as connection:
            return await connection.fetch(query, *params)


async def transaction(query: str, *params) -> None:
    """Transaction"""
    async with create_pool(dsn=DATABASE_DSN) as pool:
        async with pool.acquire() as connection:
            async with connection.transaction():
                await connection.execute(query, *params)
