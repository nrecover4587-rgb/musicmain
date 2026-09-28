# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from pyrogram import Client
from pyrogram.types import (
    ChatJoinRequest,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from pyrogram.errors import PeerIdInvalid, UserIsBlocked

import config
from PurviMusic import app


@app.on_chat_join_request()
async def welcome_join_request(client: Client, request: ChatJoinRequest):
    user = request.from_user
    chat = request.chat

    if not user:
        return
      
    photo_url = "https://files.catbox.moe/472piq.jpg" 

    caption = (
        f"**𝖧𝖾𝗒 {user.mention} 👋**\n"
        f"**𝖳𝗁𝖺𝗇𝗄𝗌 𝖥𝗈𝗋 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝗂𝗇𝗀 𝖳𝗈 𝖩𝗈𝗂𝗇 {chat.title} 🎵**\n\n"
        f"**𝖨'𝗆 {app.mention} - 𝖠 𝖧𝗂𝗀𝗁 𝖰𝗎𝖺𝗅𝗂𝗍𝗒 𝖬𝗎𝗌𝗂𝖼 𝖲𝗍𝗋𝖾𝖺𝗆𝗂𝗇𝗀 𝖡𝗈𝗍 𝖥𝗈𝗋 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖦𝗋𝗈𝗎𝗉𝗌 & 𝖢𝗁𝖺𝗇𝗇𝖾𝗅𝗌 🚀**\n\n"
        f"**𝖩𝗎𝗌𝗍 𝖲𝖾𝗇𝖽 /start 𝖳𝗈 𝖲𝖾𝖾 𝖡𝗈𝗍 𝖬𝖾𝗇𝗎 𝖠𝗇𝖽 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 📋**"
    )

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "➕ 𝖠𝖽𝖽 𝖬𝖾 𝖨𝗇 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉",
                    url=f"https://t.me/{app.username}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    "💬 𝖲𝗎𝗉𝗉𝗈𝗋𝗍",
                    url="https://t.me/Purvi_Bots", 
                ),
                InlineKeyboardButton(
                    "📢 𝖴𝗉𝖽𝖺𝗍𝖾𝗌",
                    url="https://t.me/Purvi_Updates",
                ),
            ],
        ]
    )

    try:
      
        await client.send_photo(
            user.id,
            photo=photo_url,
            caption=caption,
            reply_markup=keyboard,
        )
    except (PeerIdInvalid, UserIsBlocked):
        pass
    except Exception:
        pass

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Hina-Music
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
