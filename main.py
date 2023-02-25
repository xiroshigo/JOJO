from telethon import TelegramClient, events, sync, functions, types
from telethon.errors import rpcbaseerrors
import time
##
from emoji import emojize
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.utils import get_input_location
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio, aiocron, datetime
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, User

#
import random
import time
import os, sys
import asyncio
import random
import wikipedia 
import requests
from collections import deque
from telethon.tl.types import ChannelParticipantsAdmins
import datetime
import os, sys
import time
#modules
from telethon.tl.functions.channels import JoinChannelRequest
import modullar.client, modullar.spam, modullar.emoji, modullar.wiki, modullar.base64, modullar.chatinfo, modullar.ping, modullar.rename, modullar.tagall, modullar.qrc, modullar.count, modullar.nq, modullar.qq, modullar.mq, modullar.rev, modullar.banall, modullar.tuto,  modullar.helpp, modullar.kick, modullar.brainrun, modullar.ahelp, modullar.policerun, modullar.magicrun, modullar.mute, modullar.ccr, modullar.userinfo, modullar.spaminfo, modullar.type, modullar.loading, modullar.afk, modullar.guardan, modullar.iptrace, modullar.tr, modullar.lovestory, modullar.lovelyrun, modullar.alive, modullar.fuckrun, modullar.dinorun, modullar.bombs, modullar.ding, modullar.hypno, modullar.anim, modullar.ascii, modullar.toshbaqa, modullar.figlet, modullar.dumper, modullar.pornhub, modullar.clone, modullar.speedtest, modullar.picer


print("""\033[1;32m
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
""")
#
client = modullar.client.client
#bot
#botClient = modullar.client.botClient

#spam
with client as darknet:
				darknet.add_event_handler(modullar.spam.delayspam)
#emoji
with client as darknet:
				darknet.add_event_handler(modullar.emoji.itachi)
#wiki        
with client as darknet:
				darknet.add_event_handler(modullar.wiki.wiki)
#base64
with client as darknet:
				darknet.add_event_handler(modullar.base64.runb64)
#chatinfo
with client as darknet:
				darknet.add_event_handler(modullar.chatinfo.info)
#ping
with client as darknet:
				darknet.add_event_handler(modullar.ping.pingHandler)
#rename nickname
with client as darknet:
				darknet.add_event_handler(modullar.rename.rename)
#tagall
with client as darknet:
				darknet.add_event_handler(modullar.tagall.tagall)
#qrc
with client as darknet:
				darknet.add_event_handler(modullar.qrc.runqrc)
#count
with client as darknet:
				darknet.add_event_handler(modullar.count.count)
#nq
with client as darknet:
				darknet.add_event_handler(modullar.nq.nq)
#qq
with client as darknet:
				darknet.add_event_handler(modullar.qq.qq)
#mq
with client as darknet:
				darknet.add_event_handler(modullar.mq.mq)
#rev
with client as darknet:
				darknet.add_event_handler(modullar.rev.rev)
#banall
with client as darknet:
				darknet.add_event_handler(modullar.banall.banall)
#tuto
with client as darknet:
				darknet.add_event_handler(modullar.tuto.chatscan)
				#help
with client as darknet:
				darknet.add_event_handler(modullar.helpp.help)
#kick
with client as darknet:
				darknet.add_event_handler(modullar.kick.kick)
#brain
with client as darknet:
				darknet.add_event_handler(modullar.brainrun.brainhandler)
#ahelp
with client as darknet:
				darknet.add_event_handler(modullar.ahelp.ahelp)
#police
with client as darknet:
				darknet.add_event_handler(modullar.policerun.policehandler)
#magic
with client as darknet:
				darknet.add_event_handler(modullar.magicrun.magichandler)
#mute
with client as darknet:
				darknet.add_event_handler(modullar.mute.mute)
#calculatoe
with client as darknet:
				darknet.add_event_handler(modullar.ccr.ccr)
#userinfo
with client as darknet:
				darknet.add_event_handler(modullar.userinfo.userinfo)				
#spaminfo
with client as darknet:
				darknet.add_event_handler(modullar.spaminfo.spaminfos)	
				#type				
with client as darknet:
				darknet.add_event_handler(modullar.type.type)	
#loading
with client as darknet:
				darknet.add_event_handler(modullar.loading.loading)
#afkon
with client as darknet:
				darknet.add_event_handler(modullar.afk.runafkon)
#akfoff
with client as darknet:
				darknet.add_event_handler(modullar.afk.runafkoff)
#afkstatus
with client as darknet:
				darknet.add_event_handler(modullar.afk.runafkstatus)
