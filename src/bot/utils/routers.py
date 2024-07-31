from aiogram import Router

from src.bot.utils import filters

# MESSAGES
msg = Router()

# CALLBACKS
cb = Router()

# INLINES
inl = Router()

# ERRORS
err = Router()

# EXTRA
# Admin
admin = Router()
admin.message.filter(filters.IsAdmin())
