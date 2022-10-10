
from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
import datetime
import modullar.client
client = modullar.client.client

@events.register(events.NewMessage(outgoing=True))
async def clock(event):
	    if ".clock" in event.raw_text:
		    while True:
		        client = event.client
		        me = await client.get_me()
		        username = me.username
		        #nick = input("nickname yozing soat uchun: ")
		        time = datetime.datetime.today().strftime("{} | %H:%M".format(username))
		        async with client:
		            await client(UpdateProfileRequest(first_name=time))
		            await asyncio.sleep(60)
#asyncio.get_event_loop().run_until_complete(clock())
#client.start()
#client.run_until_disconnected()