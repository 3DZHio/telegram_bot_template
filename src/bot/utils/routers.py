from aiogram import Router

from src.bot.utils import filters

# MESSAGES
start_msg = Router()

# CALLBACKS


# INLINES


# ERRORS


# EXTRA
# Admin
admin = Router()
admin.message.filter(filters.IsAdmin())
