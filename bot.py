import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

from datetime import datetime
from pytz import timezone
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from helper.cleanup import cleanup_old_files
import os

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=min(32, os.cpu_count() + 4),
            plugins={"root": "plugins"},
            sleep_threshold=15,
            max_concurrent_transmissions=Config.MAX_CONCURRENT_TRANSMISSIONS,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username  
        self.uptime = Config.BOT_UPTIME     
        print(f"\033[1;96m @{me.username} Sᴛᴀʀᴛᴇᴅ......⚡️⚡️⚡️\033[0m")


Bot().run()
