from pyrogram import filters
from config import Config

async def admin_check(_, __, message):
    if not message.from_user:
        return False
    return message.from_user.id in Config.ADMIN

admin_only = filters.create(admin_check)
