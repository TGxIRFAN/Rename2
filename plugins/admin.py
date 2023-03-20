import re, asyncio, time, shutil, psutil, os, sys
from pyrogram import Client, filters, enums
from pyrogram.types import *
from config import BOT_START_TIME, ADMIN
from utils import humanbytes  


@Client.on_message(filters.private & filters.command("status") & filters.incoming)          
async def stats(bot, update):
    currentTime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - BOT_START_TIME))
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    ms_g = f"""<b><u>Bot Status</b></u>

Uptime: <code>{currentTime}</code>
CPU Usage: <code>{cpu_usage}%</code>
RAM Usage: <code>{ram_usage}%</code>
Total Disk Space: <code>{total}</code>
Used Space: <code>{used} ({disk_usage}%)</code>
Free Space: <code>{free}</code> """

    msg = await bot.send_message(chat_id=update.chat.id, text="__Processing...__", parse_mode=enums.ParseMode.MARKDOWN)         
    await msg.edit_text(text=ms_g, parse_mode=enums.ParseMode.HTML)
    

