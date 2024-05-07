from aiogram import Bot
from aiogram.types import BotCommandScopeAllPrivateChats, BotCommand

from src.bot.texts.inner import bot_commands


async def set_commands(bot: Bot) -> None:
    await bot.set_my_commands(commands=[
        BotCommand(command=command, description=description)
        for command, description in bot_commands.items()
    ], scope=BotCommandScopeAllPrivateChats())
