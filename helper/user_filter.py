from pyrogram import filters
from config import Config

async def admin_check(_, __, message):
    if not message.from_user:
        return False
    
    # Check if bot is in public mode via Env or DB
    if Config.IS_PUBLIC:
        return True
        
    is_public = await db.get_config('is_public', False)
    if is_public:
        return True
        
    return message.from_user.id in Config.ADMIN

admin_only = filters.create(admin_check)
