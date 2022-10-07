from telethon import events
from time import sleep
from telethon.tl.functions.users import GetFullUserRequest
from telethon import functions

approvedusers = set([])
protectionmode = set([])

@events.register(events.NewMessage(outgoing=True, pattern=r'\.blockon'))
async def red(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        if protectionmode:
            if "off" in protectionmode:
                protectionmode.remove("off")
        guardmodeon = "on"
        if guardmodeon in protectionmode:
            await event.client.send_message(messagelocation, "Lichkangizga yozgan odam endi avtomatik blocklanadi...\nJOJO | USERBOT")
        else:
            protectionmode.add(guardmodeon)
            await event.client.send_message(messagelocation, "Lichkangizga yozgan odam endi avtomatik blocklanadi...\nJOJO | USERBOT")
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r'\.blockoff'))
async def reduz(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        guardmodeoff = "off"
        if "on" in protectionmode:
            protectionmode.remove("on")
        if guardmodeoff in protectionmode:
            await event.client.send_message(messagelocation, "BLOCK - plugini oʻchirildi...\nJOJO | USERBOT")
        else:
            protectionmode.add(guardmodeoff)
            await event.client.send_message(messagelocation, "BLOCK - plugini oʻchirildi...\nJOJO | USERBOT")
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r'\.blockinfo'))
async def reduzb(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        statusinformation = []
        if protectionmode:
            for details in protectionmode:
                statusinformation.append(details)
            convertdata = "\n".join(statusinformation)
            await event.client.send_message(messagelocation, f"Block on/off: {convertdata.title()}")
        else:
            await event.client.send_message(messagelocation, "block himoyasi sukit boyicha oʻchirilgan")
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r'\.pa'))
async def reduzbe(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        getinformation = await event.get_reply_message()
        selecteduser = getinformation.sender_id
        if selecteduser not in approvedusers:
            approvedusers.add(selecteduser)
            await event.client.send_message(messagelocation, "Bu foydalanuvchi muvaffaqiyatli tasdiqlandi")
        else:
            await event.client.send_message(messagelocation, "Bu foydalanuvchi muvaffaqiyatli tasdiqlandi")
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r'\.pda'))
async def reduzbek(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        getinformation = await event.get_reply_message()
        selecteduser = getinformation.sender_id
        if selecteduser in approvedusers:
            approvedusers.remove(selecteduser)
            await event.client.send_message(messagelocation, "Bu foydalanuvchi tasdiqlangan roʻyxatdan muvaffaqiyatli olib tashlandi")
        else:
            await event.client.send_message(messagelocation, "Bu foydalanuvchini tasdiqlamadingiz ! ")
    except:
        pass

@events.register(events.NewMessage(outgoing=True, pattern=r'\.tlist'))
async def reduzbek77(event):
    await event.edit("Processing...")
    sleep(2)
    await event.delete()
    messagelocation = event.to_id
    try:
        approveddetails = []
        if approvedusers:
            for details in approvedusers:
                approveddetails.append(details)
            convertdata = "\n".join(map(str,approveddetails))
            lenght = len(approvedusers)
            if lenght == 1:
                await event.client.send_message(messagelocation, f"Tasdiqlangan userlar:\n{convertdata}")
            else:
                await event.client.send_message(messagelocation, f"tasdiqlangan userlar:\n{convertdata}")
        else:
            await event.client.send_message(messagelocation, "Tasdiqlangan foydalanuvchilar topilmadi...")
    except:
        pass

@events.register(events.NewMessage)
async def reduzbek7719(event):
    if event.is_private:
        getridogramuserdetails = await event.client(GetFullUserRequest("me"))
        ridogramuser = getridogramuserdetails.users[0].id
        user = await event.get_chat()
        messagelocation = user.id
        blockimage = "http://telegra.ph/file/c870c436c2ebe20c2b21f.jpg"
        senderinformation = await event.client(GetFullUserRequest(user.id))
        itisbot = senderinformation.users[0].bot
        isridogramuser = await event.get_sender()
        try:
            if "on" in protectionmode:
                if itisbot == True:
                    pass
                else:
                    if user.id not in approvedusers:
                        if user.id == ridogramuser:
                            pass
                        else:
                            if ridogramuser == isridogramuser.id:
                                pass
                            else:
                                await event.client.send_file(messagelocation, blockimage, caption=f"Hurmatli {user.first_name}, \nmenga xabar yuborganingiz uchun tashakkur, lekin men sizni vaqtincha bloklayapman, chunki sizga xabar yuborishingizga ruxsat bermayapman, iltimos, ruxsatimni kuting")
                                await event.client(functions.contacts.BlockRequest(user.id))
        except:
            pass