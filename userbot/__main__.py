from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, DARKMAMBAversion
from pathlib import Path
import asyncio
import glob
import telethon.utils
l2= Config.SUDO_COMMAND_HAND_LER
DARKMAMBA_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/95f920f5168d50160f5a7.jpg"
l1 = Config.COMMAND_HAND_LER


async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"DARKMAMBA_STRING - {str(e)}")
        sys.exit()
        
        
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.BOT_USERNAME is not None:
        print("Initiating Inline Bot")
        bot.tgbot = TelegramClient(
            "BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.BOT_TOKEN)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.BOT_USERNAME))
        print("Startup Completed")
    else:
        bot.start()
print("Loading Modules / Plugins")


async def module():
  import glob
  path = 'userbot/plugins/*.py'
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      load_module(shortname.replace(".py", ""))
"""
async def assistant():
    path = "userbot/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
      with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))

        extra_repo = "https://github.com/HIDDENB0Y/DARKMAMBA"
        try:
            os.system(f"git clone {extra_repo}")  
        except BaseException:
            pass
        import glob
        LOGS.info("Loading Addons")
        path = "DARKMAMBAUSERBOT/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as ex:
                path2 = Path(ex.name)
                shortname = path2.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                    if not shortname.startswith("__") or shortname.startswith("_"):
                        LOGS.info(f"[DARKMAMBA] - Addons -  Installed - {shortname}")
                except Exception as e:
                    LOGS.warning(f"[DARKMAMBA] - Addons - ERROR - {shortname}")
                    LOGS.warning(str(e))
    else:
        print("Addons Not Loading")
"""
bot.loop.run_until_complete(module())

print(f"""『🔱DARKMAMBA🔱』➙𖤍࿐ IS ON!!! DARKMAMBA VERSION :- {DARKMAMBAversion}
TYPE :- " .gpromote @SUKHI-MR_HACKER " OR .python OR .ping CHECK IF I'M ON!
╔════❰DARKMAMBA❱═❍⊱❁۪۪
║┣⪼ OWNER - HIDDENB0Y
║┣⪼{DARKMAMBA_PIC}
║┣⪼ CREATOR -@SUKHI_MR_HACKER
║┣⪼ TELETHON - 1.2.0
║┣⪼ ✨ 『🔱DARKMAMBA 🔱』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱""")



async def darkmamba_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                DARKMAMBA_PIC,
                caption=f"#START \n\nDeployed DARKMAMBA Successfully\n\n**DARKMAMBA- {DARKMAMBAversion}**\n\nType `{l1}python` or `{l1}pyalive` to check! \n\nJoin [DARKMAMBA Channel](t.me/DARKMAMBA_UPDATES) for Updates & [DARKMAMBA Chat](t.me/DARKMAMBA_SUPPORT) for any query regarding DARKMAMBA",
            )
    except Exception as e:
        print(str(e))

# Join DARKMAMBA Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@DARKMAMBA_UPDATES"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@DARKMAMBA_SUPPORT"))
    except BaseException:
         pass


bot.loop.create_task(darkmamba_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
