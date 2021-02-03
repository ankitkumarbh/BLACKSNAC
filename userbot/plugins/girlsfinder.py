#       Creadit Goes To @Royal_Boy_45 Pro bOy 
#       real girls finder plugins Not Fake
#       Not Adults Plugin 

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern="cfind?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    
    reply_message = await event.get_reply_message()
    chat = "@date4ubot"
    await event.edit("Finding...")
    async with event.client.conversation(chat) as conv:
          try:     
              response =conv.wait_event(events.NewMessage(incoming=True,from_users=1258724344))
              await event.client.send_message(chat, "Next")
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Boss! Please Unblock @date4ubot ")
              return
          if response.text.startswith(" "):
             await event.edit("Sorry sir, That @date4ubot is dead now")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
   
#           Madharchod Kang mat Ker Na Bosdike Randi ki aulad 
#           Jo Kang Kiya uski ma ko undertaker chode ganad Chala Jayega ga Teri ma Ka

#  Made by
#  Shivansh Rajput
#  @Royal_Boy_45 , @Royal_king7
