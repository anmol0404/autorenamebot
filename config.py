"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","pyro-botz")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin.strip()) for admin in re.split(r'[, ]+', os.environ.get('ADMIN', '')) if admin.strip().replace('-', '').isdigit()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    JOIN_CHANNEL = os.environ.get("JOIN_CHANNEL", "")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
    MAX_CONCURRENT_TRANSMISSIONS = int(os.environ.get("MAX_CONCURRENT_TRANSMISSIONS", "2")) # Set the maximum amount of concurrent transmissions (uploads & downloads).
    
    # wes response configuration     
    WEB_SUPPORT = bool(os.environ.get("WEB_SUPPORT", "True"))
    IS_PUBLIC = bool(os.environ.get("IS_PUBLIC", "False").lower() == "true")



class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hᴀɪ {} 👋,
Tʜɪs Is Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ
Usɪɴɢ Tʜɪs Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ & Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oꜰ Yᴏᴜʀ Fɪʟᴇ
Yᴏᴜ Cᴀɴ Aʟsᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ & Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ
Tʜɪs Bᴏᴛ Aʟꜱᴏ Sᴜᴘᴘᴏʀᴛs Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ
Mᴏᴅɪꜰɪᴇᴅ Bʏ : <a href='https://t.me/eywwi'>Aɴᴍᴏʟ</a> 💞</b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : {}
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/PYRO_BOTZ/53>𝗧𝗘𝗔𝗠 𝗣𝗬𝗥𝗢 𝗕𝗢𝗧𝗭</a> 
├👨‍💻 Mᴏᴅᴅᴇʀ : <a href=https://t.me/eywwi>Aɴᴍᴏʟ</a>
├📕 Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├📊 Bᴜɪʟᴅ Vᴇʀꜱɪᴏɴ: <a href=https://github.com/anmol0404/autorenamebot>Pyʀᴏ Rᴇɴᴀᴍᴇʀ V4.0.0</a></b>     
╰───────────────⍟ """

    HELP_TXT = """
🌌 <b><u>Usᴇʀ Cᴏᴍᴍᴀɴᴅꜱ</u></b>

<b>• /start</b> - Start the bot
<b>• /help</b> - Show all commands
<b>• /set_caption</b> - Set custom caption
<b>• /see_caption</b> - View your caption
<b>• /del_caption</b> - Delete caption
<b>• /del_thumb</b> - Delete your thumbnail
<b>• /view_thumb</b> - View your thumbnail

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ</u></b>
Send any file & type new file name.

━━━━━━━━━━━━━━━━━━━━━━
👑 <b><u>Adᴍɪɴ Cᴏᴍᴍᴀɴᴅꜱ</u></b>

<b>• /stats</b> - Bot status & stats
<b>• /restart</b> - Restart the bot
<b>• /update</b> - Update from GitHub
<b>• /broadcast</b> - Broadcast (reply to a msg)
<b>• /addadmin</b> - Promote user to admin
<b>• /removeadmin</b> - Demote admin
<b>• /admins</b> - List all admins
<b>• /toggle_public</b> - Toggle public mode
"""

#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @ᴩyʀᴏ_ʙᴏᴛᴢ🙏🥲
    DEV_TXT = """<b><u>Sᴩᴇᴄɪᴀʟ Tʜᴀɴᴋꜱ & Dᴇᴠᴇʟᴏᴩᴇʀꜱ</b></u>
» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : <a href=https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT>𝐏𝐘𝐑𝐎 𝐑𝐄𝐍𝐀𝐌𝐄 𝐁𝐎𝐓</a>
» Mᴏᴅɪꜰɪᴇᴅ Bʏ : <a href=https://t.me/eywwi>Aɴᴍᴏʟ</a>
• ❣️ <a href=https://github.com/lntechnical2>𝗟𝗡 𝗧𝗘𝗖𝗛𝗡𝗜𝗖</a>
• ❣️ <a href=https://t.me/Mhd_ rzn>𝗠𝗵𝗱_𝗿𝘇𝗻</a>
• ❣️ <a href=https://youtu.be/GfulqsSnTv4>𝗠𝗼𝗧𝗲𝗰𝗵 𝗬𝗧</a>
• ❣️ <a href=https://t.me/mr_MKN>𝗠𝗿.𝗠𝗞𝗡 𝗧𝗚</a>
• ❣️ <a href=https://t.me/GitHub_noob>𝗚𝗶𝘁𝗛𝘂𝗯 𝗡𝗢𝗢𝗕</a>
• ❣️ <a href=https://t.me/about_jeol>𝗝𝗲𝗼𝗹 𝗣𝗮𝘂𝗹</a> """

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""
