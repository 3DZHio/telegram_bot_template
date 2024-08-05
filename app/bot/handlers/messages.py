from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.bot.texts import outer
from app.bot.utils import routers
from app.database.models import users


# ADMIN
@routers.admin.message(F.text == outer.get_admin)
async def admin(message: Message) -> None:
	await message.delete()
	await message.answer(text=outer.msg_admin)


# START
@routers.msg.message(CommandStart())
async def start(message: Message) -> None:
	uid = message.from_user.id
	await message.delete()
	if not (await users.exists(uid)):
		await users.add(uid)
	await message.answer(text=outer.msg_start)
