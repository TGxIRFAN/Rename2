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


class mr(object):
    PROGRESS_BAR = """\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗂️ : {1} | {2}
┣⪼ ⏳️ : {0}%
┣⪼ 🚀 : {3}/s
┣⪼ ⏱️ : {4}
╰━━━━━━━━━━━━━━━➣ """

    ABOUT_TXT = """
╭───────────⍟
├🤖 𝙼𝚈 𝙽𝙰𝙼𝙴 : {}
├👑 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁𝚂 : <a href=https://t.me/filesharebotusers>𝗔𝗠𝗟 𝗨𝗣𝗗𝗔𝗧𝗘𝗦</a> 
├👨‍💻 𝙿𝚁𝙾𝙶𝚁𝙰𝙼𝙴𝚁 : <a href=https://github.com/lntechnical2>𝙻𝙽 𝚃𝙴𝙲𝙷.𝚐𝚒𝚝</a>
├📕 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 : <a href=https://github.com/pyrogram>𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</a>
├✏️ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : <a href=https://www.python.org>𝙿𝚈𝚃𝙷𝙾𝙽 3</a>
├💾 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴 : <a href=https://cloud.mongodb.com>𝙼𝙾𝙽𝙶𝙾𝙳𝙱</a>
├📊 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚄𝚂 : v2.1.90 [ ꜱɪɢᴍᴀ 🗿 ]              
╰───────────────⍟
                                """
    HELP_TXT = """
🌌 <b><u>𝙷𝙾𝚆 𝚃𝙾 𝚂𝙴𝚃 𝚃𝙷𝚄𝙼𝙱𝙽𝙸𝙻𝙴</u></b>
  
★ /start A Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pɪᴄᴛᴜʀᴇ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
★ /delthumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Aɴᴅ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
★ /viewthumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Vɪᴇᴡ Yᴏᴜ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ

📑 <b><u>𝙷𝙾𝚆 𝚃𝙾 𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝙲𝙰𝙿𝚃𝙸𝙾𝙽</u></b>
★ /set_caption Sᴇᴛ A Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ.
★ /see_caption Sᴇᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
★ /del_caption Dᴇʟᴇᴛᴇ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ

𝙴𝚇𝙰𝙼𝙿𝙻𝙴 :- /set_caption 📕Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration}

📑 𝙷𝙾𝚆 𝚃𝙾 𝚁𝙴𝙽𝙰𝙼𝙴 𝙰 𝙵𝙸𝙻𝙴
★Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Cʟɪᴄᴋ Rᴇɴᴀᴍᴇ \nOᴩᴛɪᴏɴ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nᴀᴍᴇ Aɴᴅ \nSᴇɴᴅ Sᴇʟᴇᴄᴛ [ Dᴏᴄᴜᴍᴇɴᴛ, Vɪᴅᴇᴏ, Aᴜᴅɪᴏ ]
𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/filesharebotusers>𝑺𝑼𝑷𝑷𝑶𝑹𝑻 𝑮𝑹𝑶𝑼𝑷</a>
"""

#⚠️ don't remove our credits 🙏😢😢
    DEV_TXT = """
<b><u>Special Thanks & Developers</b></u> 

» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : <a href=https://t.me/Ak_Links1>𝗔𝗞 𝗕𝗢𝗧𝗭</a>

• ❣️ <a href=https://t.me/V_I_J_A_Y_THALAPATHY1>𝐀𝐒 𝐓𝐆 [𝐎𝐍𝐋𝐈𝐍𝐄]</a>
• ❣️ <a href=https://t.me/Fake_2_me>𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥</a>
• ❣️ <a href=https://t.me/psycho_009>𝐀𝐤 ᠰ 𝐓𝐠 [O𝐅𝐅𝐥𝐢𝐧𝐞 ]</a>
• ❣️ <a href=https://t.me/Lucifer_Tg3>𝐋𝐔𝐂𝐈𝐅𝐄𝐑 [𝐎𝐅𝐅𝐋𝐈𝐍𝐄]</a>
• ❣️ <a href=https://t.me/filesharebotusers>𝗔𝗠𝗟 𝗨𝗣𝗗𝗔𝗧𝗘𝗦</a>
• ❣️ <a href=https://t.me/Ak_Links1>𝗔𝗞 𝗕𝗢𝗧𝗭</a>
"""
