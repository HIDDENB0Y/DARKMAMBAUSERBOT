from math import ceil
from re import compile
import asyncio
import html
import os
import re
import sys
from telethon.events import InlineQuery, callbackquery
from userbot import *
from userbot.cmdhelp import *
from PYTHONBOT.utils import *
import telethon.tl.functions
from userbot.Config import Config
from userbot import ALIVE_NAME
from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ExportChatInviteRequest
DEFAULTUSER = ALIVE_NAME or "PYTHON"
from . import * 
python_row = Config.BUTTONS_IN_HELP
python_emoji1 = Config.EMOJI_IN_HELP1
python_emoji2 = Config.EMOJI_IN_HELP2
alive_emoji = Config.ALIVE_EMOJI
python_pic = Config.PM_PIC or ""
cstm_pmp = Config.PM_MSG
ALV_PIC = Config.ALIVE_PIC
help_pic = Config.HELP_PIC or "https://te.legra.ph/file/d8301597d9e9647d2be06.jpg"
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"

LOG_GP = Config.LOGGER_ID
mssge = (
    str(cstm_pmp)
    if cstm_pmp
    else "**You Have Trespassed To My Master's PM!\nThis Is Illegal And Regarded As Crime.**"
)

USER_BOT_WARN_ZERO = "Enough Of Your Flooding In My Master's PM!! \n\n**π« Blocked and Reported**"

PYTHON_FIRST = (
    "π·ππππ πππ/πΌπππ,\nπΈ πππππ'π ππππππππ π’ππ π’ππ ππ ππππππππ πππππππ πππβ οΈ.\n"
    "ππ‘π’π¬ ππ¬ ππ² ππ°π§ππ« {}\n\n"
    "**{}**\n\nPlease Choose Why u Are Hereβ₯οΈ!!"
)

alive_txt = """
    **{}**\n
   **β₯οΈαΊΓΈβ  αΊβ Ξ±β Β΅Ρβ₯οΈ**
**β’{}β’ΓΥ‘Υ²Μ?½Μr :** {}\n
**β’{}β’pyhtonαΊΓΈβ  :** {}
**β’{}β’β ?½Μl?½ΜΖ­hΓΈΥ²  :** {}
**β’{}β’ΓbΓ»ΓΓͺ     :** {}
**β’{}β’ΓudΓΈ      :** {}
**β’{}β’BΓΈβ        :** {}
"""

def button(page, modules):
    Row = python_row
    Column = 3

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(f"{python_emoji1} " + pair + f" {python_emoji2}", data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
               f"β­ΟΞ±Ο²ΞΊ{alive_emoji}", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"{python_emoji2} β {python_emoji1}", data="close"
            ),
            custom.Button.inline(
               f"{alive_emoji}Υ²?½xΤ΅β­", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]


    modules = CMD_HELP
