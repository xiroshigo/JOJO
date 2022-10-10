from html_telegraph_poster.upload_image import upload_image
from telethon import TelegramClient, events, sync
import modullar.client
client = modullar.client.client

@events.register(events.NewMessage(pattern=".tgraph", outgoing=True))
async def tgraph(event):
	await event.edit("yuklanmoqda")
	red_uzbek = await event.get_reply_message()
	msgl = event.to_id
	try:
		nethunter_bro = await red_uzbek.download_media()
		up = upload_image(nethunter_bro)
	except:
		return await event.edit("nimadir hato...")
	await event.client.send_message(msgl, up)
	remove(nethunter_bro)