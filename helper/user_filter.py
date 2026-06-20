from pyrogram import filters
from config import Config
from helper.database import db

async def admin_check(_, __, message):
    if not message.from_user:
        return False
    
    # Check if bot is in public mode via Env or DB
    if Config.IS_PUBLIC:
        return True
        
    is_public = await db.get_config('is_public', False)
    if is_public:
        return True
        
    if message.from_user.id in Config.ADMIN:
        return True

    db_admins = await db.get_db_admins()
    return message.from_user.id in db_admins

admin_only = filters.create(admin_check)
