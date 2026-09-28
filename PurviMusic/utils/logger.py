# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from html import escape

from pyrogram.enums import ParseMode

from PurviMusic import app
from PurviMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} ᴘʟᴀʏ ʟᴏɢ</b>

<b>ᴄʜᴀᴛ ɪᴅ :</b> <code>{message.chat.id}</code>
<b>ᴄʜᴀᴛ ɴᴀᴍᴇ :</b> {message.chat.title}
<b>ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.chat.username}

<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>
<b>ɴᴀᴍᴇ :</b> {message.from_user.mention}
<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}

<b>ǫᴜᴇʀʏ :</b> {message.text.split(None, 1)[1]}
<b>sᴛʀᴇᴀᴍᴛʏᴘᴇ :</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return

async def autoplay_logs(chat_id, title, video_id, streamtype):
    if not await is_on_off(2):
        return
    if chat_id == LOGGER_ID:
        return

    chat_name = "ᴜɴᴋɴᴏᴡɴ"
    chat_username = None
    try:
        chat = await app.get_chat(chat_id)
        chat_name = chat.title or chat.first_name or chat_name
        chat_username = chat.username
    except Exception:
        pass

    username = f"@{chat_username}" if chat_username else "ɴ/ᴀ"
    logger_text = f"""
<b>{app.mention} ᴀᴜᴛᴏᴘʟᴀʏ ʟᴏɢ</b>

<b>ᴄʜᴀᴛ ɪᴅ :</b> <code>{chat_id}</code>
<b>ᴄʜᴀᴛ ɴᴀᴍᴇ :</b> {escape(str(chat_name))}
<b>ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ :</b> {username}

<b>sᴏɴɢ ᴛɪᴛʟᴇ :</b> {escape(str(title))}
<b>ᴠɪᴅᴇᴏ ɪᴅ :</b> <code>{video_id}</code>
<b>sᴛʀᴇᴀᴍᴛʏᴘᴇ :</b> {streamtype}"""
    try:
        await app.send_message(
            chat_id=LOGGER_ID,
            text=logger_text,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
        )
    except Exception:
        pass


# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Hina-Music
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
