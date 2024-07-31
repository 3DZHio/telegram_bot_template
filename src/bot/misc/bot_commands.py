from aiogram import Bot
from aiogram.types import BotCommandScopeAllPrivateChats, BotCommand

# BOT COMMANDS
bot_commands: dict[str, str] = {
    "start": "Start",
}


async def set_commands(bot: Bot) -> None:
    await bot.set_my_commands(
        commands=[
            BotCommand(command=command, description=description)
            for command, description in bot_commands.items()
        ],
        scope=BotCommandScopeAllPrivateChats(),
    )
