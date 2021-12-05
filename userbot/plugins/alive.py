import time
import random
import time
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from userbot.Config import Config
from telethon import version
from userbot import ALIVE_NAME, StartTime, DARKMAMBAversion
from DARKMAMBA.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from . import *
async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "🌠✮  🎀  𝒟𝒜𝑅𝒦𝑀𝒜𝑀𝐵𝒜  🎀  ✮🌠 🇮🇳"
DARKMAMBA_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "ℓєgєи∂ Choice 🌠✮  🎀  𝒟𝒜𝑅𝒦𝑀𝒜𝑀𝐵𝒜  🎀  ✮🌠"
CUSTOM_YOUR_GROUP =Config.YOUR_GROUP or "@DARKMAMBA_SUPPORT"

darkmamba= bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={darkmamba})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="pyalive$"))
@bot.on(sudo_cmd(pattern="pyalive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if  DARKMAMBA_IMG:
        DARKMAMBA_caption = f"{CUSTOM_ALIVE_TEXT}**\n"
        
        DARKMAMBA_caption += f"╔════❰𓆩༒Alive-linux𓆩༒❱═❍⊱❁ \n"
        DARKMAMBA_caption += f"║╭━━━━━━━━━━━━━━━➣ \n"
        DARKMAMBA_caption += f"║┣⪼𓆩༒Developer༒𓆪⭆[SUKHI](t.me/SUKHI_MR_HACKER) \n"
        DARKMAMBA_caption += f"║┣⪼𓆩༒E-Developer༒𓆪⭆[HELLBOY](t.me/HELLL_BOYYY) \n"
        DARKMAMBA_caption += f"║╰━━━━━━━━━━━━━━━➣\n"
        DARKMAMBA_caption += f"║╭━━━━━━━━━━━━━━━➣ \n"
        DARKMAMBA_caption += f"║┣⪼𓆩༒MAMBA༒𓆪⭆[MAMBA](https://github.com/SUKHPAL443/MAMBAPRO)\n"
        DARKMAMBA_caption += f"║┣⪼𓆩༒PyMAMBA༒𓆪⭆9.0.8,3.0\n"
        DARKMAMBA_caption += f"║┣⪼𓆩༒MAMBAMix༒𓆪⭆3.0\n"
        DARKMAMBA_caption += f"║╰━━━━━━━━━━━━━━━➣ \n"
        DARKMAMBA_caption += f"╔══❰𓆩༒Ⲃⲟⲧ Ⲓⲛϝⲟʀⲙⲁⲧⲓⲟⲛ𓆩༒❱═➣\n"
        DARKMAMBA_caption += f"║╭━━━━━━━━━━━━━━━➣ \n"
        DARKMAMBA_caption += f"║┣⪼𓆩༒Ⲟⲱⲛⲉʀ༒𓆪⭆[SUKHI](t.me/SUKHI_MR_HACKER) \n"        
        DARKMAMBA_caption += f"║┣⪼𓆩༒Ⲋⲧⲁⲧυⲋ༒𓆪⭆Ⲟⲛⳑⲓⲛⲉ\n"            
        DARKMAMBA_caption += f"║┣⪼𓆩༒Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ༒𓆪⭆{mention}\n" 
        DARKMAMBA_caption += f"║┣⪼𓆩༒Ⳙⲣⲧⲓⲙⲉ༒𓆪⭆         {uptime}\n"
        DARKMAMBA_caption += f"║┣⪼𓆩༒Ⲃⲟⲧ Ⲣⲓⲛⳋ༒𓆪⭆        290.087 \n"   
        DARKMAMBA_caption += f"║┣⪼𓆩༒DARKMAMBA༒𓆪⭆         {DARKMAMBAversion}\n"
        DARKMAMBA_caption += f"║┣⪼𓆩༒Os:༒𓆪⭆    [Kali GNU/Linux](https://pkg.kali.org/derivative/kali-roll/) \n"   
        DARKMAMBA_caption += f"║┣⪼𓆩༒Ⲧⲉⳑⲉⲧⲏⲟⲛ༒𓆪⭆        {version.__version__}\n" 
        DARKMAMBA_caption += f"║┣⪼[𓆩༒DARKMAMBA┣⪼ 𝐔𝐬𝐞𝐫𝐛𝐨𝐭༒𓆪](https://t.me/DARKMAMBA_SUPPORT)\n"
        DARKMAMBA_caption += f"║╰━━━━━━━━━━━━━━━➣ \n"
        DARKMAMBA_caption += f"╚══════════════════❍⊱❁۪۪\n"
        
        await alive.client.send_file(
            alive.chat_id, DARKMAMBA_IMG, caption=DARKMAMBA_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"╔════❰Alive-linux❱═❍⊱❁ \n"
            f"║╭━━━━━━━━━━━━━━━➣ \n"
            f"║┣⪼Developer    ┣⪼ [SUKHI](t.me/SUKHI_MR_HACKER) \n"
            f"║┣⪼E-Developer  ┣⪼ [HELLBOY](t.me/HELLL_BOYYY) \n"
            f"║╰━━━━━━━━━━━━━━━➣\n"
            f"║╭━━━━━━━━━━━━━━━➣ \n"
            f"║┣⪼MAMBA    ┣⪼  [MAMBA](https://github.com/SUKHPAL443/MAMBAPRO)\n"
            f"║┣⪼PyMAMBA     ┣⪼9.0.8,3.0\n"
            f"║┣⪼MAMBAMix    ┣⪼ 3.0\n"
            f"║╰━━━━━━━━━━━━━━━➣ \n"
            f"╔══❰🔥Ⲃⲟⲧ Ⲓⲛϝⲟʀⲙⲁⲧⲓⲟⲛ🔥❱═➣\n"
            f"║╭━━━━━━━━━━━━━━━➣ \n"
            f"║┣⪼Ⲟⲱⲛⲉʀ      ┣⪼   [SUKHI](t.me/SUKHI_MR_HACKER) \n"
            f"║┣⪼Ⲋⲧⲁⲧυⲋ       ┣⪼    Ⲟⲛⳑⲓⲛⲉ\n"
            f"║┣⪼Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ  ┣⪼  {mention}\n"
            f"║┣⪼Ⳙⲣⲧⲓⲙⲉ       ┣⪼  {uptime}\n"
            f"║┣⪼Ⲃⲟⲧ Ⲣⲓⲛⳋ     ┣⪼   290.087 \n"   
            f"║┣⪼DARKMAMBA       ┣⪼  {DARKMAMBAversion}\n"
            f"║┣⪼Os:          ┣⪼  [Kali GNU/Linux](https://pkg.kali.org/derivative/kali-roll/) \n"   
            f"║┣⪼Ⲧⲉⳑⲉⲧⲏⲟⲛ      ┣⪼  {version.__version__}\n" 
            f"║┣⪼[✨🐍DARKMAMBA┣⪼ 𝐔𝐬𝐞𝐫𝐛𝐨𝐭🐍✨](https://t.me/DARKMAMBA_SUPPORT)\n"
            f"║╰━━━━━━━━━━━━━━━➣ \n"
            f"╚══════════════════❍⊱❁۪۪\n"
        )


msg = f"""
  ⚜️ 🌠✮  🎀  𝒟𝒜𝑅𝒦𝑀𝒜𝑀𝐵𝒜  🎀  ✮🌠 ιѕ σиℓιиє ⚜️
{Config.ALIVE_MSG}
**╔════❰Alive-linux❱═❍⊱❁ \n"
**║╭━━━━━━━━━━━━━━━➣ \n"
**║┣⪼Developer    ┣⪼ [SUKHI](t.me/SUKHI_MR_HACKER) \n"
**║┣⪼E-Developer  ┣⪼ [HELLBOY](t.me/HELLL_BOYYY) \n"
**║╰━━━━━━━━━━━━━━━➣\n"
**║╭━━━━━━━━━━━━━━━➣ \n"
**║┣⪼MAMBA    ┣⪼  [MAMBA](https://github.com/SUKHPAL443/MAMBAPRO)\n"
**║┣⪼PyMAMBA     ┣⪼9.0.8,3.0\n"
**║┣⪼MAMBAMix    ┣⪼ 3.0\n"
**║╰━━━━━━━━━━━━━━━➣ \n"
**╔══❰🔥Ⲃⲟⲧ Ⲓⲛϝⲟʀⲙⲁⲧⲓⲟⲛ🔥❱═➣\n"
**║╭━━━━━━━━━━━━━━━➣ \n"
**║┣⪼Ⲟⲱⲛⲉʀ    ┣⪼   [SUKHI](t.me/SUKHI_MR_HACKER) \n"
**║┣⪼Ⲋⲧⲁⲧυⲋ     ┣⪼    Ⲟⲛⳑⲓⲛⲉ\n"
**┣⪼Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ ┣⪼  {mention}\n"
**║┣⪼Ⳙⲣⲧⲓⲙⲉ     ┣⪼  {uptime}\n"
**║┣⪼Ⲃⲟⲧ Ⲣⲓⲛⳋ   ┣⪼   290.087 \n"   
**║┣⪼DARKMAMBA    ┣⪼  {DARKMAMBAversion}\n"
**║┣⪼Os:  ┣⪼  [Kali GNU/Linux](https://pkg.kali.org/derivative/kali-roll/) \n"   
**║┣⪼Ⲧⲉⳑⲉⲧⲏⲟⲛ   ┣⪼  {version.__version__}\n" 
**║┣⪼[✨🐍DARKMAMBA┣⪼ 𝐔𝐬𝐞𝐫𝐛𝐨𝐭🐍✨](https://t.me/DARKMAMBA_SUPPORT)\n"
**║╰━━━━━━━━━━━━━━━➣ \n"
**╚══════════════════❍⊱❁۪۪\n"
"""
botname = Config.BOT_USERNAME

@bot.on(admin_cmd(pattern="alive$"))
@bot.on(admin_cmd(pattern="alive$", allow_sudo=True))
async def darkmamba_a(event):
    try:
        darkmamba = await bot.inline_query(botname, "alive")
        await darkmamba[0].click(event.chat_id)
        if event.sender_id == DARKMAMBA_SUPPORT:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)

CmdHelp("alive").add_command(
    'bot', None, 'υѕє αи∂ ѕєє'
).add_type(
    "Official"
).add()
