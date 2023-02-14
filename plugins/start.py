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
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

import os, sys
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
import random
from helper.txt import mr
from helper.database import db
from config import START_PIC, FLOOD, ADMIN, LOG_CHANNEL


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)     
        await client.send_message(LOG_CHANNEL, text=f"#NewUser\nName: {user.first_name}\nID: {user.id}")
    txt=f"Hᴀɪ {user.mention} \nIᴀᴍ A Sɪᴍᴩʟᴇ Fɪʟᴇ Rᴇɴᴀᴍᴇ + Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ Cᴏɴᴠᴇʀᴛᴇʀ Bᴏᴛ Wɪᴛʜ Pᴇʀᴍᴀɴᴇɴᴛ Tʜᴜʙɴɪʟᴇ & Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ Sᴜᴩᴩᴏʀᴛ!"
    button=InlineKeyboardMarkup([[
        InlineKeyboardButton("👨‍💻Dᴇᴠꜱ👨‍💻", callback_data='dev')
        ],[
        InlineKeyboardButton('📢Uᴩᴅᴀᴛᴇꜱ📢', url='https://t.me/MLZ_BOTZ'),
        InlineKeyboardButton('🧩Sᴜᴩᴩᴏʀᴛꜱ🧩', url='https://t.me/MLZ_BOTZ_SUPPORT')
        ],[
        InlineKeyboardButton('♻️Aʙᴏᴜᴛ♻️', callback_data='about'),
        InlineKeyboardButton('⚙Hᴇʟᴩ⚙', callback_data='help')
        ]])
    if START_PIC:
        await message.reply_photo(START_PIC, caption=txt, reply_markup=button)       
    else:
        await message.reply_text(text=txt, reply_markup=button, disable_web_page_preview=True)
   

@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 Sᴛᴀʀᴛ Rᴇɴᴀᴍᴇ 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ Cᴀɴᴄᴇʟ ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 Sᴛᴀᴇᴛ Rᴇɴᴀᴍᴇ📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ Cᴀɴᴄᴇʟ ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""Hᴀɪ {query.from_user.mention} \nIᴀᴍ A Sɪᴍᴩʟᴇ Fɪʟᴇ Rᴇɴᴀᴍᴇ + Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ Cᴏɴᴠᴇʀᴛᴇʀ Bᴏᴛ Wɪᴛʜ Pᴇʀᴍᴀɴᴇɴᴛ Tʜᴜʙɴɪʟᴇ & Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ Sᴜᴩᴩᴏʀᴛ!""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("👨‍💻Dᴇᴠꜱ👨‍💻", callback_data='dev')                
                ],[
                InlineKeyboardButton('📢Uᴩᴅᴀᴛᴇꜱ📢', url='https://t.me/Ak_Links1'),
                InlineKeyboardButton('🧩Sᴜᴩᴩᴏʀᴛꜱ🧩', url='https://t.me/filesharebotusers')
                ],[
                InlineKeyboardButton('♻️Aʙᴏᴜᴛ♻️', callback_data='about'),
                InlineKeyboardButton('⚙Hᴇʟᴩ⚙', callback_data='help')
                ]]
                )
            )
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               
               ],[
               
               ],[
               InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
               InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               
               ],[
               
               ],[
               InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
               InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               
               ],[
               
               ],[
               InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
               InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()
            
@Client.on_message(filters.command('restart') & filters.user(ADMIN))
async def bot_restart(bot, message):
    msg = await message.reply("🔄 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...")
    await sleep(3)
    await msg.edit("✅️ 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳! 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴.")
    os.execl(sys.executable, sys.executable, *sys.argv)
            





