from pyrogram import Client, filters 
from config import Config
from helper.database import db
from helper.user_filter import admin_only

@Client.on_message(filters.private & admin_only & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**__Gɪᴠᴇ Tʜᴇ Cᴀᴩᴛɪᴏɴ__\n\nExᴀᴍᴩʟᴇ:- `/set_caption {filename}\n\n💾 Sɪᴢᴇ: {filesize}\n\n⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}`**")
    caption = message.text.split(" ", 1)[1]
    try:
        caption.format(filename='', filesize='', duration='')
    except KeyError as e:
        await message.edit(f"**ᴡʀᴏɴɢ ᴋᴇʏᴡᴏʀᴅ : {e} \nᴛʀʏ ᴀɢᴀɪɴ**")
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("__**✅ Cᴀᴩᴛɪᴏɴ Sᴀᴠᴇᴅ**__")
   
@Client.on_message(filters.private & admin_only & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("__**😔 Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴy Cᴀᴩᴛɪᴏɴ**__")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("__**❌️ Cᴀᴩᴛɪᴏɴ Dᴇʟᴇᴛᴇᴅ**__")
                                       
@Client.on_message(filters.private & admin_only & filters.command(['see_caption', 'view_caption']))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**Yᴏᴜ'ʀᴇ Cᴀᴩᴛɪᴏɴ:-**\n\n`{caption}`")
    else:
       await message.reply_text("__**😔 Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴy Cᴀᴩᴛɪᴏɴ**__")


@Client.on_message(filters.private & admin_only & filters.command(['view_thumb', 'viewthumb']))
async def viewthumb(client, message):    
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(chat_id=message.chat.id, photo=thumb)
    else:
        await message.reply_text("😔 __**Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴy Tʜᴜᴍʙɴᴀɪʟ**__") 
		
@Client.on_message(filters.private & admin_only & filters.command(['del_thumb', 'delthumb']))
async def removethumb(client, message):
    await db.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("❌️ __**Tʜᴜᴍʙɴᴀɪʟ Dᴇʟᴇᴛᴇᴅ**__")
	
@Client.on_message(filters.private & admin_only & filters.photo)
async def addthumbs(client, message):
    mkn = await message.reply_text("Please Wait ...")
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await mkn.edit("✅️ __**Tʜᴜᴍʙɴᴀɪʟ Sᴀᴠᴇᴅ**__")

@Client.on_message(filters.private & admin_only & filters.command('set_join'))
async def add_join_channel(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**__Gɪᴠᴇ Tʜᴇ Cʜᴀɴɴᴇʟ Usᴇʀɴᴀᴍᴇ__\n\nExᴀᴍᴩʟᴇ:- `/set_join @YourChannel`**")
    channel = message.text.split(" ", 1)[1]
    await db.set_join_channel(message.from_user.id, channel=channel)
    await message.reply_text("__**✅ Jᴏɪɴ Cʜᴀɴɴᴇʟ Sᴀᴠᴇᴅ**__")

@Client.on_message(filters.private & admin_only & filters.command('del_join'))
async def delete_join_channel(client, message):
    channel = await db.get_join_channel(message.from_user.id)
    if not channel:
       return await message.reply_text("__**😔 Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴy Jᴏɪɴ Cʜᴀɴɴᴇʟ**__")
    await db.set_join_channel(message.from_user.id, channel=None)
    await message.reply_text("__**❌️ Jᴏɪɴ Cʜᴀɴɴᴇʟ Dᴇʟᴇᴛᴇᴅ**__")

@Client.on_message(filters.private & admin_only & filters.command(['view_join', 'see_join']))
async def see_join_channel(client, message):
    channel = await db.get_join_channel(message.from_user.id)
    if channel:
       await message.reply_text(f"**Yᴏᴜ'ʀᴇ Jᴏɪɴ Cʜᴀɴɴᴇʟ:-**\n\n`{channel}`")
    else:
       await message.reply_text("__**😔 Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴy Jᴏɪɴ Cʜᴀɴɴᴇʟ**__")

@Client.on_message(filters.private & admin_only & filters.command('set_type'))
async def add_type(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**__Gɪᴠᴇ Tʜᴇ Tyᴩᴇ__\n\nExᴀᴍᴩʟᴇ:- `/set_type document` Oʀ `/set_type video`**")
    mode = message.text.split(" ", 1)[1].lower()
    if mode not in ["document", "video"]:
        return await message.reply_text("**❌️ Iɴᴠᴀʟɪᴅ Tyᴩᴇ! Uꜱᴇ `document` Oʀ `video`**")
    await db.set_upload_mode(message.from_user.id, mode=mode)
    await message.reply_text(f"__**✅ Uᴩʟᴏᴀᴅ Tyᴩᴇ Sᴇᴛ Tᴏ {mode.capitalize()}**__")

@Client.on_message(filters.private & admin_only & filters.command(['view_type', 'see_type']))
async def see_type(client, message):
    mode = await db.get_upload_mode(message.from_user.id)
    await message.reply_text(f"**Yᴏᴜ'ʀᴇ Cᴜʀʀᴇɴᴛ Uᴩʟᴏᴀᴅ Tyᴩᴇ:-** `{mode.capitalize()}`")

@Client.on_message(filters.private & admin_only & filters.command('del_type'))
async def delete_type(client, message):
    await db.set_upload_mode(message.from_user.id, mode="document")
    await message.reply_text("__**❌️ Uᴩʟᴏᴀᴅ Tyᴩᴇ Rᴇꜱᴇᴛ Tᴏ Dᴏᴄᴜᴍᴇɴᴛ**__")

@Client.on_message(filters.private & filters.user(Config.ADMIN) & filters.command('public'))
async def toggle_public(client, message):
    if len(message.command) == 1:
        is_public = await db.get_config('is_public', False)
        status = "Enabled" if is_public else "Disabled"
        return await message.reply_text(f"**Cᴜʀʀᴇɴᴛ Pᴜʙʟɪᴄ Mᴏᴅᴇ:** `{status}`\n\nUꜱᴇ `/public on` Oʀ `/public off` Tᴏ Cʜᴀɴɢᴇ.")
    
    mode = message.text.split(" ", 1)[1].lower()
    if mode == "on":
        await db.set_config('is_public', True)
        await message.reply_text("**✅ Pᴜʙʟɪᴄ Mᴏᴅᴇ Eɴᴀʙʟᴇᴅ! Aʟʟ Uꜱᴇʀꜱ Cᴀɴ Nᴏᴡ Uꜱᴇ Tʜᴇ Bᴏᴛ.**")
    elif mode == "off":
        await db.set_config('is_public', False)
        await message.reply_text("**❌ Pᴜʙʟɪᴄ Mᴏᴅᴇ Dɪꜱᴀʙʟᴇᴅ! Oɴʟy Aᴅᴍɪɴꜱ Cᴀɴ Uꜱᴇ Tʜᴇ Bᴏᴛ.**")
    else:
        await message.reply_text("**❌️ Iɴᴠᴀʟɪᴅ Mᴏᴅᴇ! Uꜱᴇ `on` Oʀ `off`**")


