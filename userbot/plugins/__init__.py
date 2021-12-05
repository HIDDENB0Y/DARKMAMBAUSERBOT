from userbot import *
from userbot.utils import *
from userbot.Config import Config
from userbot.cmdhelp import CmdHelp
import datetime
from telethon import version
from . import *
DARKMAMBA_USER = bot.me.first_name
SUKHI_MR_HACKER = bot.uid
darkmamba_mention = f"[{DARKMAMBA_USER}](tg://user?id={SUKHI_MR_HACKER})"
DARKMAMBA_logo = "./userbot/resources/pics/-6163428037589314866_121.jpg"
DARKMAMBA_logo1 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
DARKMAMBA_logo2 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
DARKMAMBA_logo4 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
DARKMAMBA_logo3 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
DARKMAMBAversion = "𝚅9.𝙾.8"

perf = "[ DARKMAMBA ]"
#Developer here list
DEVLIST = [
    "2034973894"
    "2129450671"
]
async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

l1 = Config.COMMAND_HAND_LER
l2 = Config.SUDO_COMMAND_HAND_LER
#sudo explained 
sudos = Config.SUDO_USERS
if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"

START_TIME = datetime.datetime.now()
uptime = f"{str(datetime.datetime.now() - START_TIME).split('.')[0]}"
my_channel = Config.YOUR_CHANNEL or "DARKMAMBA_UPDATES"
my_group = Config.YOUR_GROUP or "DARKMAMBA_UPDATES"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")


mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"

chnl_link = "https://t.me/DARKMAMBA_UPDATES"
darkmamba_channel = f"[🍡  🎀  𝒟𝒜𝑅𝒦𝑀𝒜𝑀𝐵𝒜  🎀  🍡]({chnl_link})"
grp_link = "https://t.me/DARKMAMBA_SUPPORT"
darkmamba_grp = f"[𝒟𝒜𝑅𝒦𝑀𝒜𝑀𝐵𝒜 Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
