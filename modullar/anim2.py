import asyncio
from collections import deque

from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Cat"


@borg.on(admin_cmd(pattern=r"star$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("π¦β¨π¦β¨π¦β¨π¦β¨"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(admin_cmd(pattern=r"boxs"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("π₯π§π¨π©π¦πͺπ«β¬β¬"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(admin_cmd(pattern=f"rain$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("π¬βοΈπ©π¨π§π¦π₯βπ€"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(admin_cmd(pattern=r"clol$"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("π€π§π€¨π€π§π€¨"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(admin_cmd(pattern=r"odra$"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("πΆππΆππΆππΆπ"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(admin_cmd(pattern=r"deploy$"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0, 12)
    await event.edit("Deploying...")
    animation_chars = [
        "**Heroku Connecting To Latest Github Build **",
        f"**Build started by user** ** {DEFAULTUSER} **",
        f"**Deploy** `535a74f0` **by user** ** {DEFAULTUSER} **",
        "**Restarting Heroku Server...**",
        "**State changed from up to starting**",
        "**Stopping all processes with SIGTERM**",
        "**Process exited with** `status 143`",
        "**Starting process with command** `python3 -m stdborg`",
        "**State changed from starting to up**",
        "__INFO:Userbot:Logged in as 557667062__",
        "__INFO:Userbot:Successfully loaded all plugins__",
        "**Build Succeeded**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@events.register(events.NewMessage(pattern=".dump "))
async def dump(message):
    try:
        obj = message.pattern_match.group(1)
        if len(obj) != 3:
            raise IndexError
        inp = " ".join(obj)
    except IndexError:
        inp = "π₯ π π«"
    u, t, g, o, s, n = inp.split(), "π", "<(^_^ <)", "(> ^_^)>", "β  ", "\n"
    h = [(u[0], u[1], u[2]), (u[0], u[1], ""), (u[0], "", "")]
    for something in reversed(
        [
            y
            for y in (
                [
                    "".join(x)
                    for x in (
                        f + (s, g, s + s * f.count(""), t),
                        f + (g, s * 2 + s * f.count(""), t),
                        f[:i] + (o, f[i], s * 2 + s * f.count(""), t),
                        f[:i] + (s + s * f.count(""), o, f[i], s, t),
                        f[:i] + (s * 2 + s * f.count(""), o, f[i], t),
                        f[:i] + (s * 3 + s * f.count(""), o, t),
                        f[:i] + (s * 3 + s * f.count(""), g, t),
                    )
                ]
                for i, f in enumerate(reversed(h))
            )
        ]
    ):
        for something_else in something:
            await asyncio.sleep(0.3)
            try:
                await message.edit(something_else)
            except errors.MessageIdInvalidError:
                return


@borg.on(admin_cmd(pattern="fleaveme$"))
async def _(event):
    animation_interval = 1
    animation_ttl = range(0, 10)
    animation_chars = [
        "β¬β¬β¬\nβ¬β¬β¬\nβ¬β¬β¬",
        "β¬β¬β¬\nβ¬πβ¬\nβ¬β¬β¬",
        "β¬β¬οΈβ¬\nβ¬πβ¬\nβ¬β¬β¬",
        "β¬β¬οΈβοΈ\nβ¬πβ¬\nβ¬β¬β¬",
        "β¬β¬οΈβοΈ\nβ¬πβ‘οΈ\nβ¬β¬β¬",
        "β¬β¬οΈβοΈ\nβ¬πβ‘οΈ\nβ¬β¬βοΈ",
        "β¬β¬οΈβοΈ\nβ¬πβ‘οΈ\nβ¬β¬οΈβοΈ",
        "β¬β¬οΈβοΈ\nβ¬πβ‘οΈ\nβοΈβ¬οΈβοΈ",
        "β¬β¬οΈβοΈ\nβ¬οΈπβ‘οΈ\nβοΈβ¬οΈβοΈ",
        "βοΈβ¬οΈβοΈ\nβ¬οΈπβ‘οΈ\nβοΈβ¬οΈβοΈ",
    ]
    if event.fwd_from:
        return
    await event.edit("fleaveme....")
    await asyncio.sleep(2)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])


@borg.on(admin_cmd(pattern="loveu", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 70)
    await event.edit("loveu")
    animation_chars = [
        "π",
        "π©βπ¨",
        "π",
        "π",
        "π€£",
        "π",
        "π",
        "π",
        "π",
        "βΊ",
        "π",
        "π€",
        "π€¨",
        "π",
        "π",
        "πΆ",
        "π£",
        "π₯",
        "π?",
        "π€",
        "π―",
        "π΄",
        "π",
        "π",
        "βΉ",
        "π",
        "π",
        "π",
        "π",
        "π’",
        "π­",
        "π€―",
        "π",
        "β€",
        "i Love Youβ€",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 35])


@borg.on(admin_cmd(pattern=f"plane", outgoing=True))
async def _(event):
    if event.fwd_from:
        retun
    await event.edit("β-------------")
    await event.edit("-β------------")
    await event.edit("--β-----------")
    await event.edit("---β----------")
    await event.edit("----β---------")
    await event.edit("-----β--------")
    await event.edit("------β-------")
    await event.edit("-------β------")
    await event.edit("--------β-----")
    await event.edit("---------β----")
    await event.edit("----------β---")
    await event.edit("-----------β--")
    await event.edit("------------β-")
    await event.edit("-------------β")
    await asyncio.sleep(3)
    await event.delete()


@borg.on(admin_cmd(pattern=r"police"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 12)
    await event.edit("Police")
    animation_chars = [
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        "π΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄\nπ΅π΅π΅β¬β¬β¬π΄π΄π΄",
        "π΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅\nπ΄π΄π΄β¬β¬β¬π΅π΅π΅",
        f"{DEFAULTUSER} **Police iz Here**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@borg.on(admin_cmd(pattern=f"jio$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 19)
    await event.edit("jio network boosting...")
    animation_chars = [
        "`Connecting To JIO NETWORK ....`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "*Optimising JIO NETWORK...*",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "`β β β β β β β`",
        "**JIO NETWORK Boosted....**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 19])


@borg.on(admin_cmd(pattern=f"solarsystem", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 80)
    await event.edit("solarsystem")
    animation_chars = [
        "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
        "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nπβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
        "`βΌοΈπβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈββΌοΈ`",
        "`βΌοΈβΌοΈβΌοΈπβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈββΌοΈβΌοΈβΌοΈ`",
        "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
        "`βΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nββΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈπ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ`",
        "`βΌοΈββΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈπβΌοΈ`",
        "`βΌοΈβΌοΈβΌοΈββΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈβΌοΈπβΌοΈβΌοΈ\nβΌοΈβΌοΈβΌοΈβΌοΈβΌοΈ\nβΌοΈπβΌοΈβΌοΈβΌοΈ`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])
