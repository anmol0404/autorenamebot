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

import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from helper.database import db
from config import Config, Txt  
from helper.user_filter import admin_only
  

@Client.on_message(filters.private & filters.command("help"))
async def help_command(client, message):
    user = message.from_user
    is_admin = user.id in Config.ADMIN
    if not is_admin:
        db_admins = await db.get_db_admins()
        is_admin = user.id in db_admins
    if is_admin:
        await message.reply_text(Txt.HELP_TXT, disable_web_page_preview=True)
    else:
        user_help = """
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
"""
        await message.reply_text(user_help, disable_web_page_preview=True)


@Client.on_message(filters.private & admin_only & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message)                
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton("👨‍💻 Dᴇᴠꜱ 👨‍💻", callback_data='dev')
        ],[
        InlineKeyboardButton('📯 Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/PYRO_BOTZ'),
        InlineKeyboardButton('💁‍♂️ Sᴜᴩᴩᴏʀᴛ', url='https://t.me/PYRO_BOTZ_CHAT')
        ],[
        InlineKeyboardButton('🎛️ Aʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('🛠️ Hᴇʟᴩ', callback_data='help')
    ]])
    if Config.START_PIC:
        await message.reply_photo(Config.START_PIC, caption=Txt.START_TXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Txt.START_TXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)
   

@Client.on_callback_query(admin_only)
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton("👨‍💻 Dᴇᴠꜱ 👨‍💻", callback_data='dev')
                ],[
                InlineKeyboardButton('📯 Uᴩᴅᴀᴛᴇꜱ', url='https://t.me/PYRO_BOTZ'),
                InlineKeyboardButton('💁‍♂️ Sᴜᴩᴩᴏʀᴛ', url='https://t.me/PYRO_BOTZ_CHAT')
                ],[
                InlineKeyboardButton('🎛️ Aʙᴏᴜᴛ', callback_data='about'),
                InlineKeyboardButton('🛠️ Hᴇʟᴩ', callback_data='help')
            ]])
        )
    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("❣️ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
                ],[
                InlineKeyboardButton("❤️‍🔥 Hᴏᴡ Tᴏ Uꜱᴇ❤️‍🔥", url='https://youtu.be/4ZfvMSDXBVg')
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
            ]])            
        )
    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("❣️ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
                ],[
                InlineKeyboardButton("🖥️ Hᴏᴡ Tᴏ Mᴀᴋᴇ", url="https://youtu.be/GfulqsSnTv4")
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
            ]])            
        )
    elif data == "dev":
        await query.message.edit_text(
            text=Txt.DEV_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("❣️ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
                ],[
                InlineKeyboardButton("🖥️ Hᴏᴡ Tᴏ Mᴀᴋᴇ", url="https://youtu.be/GfulqsSnTv4")
                ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
            ]])          
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()




