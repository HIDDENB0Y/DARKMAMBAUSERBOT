from userbot import bot, CMD_HELP, ALIVE_NAME
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from DARKMAMBA.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp
import html
from telethon import events
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from telethon.events import ChatAction
from . import *

SUKHI_MR_HACKER= str(ALIVE_NAME) if ALIVE_NAME else "DARKMAMBA User"
papa = borg.uid


async def get_full_user(event):  
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await edit_or_reply(event, "**Som3thing W3nt Wr0ng**\n`Can you please provide me a user id`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await edit_or_reply(event, "**Som3thing W3nt Wr0ng**\n", str(err))           
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await edit_or_reply(event, str(err))
        return None
    return user_obj

@bot.on(admin_cmd(pattern="gban ?(.*)"))
@bot.on(sudo_cmd(pattern="gban ?(.*)", allow_sudo=True))
async def gban(userbot):
    if userbot.fwd_from:
        return
    ids = userbot
    sender = await ids.get_sender()
    hum = await ids.client.get_me()
    if not sender.id == hum.id:
        PYTHONBOT = await edit_or_reply(ids, "Trying to gban this retard!")
    else:
        PYTHONBOT = await edit_or_reply(ids, "`🐼  🎀  𝒜𝐵𝐸 𝒴𝒜𝒜𝑅 𝒦𝐸𝒮𝐸 𝒞𝐻𝒰𝒯𝐼𝒴𝒜 𝐼𝒩𝒮𝒜𝒜𝒩 𝒦☯ 𝒢𝐵𝒜𝒩 𝒦𝑅𝒩𝒜 𝒫𝒟𝒟 𝑅𝐻𝒜 𝐻𝒜𝐼. 𝑅𝒰𝒦𝒥𝒜𝒜 𝒴𝒜𝒜𝑅 𝒮𝒜𝐵𝒜𝑅 𝑅𝒦𝐻 𝒢𝐵𝒜𝒩 𝐻❤𝒩𝐸 𝒟𝐸  🎀  🐼
`")
    hum = await userbot.client.get_me()
    await DARKMAMBA.edit(f"`🔥🐙  🎀  𝐿𝐸 𝐵𝐻𝒜𝐼 𝒟𝐸𝒦𝐻𝒯𝒜 𝒥𝒜𝒜 𝒦𝐼𝒯𝒩𝐸 𝑀𝐸 𝒮𝐸 𝒢𝐵𝒜𝒩 𝒥𝒜𝒴𝐸𝒢𝒜  🎀🐙😎 `")
    my_mention = "[{}](tg://user?id={})".format(hum.first_name, hum.id)
    f"@{hum.username}" if hum.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await DARKMAMBA.edit(f"**🐹  🎀  𝐵𝐻𝒜𝐼 𝒦𝒰𝒞𝐻 𝒢𝒜𝒟𝐵𝒜𝒟 𝐻𝒜𝐼  🎀  🐹**")
    if user:
        if user.id == 1938996006:
            return await DARKMAMBA.edit(
                f"`How dare u trying to Gban my master`"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except:
            pass
        try:
            await userbot.client(BlockRequest(user))
        except:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await DARKMAMBA.edit(f"𝓛𝓔 𝓑𝓔𝓣𝓐 𝓤𝓢𝓚𝓘 𝓖𝓐𝓝𝓓 𝓜𝓔 𝓖𝓑𝓐𝓝 𝓓𝓐𝓐𝓛 𝓡𝓗𝓐 𝓗𝓤 😂\n\nTotal Chats :- `{a}`")
            except:
                b += 1
    else:
        await DARKMAMBA.edit(f"`Either reply to a user or gib me user id/name`")
    try:
        if gmute(user.id) is False:
            return await DARKMAMBA.edit(f"**Error! User phle se chuda(Gbanned) pda h 😂 .**")
    except:
        pass
    return await DARKMAMBA.edit(
        f"[{user.first_name}](tg://user?id={user.id}) \n\n**•°¯`••   🎀  𝒢𝐵𝒜𝒩 𝐻💍 𝒢𝒴𝒜 𝒴𝐸 𝐵𝐸𝒯𝒜  🎀   ••`¯°•🔥\nAffected Chats😏 : {a} **"
    )

@bot.on(admin_cmd(pattern="ungban ?(.*)"))
@bot.on(sudo_cmd(pattern="ungban ?(.*)", allow_sudo=True))
async def gunban(userbot):
    if userbot.fwd_from:
        return
    ids = userbot
    sender = await ids.get_sender()
    hum = await ids.client.get_me()
    if not sender.id == hum.id:
        DARKMAMBA = await edit_or_reply(ids, "`UNGBAN KRNE KA TRY KAR RHA HU...`")
    else:
        DARKMAMBA = await edit_or_reply(ids, "`UNGBAN HO RHA HAI SABAR RKH BETA...`")
    hum = await userbot.client.get_me()
    await DARKMAMBA.edit(f"`UNGBAN KRNE KA TRY KAR RHA HU...`")
    my_mention = "[{}](tg://user?id={})".format(hum.first_name, hum.id)
    f"@{hum.username}" if hum.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await DARKMAMBA.edit("**YE INSAAN PAIDA HI GALAT HUWA HAI TOO ISKI ID KAHA SE SAHI HOGI**")
    if user:
        if user.id == DARKMAMBA:
            return await DARKMAMBA.edit("**You need to grow some balls to gban / ungban my creator**")
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except:
            pass
        try:
            await userbot.client(UnblockRequest(user))
        except:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await DARKMAMBA.edit(f"Ok! Now ABE OO PHLE TOO BAAP SE JEETA NHI JB GBAN DE DIYA TOO UNGBAN KRVAANE KE LIYE MERE LUND KO CHAAT RHA HAI.\nChats:- `{a}`")
            except:
                b += 1
    else:
        await DARKMAMBA.edit("**Reply to a user**")
    try:
        if ungmute(user.id) is False:
            return await DARKMAMBA.edit("**Error! ISKO PHLE SE HI CHOD DIYA BINA CONDOM KE.**")
    except:
        pass
    return await DARKMAMBA.edit(
        f"**[{user.first_name}](tg://user?id={user.id}) Purani Baate bhul jaa... ab Friend ban ja 😂.**\n\nUngban Successful 🔥\nChats :- `{a}`"
    )




@borg.on(ChatAction)
async def handler(legend): 
   if DARKMAMBA.user_joined or DARKMAMBA.user_added:      
       try:       	
         from userbot.plugins.sql_helper.gmute_sql import is_gmuted
         guser = await DARKMAMBA.get_user()      
         gmuted = is_gmuted(guser.id)             
       except:      
          return
       if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):                                                                         
                chat = await DARKMAMBA.get_chat()
                admin = chat.admin_rights
                creator = chat.creator   
                if admin or creator:
                 try:
                    await client.edit_permissions(python.chat_id, guser.id, view_messages=False)                              
                    await DARKMAMBA.reply(
                     f"⚠️⚠️**Warning**⚠️⚠️\n\n`Gbanned User Joined the chat!!`\n"                      
                     f"**🔥 Victim Id 🔥**:\n[{guser.id}](tg://user?id={guser.id})\n"                   
                     f"**🔥 Action 🔥**  :\n`Banned this piece of shit....` **AGAIN!**")                                                
                 except:       
                    DARKMAMBA.reply("`Sheit!! No permission to ban users.\n@admins ban this retard.\nGlobally Banned User And A Potential Spammer`\n**Make your group a safe place by cleaning this shit**")                   
                    return
                  
                  
CmdHelp("gban").add_command(
  'gban', '<reply> / <userid> / <username>', 'Gbans the targeted user and adds to gban watch list'
).add_command(
  'ungban', '<reply> / <userid> / <username>', 'Unbans the targeted user and removes them from gban watch list. Grants another Chance'
).add_command(
  'gmute', '<reply>/ <userid>/ <username>', 'Gmutes the targeted user. Works only if you have delete msg permission. (Works on admins too)'
).add_command(
  'ungmute', '<reply>/ <userid>/ <username>', 'Ungmutes the user. Now targeted user is free'
).add()