if Config.BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "pythonbot_help":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            help_msg = f"π©{python_emoji2}{python_mention}{python_emoji1}πͺ\n\n**ππππππ πΌππππππ πΈπππππππππ₯β­ `{len(CMD_HELP)}`**\n**πTΞΏΟΞ±β CΞΏΠΌΠΌΞ±ΠΈβΡπ₯β­ `{len(apn)}`**\n**πPΞ±Φ?½β­ 1/{veriler[0]}** \n"
            if help_pic and help_pic.endswith((".jpg", ".png")):
                result = builder.photo(
                    help_pic,
                    text=help_msg,
                    buttons=veriler[1],
                    link_preview=False,
                )
            elif help_pic:
                result = builder.document(
                    help_pic,
                    text=help_msg,
                    title="PythonBot Alive",
                    buttons=veriler[1],
                    link_preview=False,
                )
            else:
                result = builder.article(
                    f"Hey! Only use .op please",
                    text=help_msg,
                    buttons=veriler[1],
                    link_preview=False,
                )
        elif event.query.user_id == bot.uid and query.startswith("fsub"):
            hunter = event.pattern_match.group(1)
            python = hunter.split("+")
            user = await bot.get_entity(int(python[0]))
            channel = await bot.get_entity(int(python[1]))
            msg = f"**π Welcome** [{user.first_name}](tg://user?id={user.id}), \n\n**π You need to Join** {channel.title} **to chat in this group.**"
            if not channel.username:
                link = (await bot(ExportChatInviteRequest(channel))).link
            else:
                link = "https://t.me/" + channel.username
            result = [
                await builder.article(
                    title="force_sub",
                    text = msg,
                    buttons=[
                        [Button.url(text="Channel", url=link)],
                        [custom.Button.inline("π Unmute Me", data=unmute)],
                    ],
                )
            ]
 
        elif event.query.user_id == bot.uid and query == "alive":
            pyt_thon = alive_txt.format(Config.ALIVE_MSG, alive_emoji, python_mention, alive_emoji, PYTHONversion, alive_emoji, version.__version__, alive_emoji, abuse_m, alive_emoji, is_sudo, alive_emoji, Config.BOY_OR_GIRL)
            alv_btn = [
                [Button.url(f"{PYTHON_USER}", f"tg://openmessage?user_id={Legendl_Mr_Hacker}")],
                [Button.url("My Channel", f"https://t.me/{my_channel}"), 
                Button.url("My Group", f"https://t.me/{my_group}")],
            ]
            if ALV_PIC and ALV_PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALV_PIC,
                    text=pyt_hon,
                    buttons=alv_btn,
                    link_preview=False,
                )
            elif ALV_PIC:
                result = builder.document(
                    ALV_PIC,
                    text=pyt_thon,
                    title="PythonBot Alive",
                    buttons=alv_btn,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    text=pyt_thon,
                    title="PythonBot Alive",
                    buttons=alv_btn,
                    link_preview=False,
                )

        elif event.query.user_id == bot.uid and query == "pm_warn":
            pyth_on = PYTHON_FIRST.format(python_mention, mssge)
            result = builder.photo(
                file=python_pic,
                text=pyth_on,
                buttons=[
                    [
                        custom.Button.inline("π Request π", data="req"),
                        custom.Button.inline("π¬ Chat π¬", data="chat"),
                    ],
                    [custom.Button.inline("π« Spam π«", data="heheboi")],
                    [custom.Button.inline("Curious β", data="pmclick")],
                ],
            )

        elif event.query.user_id == bot.uid and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"**β π»ππππππππ’ π°π PYTHONπ±ππ β**",
                buttons=[
                    [Button.url("β₯οΈ ππππ β₯", "https://github.com/LEGEND-LX/PYTHONBOT")],
                    [Button.url("β¦οΈ Relp β¦οΈ", "https://replit.com/@LEGEND-LX/PYTHONBOT-4")],
                ],
            )

        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[βββ β]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )

        else:
            result = builder.article(
                "@python_Userbot_Support",
                text="""**Hey! This is [PythonαΊΓΈβ ](https://t.me/Python_Userbot_Support) \nYou can know more about me from the links given below π**""",
                buttons=[
                    [
                        custom.Button.url("π₯ CHANNEL π₯", "https://t.me/Python_Updata"),
                        custom.Button.url(
                            "β‘ GROUP β‘", "https://t.me/Python_Userbot_Support"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "β¨ REPO β¨", "https://github.com/LEGEND-LX/PYTHONBOT"),
                        custom.Button.url
                    (
                            "π° TUTORIAL π°", "https://youtu.be/yvNKVtXAndo"
                    )
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"pmclick")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for Other Users..."
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"π° This is PythonαΊΓΈβ  PM Security for {python_mention} to keep away unwanted retards from spamming PM..."
            )

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"req")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"β **Request Registered** \n\n{python_mention} will now decide to look for your request or not.\nπ Till then wait patiently and don't spam!!"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**π Hey {python_mention} !!** \n\nβοΈ You Got A Request From [{first_name}](tg://user?id={ok}) In PM!!"
            await bot.send_message(LOG_GP, tosend)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"chat")))
    async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Ahh!! You here to do chit-chat!!\n\nPlease wait for {python_mention} to come. Till then keep patience and don't spam."
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"**π Hey {python_mention} !!** \n\nβοΈ You Got A PM from  [{first_name}](tg://user?id={ok})  for random chats!!"
            await bot.send_message(LOG_GP, tosend)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"heheboi")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"π₯΄ **Nikal lawde\nPehli fursat me nikal**"
            )
            await event.client(functions.contacts.BlockRequest(event.query.user_id))
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            first_name = html.escape(target.user.first_name)
            await bot.send_message(
                LOG_GP,
                f"**Blocked**  [{first_name}](tg://user?id={ok}) \n\nReason:- Spam",
            )


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"unmute")))
    async def on_pm_click(event):
        hunter = (event.data_match.group(1)).decode("UTF-8")
        python = hunter.split("+")
        if not event.sender_id == int(python[0]):
            return await event.answer("This Ain't For You!!", alert=True)
        try:
            await bot(GetParticipantRequest(int(python[1]), int(python[0])))
        except UserNotParticipantError:
            return await event.answer(
                "You need to join the channel first.", alert=True
            )
        await bot.edit_permissions(
            event.chat_id, int(python[0]), send_message=True, until_date=None
        )
        await event.edit("Yay! You can chat now !!")


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"reopen")))
    async def reopn(event):
            if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
                current_page_number=0
                simp = button(current_page_number, CMD_HELP)
                veriler = button(0, sorted(CMD_HELP))
                apn = []
                for x in CMD_LIST.values():
                    for y in x:
                        apn.append(y)
                await event.edit(
                    f"",
                    buttons=simp[1],
                    link_preview=False,
                )
            else:
                reply_pop_up_alert = "ΞΏΠ½ Ο²ΞΏΠΌΠΌΞΏΠΈ Ξ³Ξ±ΡΡ Ο ΟΠ½ΞΉΠΈΞΊ Ο Ο²Ξ±ΠΈ Ο²βΞΉΟ²ΞΊ ΞΏΠΈ ΞΉΟπππ. βΡΟβΞΏΞ³ ΟΡ ΞΏΟΠΈ ΟΞΏΟ. Β© PythonαΊΓΈβ β’"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            veriler = custom.Button.inline(f"{python_emoji1} Re-Open Menu {python_emoji2}", data="reopen")
            await event.edit(f"**βοΈ PythonαΊΓΈβ  MΓͺΓ±Γ» PrΓ΅vΓ?dΓͺr hΓ‘Ε‘ bΔΔn ΔΕΓΈΕ‘Δd by {python_mention} βοΈ**\n\n**Bot Of :**  {python_mention}\n\n            [Β©οΈPythonαΊΓΈβ ]({chnl_link})", buttons=veriler, link_preview=False)
        else:
            reply_pop_up_alert = "ΞΊΞ³Ξ± ΟΠΈgβΞΉ ΞΊΞ±Ρ ΡΠ½Ρ Π½ΞΏ ΠΌΡΡΡ ΟΞΏΟ ΟΞ±Ρ Ξ±gΞ±Ρ Ο²Π½Ξ±Π½ΞΉΞ³Ρ ΟΞΏΠ½ ΞΊΠ½Οβ ΞΊΞ± ΟΞ±ΠΈΞ± βΞΏ ΠΈΞ±. AΞ± Χ Ξ±ΟΡ Π½ΞΏ ΟΠΈgβΞΉ ΞΊΞ±ΡΠΈΡ ΠΌΡΡΡ ΟΞΏΟ ΟΡ.   Β©PythonαΊΓΈβ "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
   

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        apn = []
        for x in CMD_LIST.values():
            for y in x:
                apn.append(y)
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                f"**π©β₯οΈ{python_emoji2}{python_mention}{python_emoji1}πͺ\n\n**πΉοΈπππππ πΌππππππ πΈππππππππβ­ `{len(CMD_HELP)}`**\n**β¨οΈTΞΏΟΞ±β CΞΏΠΌΠΌΞ±ΠΈβΡβ­ `{len(apn)}`**\n**πPΞ±Φ?½β­ 1/{veriler[0]}**",
                buttons=veriler[1],
                link_preview=False,
            )
        else:
            return await event.answer(
                "ΞΊΞ³Ξ± ΟΠΈgβΞΉ ΞΊΞ±Ρ ΡΠ½Ρ Π½ΞΏ ΠΌΡΡΡ ΟΞΏΟ ΟΞ±Ρ Ξ±gΞ±Ρ Ο²Π½Ξ±Π½ΞΉΞ³Ρ ΟΞΏΠ½ ΞΊΠ½Οβ ΞΊΞ± ΟΞ±ΠΈΞ± βΞΏ ΠΈΞ± Ξ±Ξ± Χ Ξ±ΟΡ Π½ΞΏ ΟΠΈgβΞΉ ΞΊΞ±ΡΠΈΡ ΠΌΡΡΡ ΟΞΏΟ ΟΡ.   Β©PythonαΊΓΈβ ",
                cache_time=0,
                alert=True,
            )


    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "β‘ " + cmd[0] + " β‘", data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline(f"{python_emoji1} Main Menu {python_emoji2}", data=f"page({page})")])
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                f"**π π΅πππ :**  `{commands}`\n**π’ Number of commands :**  `{len(CMD_HELP_BOT[commands]['commands'])}`",
                buttons=buttons,
                link_preview=False,
            )
        else:
            return await event.answer(
                "Hoo gya aapka. Kabse tapar tapar dabae jaa rhe h. Khudka bna lo na agr chaiye to. Β©PythonαΊΓΈβ β’",
                cache_time=0,
                alert=True,
            )


    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")
        result = f"**π π΅πππ :**  `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**β οΈ πππππππ :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
            result += f"**β‘ Type :**  {CMD_HELP_BOT[cmd]['info']['type']}\n"
        else:
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**β οΈ πππππππ :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**β‘ Type :**  {CMD_HELP_BOT[cmd]['info']['type']}\n"
            result += f"**βΉοΈ πΈπππ :**  {CMD_HELP_BOT[cmd]['info']['info']}\n"
            
        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**π  π²πππππππ :**  `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
        else:
            result += f"**π  π²πππππππ :**  `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"
        if command["example"] is None:
            result += f"**π¬ π΄π‘πππππππππ :**  `{command['usage']}`\n\n"
        else:
            result += f"**π¬ π΄π‘πππππππππ :**  `{command['usage']}`\n"
            result += f"**β¨οΈ π΅ππ π΄π‘πππππ :**  `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"
        if event.query.user_id == bot.uid or event.query.user_id in Config.SUDO_USERS:
            await event.edit(
                result,
                buttons=[
                    custom.Button.inline(f"{python_emoji1} Return {python_emoji2}", data=f"Information[{page}]({cmd})")
                ],
                link_preview=False,
            )
        else:
            return await event.answer(
                "α΅α΅Κ°β± α΅α΅α΅ βΏΚ°β± Λ’α΅α΅Κ²Κ°α΅ α΅Κ°α΅α΅α΅α΅ α΅α΅βΏα΅ Λ‘α΅ βΏα΅ α΅α΅Κ° α΅Λ’α΅ α΅α΅Κ³βΏα΅ Κ° α΅α΅Κ° α΅ΚΈα΅ α΅βΏα΅Λ‘β± α΅α΅Κ³ Κ³Κ°α΅ Κ°α΅.π€¦ββοΈπ€¦ββοΈπ€¦ββοΈ Β©PythonαΊΓΈβ β’ ",
                cache_time=0,
                alert=True,
            )





    
