from database.core.functions import select, insert
from database.core.methods import fetchone, transaction, fetchall


async def exists(uid: int) -> bool:
    """Check for Existence"""
    return bool(await fetchone(select("1", "users", "uid = $1"), uid))


async def add(uid: int) -> None:
    """Add"""
    await transaction(insert("users", "uid", "$1"), uid)


async def info(uid: int) -> dict:
    """Information"""
    return await fetchone(select("*", "users", "uid = $1"), uid)
