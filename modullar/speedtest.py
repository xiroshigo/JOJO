from telethon import events
#from datetime import datetime
#i#mport io
#import speedtest
#from userbot.utils import admin_cmd
import asyncio 

@events.register(events.NewMessage(pattern=".wtf"))
async def wtf(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    await event.edit("wtf")
    animation_chars = [
            "What",
            "What The",
            "What The F",
            "What The F Brah",
            "[What The F Brah](https://telegra.ph//file/f3b760e4a99340d331f9b.jpg)"
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i %5 ])