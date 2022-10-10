from telethon import TelegramClient, events
import modullar.client, modullar.dino
from modullar.dino import Dino
import time
dino = Dino()
client = modullar.client.client
@events.register(events.NewMessage)
async def dinohandlers(event):
		for i in range(2):
			
					if '.dino' in event.raw_text:
						time.sleep(0.3)
						for d in dino.dino:
							time.sleep(0.3)
							await event.edit(d)