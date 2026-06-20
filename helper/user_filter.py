from pyrogram import filters
from config import Config
from helper.database import db
import logging

logger = logging.getLogger(__name__)

async def admin_check(_, __, message):
    try:
        if not message.from_user:
            return False
        
        if Config.IS_PUBLIC:
            return True
            
        is_public = await db.get_config('is_public', False)
        if is_public:
            return True
            
        if message.from_user.id in Config.ADMIN:
            return True

        db_admins = await db.get_db_admins()
        return message.from_user.id in db_admins
    except Exception as e:
        logger.error(f"admin_check error: {e}")
        return False

admin_only = filters.create(admin_check)
