from telethon import TelegramClient, events
import modullar.client
import os
import time
client = modullar.client.client

@events.register(events.NewMessage(outgoing=True, pattern='\.alive'))
async def alive(noob_py):
		client = noob_py.client
		me = await client.get_me()
		username = me.username
		darknet7719 = await client.download_profile_photo(username)
		await client.edit_message(noob_py.message, "Hayrli kun...")
		time.sleep(0.5)
		await noob_py.respond("""🥷 **Foydalanuvchi**: @{}

🥷 **Versia**: 1.0.1.3
├╴╴╴╴╴╴╴╴╴╴
└ 🧟‍♀️ **Jojo Userbot**: @jojo_userbot

 👾 **2021yil 10oy 19kun dasturlangan**
 👾 **ajdodi**: magicbot-uz
 👾 **Dasturchi**: @red_uzbek

🥷 OʻRNATISH 
├╴╴╴╴╴╴╴╴╴╴
├ 👾 https://telegra.ph/JOJO--USERBOT---ORNATISH-BOYICHA-QO%CA%BBLLANMA-10-02
└ 👾 https://telegra.ph/AFK-VA-BLOCK-MODULLARIDAN-FOYDALANISH-BO%CA%BBYICHA-QO%CA%BBLLANMA-10-06""".format(username, ' '), file=darknet7719)
		await noob_py.message.delete()
		os.remove(darknet7719)