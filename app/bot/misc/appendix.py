from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext


async def delete_message_data(
    message_names: str | list,
    chat_id: int | str,
    state: FSMContext,
    bot: Bot,
    keyboard: bool = False,
) -> None:
    message_names = [message_names] if isinstance(message_names, str) else message_names
    for message_name in message_names:
        message_id = (await state.get_data()).get(message_name)
        if message_id:
            try:
                await (
                    bot.edit_message_reply_markup(
                        chat_id=chat_id, message_id=message_id
                    )
                    if keyboard
                    else bot.delete_message(chat_id=chat_id, message_id=message_id)
                )
            except TelegramBadRequest:
                pass
            await state.update_data({message_name: None})
