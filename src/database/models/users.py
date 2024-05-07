from src.database.core.functions import select, insert
from src.database.core.methods import fetchone, transaction
from src.database.text import all_columns, any_columns, inset, users, uid_condition


async def exists(uid: int) -> bool:
    """Check for Existence"""
    return bool(await fetchone(select(any_columns, users, uid_condition),
                               (uid,)))


async def add(uid: int) -> None:
    """Add"""
    await transaction(insert(users, "uid", inset),
                      (uid,))


async def info(uid: int) -> dict:
    """Information"""
    return await fetchone(select(all_columns, users, uid_condition),
                          (uid,))
