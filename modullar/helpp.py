from telethon import TelegramClient, events, sync, functions, types, Button

import modullar.client
client = modullar.client.client
botClient = modullar.client.botClient
@botClient.on(events.InlineQuery)
async def _(query):
				if query.text == "ppphelp":
								result = query.builder.article('ppphelp', text = """
ð  **Umumiy modullar**: 29
â **Berkitilgan modullar**:  0

ð **Tezlik**: ping.
ð **Birdaniga hammani ban qilish**: banall.
ð **Spamm habar**: spam. <soniya> <takrorlanish> <habar>
ð **Textni emojiga aylantiradi**: emoji. <Text>
ð **Guruh malumotlarini scanerlaydi**: chatinfo.
ð **Chatlaringiz sonini hisoblaydi**: count.
ð **Base64 da shifrlaydi**: b64. <en> <reply>
ð **Base64 shifrdan yechadi**: b64. <de> <reply>
ð **Memli sticker**: mq. <reply>
ð **Text sticker**: qq. <reply>
ð **Text image**: nq. <reply>
ð **Qr code yaratadi**: qrc. <create> <reply>
ð **Textni teskari ogiradi**: rev. <reply>
ð **Guruh azolarini chaqiradi**: tagall. 
ð **Nickname ozgartiradi**: rename. <Nickname>
ð **Wiki qidiruv**: wiki. <qidirish uchun soÊ»z>
ð **Guruhdagi azoni kick qilish uchun**: kick. <reply>
ð **Mute qilish uchun**: mute. <vaqt> <m, h, d>
ð **Calculator**: ccr. <misol>
ð **Spamni tekshirish**: spm. 
ð **User haqida malumot olish**: .userinfo <reply>
ð **Type yozuv effecti**: type. <text>
ð **Lichkangizga yozgan odamlarni blocklash**:  blockon. blockoff. blockinfo. pa. pda. tlist. 
ð **Avto otvet gutuh, contactlarda**: afkon. afkoff. afkinfo. 
ð **Habarlarni tarjima qilish**: tr. <Language code> reply message
ð **JOJO INFO**: alive. 
ð **Ip-tracer**: iptrace. <ip address>
ð **Rasmlarni ascci korinishiga ogiradi**: ascci. <reply media message>
ð **Figlet texts**: figlet. <text>
ð **clone pic**: picer. reply user
ð  ~~JOJO USERBOT~~ 					
								""", buttons= [
								[Button.inline("INFORMATION", data=b"1")],
								[Button.url("Tg channel", url="https://t.me/jojo_userbot")]
								
								])
								await query.answer([result])
@botClient.on(events.CallbackQuery)
async def uzgaruvchi(event):
				
				if event.data==b'1':
								await event.answer("JOJO | USERBOT - 1.0.1.4v \nHavfsiz Userbot\nserverga ulangamagan juda oddiy yuserbot\nha 4 kun ichida yangilanib turadi\ndasturchi: @red_uzbek\nmaqsad: Insonlarga telegramda oz boÊ»lsa da yordam berish", alert=True)

@events.register(events.NewMessage(pattern=".help", outgoing=True))
async def help(event):
				results = await client.inline_query("@jojo_user_bot", "ppphelp")
				await results[0].click(event.chat_id)
				await event.message.delete()