#runafk
with client as darknet:
				darknet.add_event_handler(modullar.afk.runafk)
#afcmcrun
with client as darknet:
				darknet.add_event_handler(modullar.afk.runmcfafk)
#guardanon
with client as darknet:
				darknet.add_event_handler(modullar.guardan.red)
#guardanoff
with client as darknet:
				darknet.add_event_handler(modullar.guardan.reduz)
#guardanstatus
with client as darknet:
				darknet.add_event_handler(modullar.guardan.reduzb)
#guardanon
with client as darknet:
				darknet.add_event_handler(modullar.guardan.reduzbe)
#guardanon
with client as darknet:
				darknet.add_event_handler(modullar.guardan.reduzbek)
#guardanon
with client as darknet:
				darknet.add_event_handler(modullar.guardan.reduzbek77)
#guardanon
with client as darknet:
				darknet.add_event_handler(modullar.guardan.reduzbek7719)
#iptrace
with client as darknet:
				darknet.add_event_handler(modullar.iptrace.iptrace)
#translate
with client as darknet:
				darknet.add_event_handler(modullar.tr.tr)
with client as darknet:
				darknet.add_event_handler(modullar.lovestory.one)
#tgraph
#with client as darknet:
#				darknet.add_event_handler(modullar.tgraph.tgraph)
with client as darknet:
				darknet.add_event_handler(modullar.lovelyrun.lovelyhandler)
#alive
with client as darknet:
				darknet.add_event_handler(modullar.alive.alive)
#fuck
with client as darknet:
				darknet.add_event_handler(modullar.fuckrun.fuckhandlers)
#dino
with client as darknet:
				darknet.add_event_handler(modullar.dinorun.dinohandlers)
#bombs
with client as darknet:
				darknet.add_event_handler(modullar.bombs.bombs)
#ding
with client as darknet:
				darknet.add_event_handler(modullar.ding.ding)
#hypno
with client as darknet:
				darknet.add_event_handler(modullar.hypno.hypno)
#lul
with client as darknet:
				darknet.add_event_handler(modullar.anim.lul)
#nothappy
with client as darknet:
				darknet.add_event_handler(modullar.anim.nothappy)
#clock
with client as darknet:
				darknet.add_event_handler(modullar.anim.clock)
#muah
with client as darknet:
				darknet.add_event_handler(modullar.anim.muah)				
#heart
with client as darknet:
				darknet.add_event_handler(modullar.anim.heart)
#smoon
with client as darknet:
				darknet.add_event_handler(modullar.anim.smoon)
#tmoon
with client as darknet:
				darknet.add_event_handler(modullar.anim.tmoon)
#dump
with client as darknet:
				darknet.add_event_handler(modullar.anim.snake)
#ascii
with client as darknet:
				darknet.add_event_handler(modullar.ascii.ascii)
#toshbaqa
with client as darknet:
				darknet.add_event_handler(modullar.toshbaqa.toshbaqa)
#figlet
with client as darknet:
				darknet.add_event_handler(modullar.figlet.figlet)
#dumper
with client as darknet:
				darknet.add_event_handler(modullar.dumper.dump)
#pornhub
with client as darknet:
				darknet.add_event_handler(modullar.pornhub.pornhub)
#pname
with client as darknet:
				darknet.add_event_handler(modullar.clone.pbio)
#speedtest
with client as darknet:
	darknet.add_event_handler(modullar.speedtest.wtf)
#picer
with client as darknet:
	darknet.add_event_handler(modullar.picer.picer)


















loop = asyncio.get_event_loop()
client.start()
#botClient.start()
os.system("clear")
print("""\033[1;33m
 ▄▄▄██▀▀▀▒█████   ▄▄▄██▀▀▀▒█████  
   ▒██  ▒██▒  ██▒   ▒██  ▒██▒  ██▒
   ░██  ▒██░  ██▒   ░██  ▒██░  ██▒
▓██▄██▓ ▒██   ██░▓██▄██▓ ▒██   ██░
 ▓███▒  ░ ████▓▒░ ▓███▒  ░ ████▓▒░
 ▒▓▒▒░  ░ ▒░▒░▒░  ▒▓▒▒░  ░ ▒░▒░▒░ 
 ▒ ░▒░    ░ ▒ ▒░  ▒ ░▒░    ░ ▒ ▒░ 
 ░ ░ ░  ░ ░ ░ ▒   ░ ░ ░  ░ ░ ░ ▒  
 ░   ░      ░ ░   ░   ░      ░ ░  
                                  
\033[1;32m
JOJO USERBOT - ISHGA TUSHURILDI

""")
loop.run_forever()


