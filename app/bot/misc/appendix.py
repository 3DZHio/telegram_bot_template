from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext


async def delete_message_data(
    message_names: str | list,
    chat_id: int,
    state: FSMContext,
    bot: Bot,
    markup: bool = False,
) -> None:
    if isinstance(message_names, str):
        message_names = [message_names]
    try:
        for message_name in message_names:
            message_id = (await state.get_data()).get(message_name)
            if message_id:
                if markup:
                    await bot.edit_message_reply_markup(
                        chat_id=chat_id, message_id=message_id
                    )
                else:
                    await bot.delete_message(chat_id=chat_id, message_id=message_id)
                await state.update_data({message_name: None})
    except TelegramBadRequest:
        pass
