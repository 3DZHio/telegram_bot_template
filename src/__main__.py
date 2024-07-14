from asyncio import run
from contextlib import suppress

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from src.bot.handlers import get_routers
from src.bot.misc import bot_commands
from src.config import settings
from src.database.core.connection import pool
from src.logs import setup_logger


async def main() -> None:
    bot = Bot(
        token=settings.BOT_TOKEN.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )  # Initializing Bot
    storage = MemoryStorage()  # Create Storage
    dp = Dispatcher(storage=storage)  # Launch Dispatcher

    setup_logger("INFO", ["aiogram.bot.api"])  # Logging
    dp.include_routers(*get_routers())  # Routers | Handlers

    await bot_commands.set_commands(bot)  # Bot Commands

    try:
        await pool.open()  # Open Connection Pool
        await dp.start_polling(
            bot, allowed_updates=dp.resolve_used_update_types()
        )  # Start Polling
    finally:
        await bot.session.close()  # Close Bot Session
        await dp.storage.close()  # Close Storage
        await pool.close()  # Close Connection Pool


if __name__ == "__main__":  # Entry Point
    with suppress(
        KeyboardInterrupt, SystemExit
    ):  # Suppress KeyboardInterrupt and SystemExit Exceptions
        run(main())  # Launch Code
