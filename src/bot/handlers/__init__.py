from aiogram import Router

from src.bot.handlers import messages, callbacks, inlines, errors


def get_routers() -> list[Router]:
    # MESSAGES
    msg = [
        messages.routers.start_msg,
    ]
    # CALLBACKS
    cb = [

    ]
    # INLINES
    inl = [

    ]
    # ERRORS
    err = [

    ]
    # EXTRA
    extra = [
        messages.routers.admin,
    ]
    return msg + cb + inl + err + extra
