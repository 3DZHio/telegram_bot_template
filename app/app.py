from asyncio import run
from contextlib import suppress

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from bot.handlers import get_routers
from bot.misc.bot_commands import set_commands
from config import settings, STORAGE_DSN
from log import setup_logger


async def main() -> None:
    setup_logger(level=settings.LOG_LEVEL)
    bot = Bot(
        token=settings.BOT_TOKEN.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await set_commands(bot)
    dp = Dispatcher(storage=RedisStorage(redis=Redis.from_url(url=STORAGE_DSN)))
    dp.include_routers(*get_routers())
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await dp.storage.close()


if __name__ == "__main__":
    with suppress(KeyboardInterrupt, SystemExit):
        run(main())
