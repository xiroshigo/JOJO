from telethon import TelegramClient, events, sync, functions, types, Button

import modullar.client
client = modullar.client.client
botClient = modullar.client.botClient
@botClient.on(events.InlineQuery)
async def _(query):
				if query.text == "ahelp":
								result = query.builder.article('Ahelp', text = """
πͺ Umumiy animatsialar: 23
πͺ Berkitilgan animatsialar: 0

π Police: police. - sirena animatsiasi
π§  Brain: brain. - qovoqmiyya
β€οΈ Magic: magic. - yurklar animatsiasi
π Loading animatsiasi: loading.
π 18+ animatsia: 18+.
β€οΈ Lovely : lovely. - sevishganlar animatsiasi
π Fuck: fuck. animation
π¦ Dino animation: dino.
π ding animatsia: ding.
π£ animatsia bomba: bombs.
π¬ hypno animatsia: hypno.
π€£ kukish animatsiasi: lul.
π nothappy animatsiasi: .nothappy
β° soat animatsiasi: clock.
π muah qnimatsiasi: muah.
β€οΈ yurak animatsiasi: heart.
π oy animatsiasi: smoon.
π oy animatsiasi: tmoon.
π iloncha animatsiasi: snake.
π’ toshbaqa animatsiasi: toshbaqa.
π¬ shirinliklarga qarshimiz: dump.
π€ lucky spin animatsia: spin. <lucky>
βfortnite dance animation: fortnite.

π JOJO | USERBOT

					
								""", buttons= [
								[Button.inline("INFORMATION", data=b"1")],
								[Button.url("Tg channel", url="https://t.me/jojo_userbot")]
								
								])
								await query.answer([result])
@botClient.on(events.CallbackQuery)
async def uzgaruvchi(event):
				
				if event.data==b'1':
								await event.answer("JOJO | USERBOT - 1.0.1.4v \nHavfsiz Userbot\nserverga ulangamagan juda oddiy yuserbot\nhar 4 kun ichida yangilanib turadi\ndasturchi: @red_uzbek\nmaqsad: Insonlarga telegramda oz boΚ»lsa da yordam berish", alert=True)

@events.register(events.NewMessage(pattern=".ahelp"))
async def ahelp(event):
				results = await client.inline_query("@jojo_user_bot", "ahelp")
				await results[0].click(event.chat_id)
				await event.message.delete()
