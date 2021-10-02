# Neon Userbot

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ThisRelax 


@register(outgoing=True, pattern=r"^\.loqo(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit(
            "`Video yükləmək üçün link göndərin` **(._.)**"
        )
    else:
        await event.edit("```Loqo hazırlanır (bu proses biraz zaman ala bilər.....```")
    chat = "@BHLogobot"
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/gen")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            video = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error:** `Cavab ala bilmədim!`"
            )
            return
        await bot.send_file(event.chat_id, video)
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, r.id, msg.id, details.id, video.id]
        )
        await event.delete()

Help = CmdHelp('tiktok').add_command(
    'tt', None,'Surətli bir şəkildə loqo hazırlayın.'
).add()
