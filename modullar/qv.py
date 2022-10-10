from telethon import events
#from datetime import datetime
#i#mport io
#import speedtest
#from userbot.utils import admin_cmd
import asyncio 

@events.register(events.NewMessage(pattern=".qv"))
#@borg.on(admin_cmd(pattern="quote ?(.*)"))
async def quote_search(event):
    if event.fwd_from:
        return
    await event.edit("Processing...")
    #search_string = event.pattern_match.group(1)
    input_url = "https://apis.xditya.me/write?text={}".format(search_string)
    headers = {"USER-AGENT": "UniBorg"}
    try:
        response = requests.get(input_url, headers=headers).json()
    except:
        response = None
    if response is not None:
        result = random.choice(response).get("input_message_content").get("message_text")
    else:
        result = None
    if result:
        await event.edit(result.replace("<code>", "`").replace("</code>", "`"))
    else:
        await event.edit("Zero results found")