from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from helper.utils_caption import process_caption, clean_name
from config import Config

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

from helper.utils import progress_for_pyrogram, convert, humanbytes
from helper.database import db

from asyncio import sleep
from PIL import Image
import os, time


@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_handler(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name  
    user_id = message.from_user.id

    if file.file_size > 2000 * 1024 * 1024:
        return await message.reply_text("Sᴏʀʀy Bʀᴏ Tʜɪꜱ Bᴏᴛ Iꜱ Dᴏᴇꜱɴ'ᴛ Sᴜᴩᴩᴏʀᴛ Uᴩʟᴏᴀᴅɪɴɢ Fɪʟᴇꜱ Bɪɢɢᴇʀ Tʜᴀɴ 2Gʙ")

    # Clean the filename automatically
    if "." in filename:
        name_part, extn = filename.rsplit('.', 1)
        new_name = clean_name(name_part) + "." + extn
    else:
        new_name = clean_name(filename) + ".mkv"

    sts = await message.reply("Tʀyɪɴɢ Tᴏ Dᴏᴡɴʟᴏᴀᴅɪɴɢ....")
    file_path = f"downloads/{user_id}{time.time()}/{new_name}"
    
    try:
        path = await message.download(file_name=file_path, progress=progress_for_pyrogram, progress_args=("Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....", sts, time.time()))                    
    except Exception as e:
        return await sts.edit(e)

    duration = 0
    try:
        metadata = extractMetadata(createParser(file_path))
        if metadata.has("duration"): 
            duration = metadata.get('duration').seconds
    except:
        pass
    
    ph_path = None
    db_caption = await db.get_caption(user_id)
    db_thumb = await db.get_thumbnail(user_id)
    db_join_channel = await db.get_join_channel(user_id)
    upload_mode = await db.get_upload_mode(user_id)
    join_channel = db_join_channel if db_join_channel else Config.JOIN_CHANNEL

    if db_caption:
        try:
            caption = db_caption.format(filename=new_name, filesize=humanbytes(file.file_size), duration=convert(duration))
        except KeyError:
            caption = process_caption(new_name, join_channel)
    else:
        caption = process_caption(new_name, join_channel)
 
    if (file.thumbs or db_thumb):
        if db_thumb:
            ph_path = await client.download_media(db_thumb) 
        else:
            ph_path = await client.download_media(file.thumbs[0].file_id)
        Image.open(ph_path).convert("RGB").save(ph_path)
        img = Image.open(ph_path)
        img.resize((320, 320))
        img.save(ph_path, "JPEG")

    await sts.edit("Tʀyɪɴɢ Tᴏ Uᴩʟᴏᴀᴅɪɴɢ....")
    try:
        if upload_mode == "document":
            await sts.reply_document(
                document=file_path,
                thumb=ph_path, 
                caption=caption, 
                progress=progress_for_pyrogram,
                progress_args=("Uᴩʟᴏᴅ Sᴛᴀʀᴛᴇᴅ....", sts, time.time())
            )
        elif upload_mode == "video": 
            await sts.reply_video(
                video=file_path,
                caption=caption,
                thumb=ph_path,
                duration=duration,
                progress=progress_for_pyrogram,
                progress_args=("Uᴩʟᴏᴅ Sᴛᴀʀᴛᴇᴅ....", sts, time.time())
            )
    except Exception as e:          
        try: 
            os.remove(file_path)
            if ph_path: os.remove(ph_path)
            return await sts.edit(f" Eʀʀᴏʀ {e}")
        except: pass
        
    try: 
        os.remove(file_path)
        if ph_path: os.remove(ph_path)
        await sts.delete()
    except: pass
