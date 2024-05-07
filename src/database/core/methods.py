from psycopg.rows import dict_row

from src.database.core.connection import pool


async def fetchone(query: str, params: tuple = None) -> dict:
    """FetchOne"""
    async with pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cursor:
            await cursor.execute(query, params)
            return await cursor.fetchone()


async def fetchall(query: str, params: tuple = None) -> list[dict]:
    """FetchAll"""
    async with pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cursor:
            await cursor.execute(query, params)
            return await cursor.fetchall()


async def transaction(query: str, params: tuple = None) -> None:
    """Transaction"""
    async with pool.connection() as conn:
        async with conn.transaction():
            await conn.execute(query, params)
