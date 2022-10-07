from telethon import TelegramClient, events
import modullar.client
from modullar.lovely import Lovely
import time
lovely = Lovely()
client = modullar.client.client
@events.register(events.NewMessage)
async def lovelyhandler(event):
		if '.lovely' in event.raw_text:
			time.sleep(0.3)
			for d in lovely.lovely:
				time.sleep(0.3)
				await event.edit(d)