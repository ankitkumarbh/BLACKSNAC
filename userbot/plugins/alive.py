# Thanks to Sipak bro and Aryan.. 
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_shivansh ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, Lastupdate
from . import dcdef
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "BLACK SNAKE"

# Thanks to Sipak bro and Aryan.. 
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_Shivansh ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for BS(BLACK SNAKE)
global ghanti
ghanti = borg.uid
edit_time = 1
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/53dc7a79cd5f5311f426f.jpg"
""" =======================CONSTANTS====================== """


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
    pm_caption = "** Welcome To Black Snake **\n\n"
    pm_caption += "**Hey!, I'm Alive. All Systems are online and functioning Perfectly!...**\n\n"
    pm_caption += f"🔶 **Telethon Version** : {version.__version__}\n"
    pm_caption += f"🔶 **Telethon Version** : 3.8.3\n"
    pm_caption += "🔶 **Support** : [ᴊᴏɪɴ](https://t.meBLACKSNAK6_support)\n"
    pm_caption += f"🔶 **Database Status** : All OK!\n\n"
    pm_caption += f"🔶 **My pro owner** : [{DEFAULTUSER}](tg://user?id={ghanti})\n"
    pm_caption += "    [✨REPO✨](https://github.com/BLACKSNAC/BLACKSNAC) 🔹 **Snake Uptime** : {uptime}"
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file1) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file1)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    

