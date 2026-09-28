# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

import asyncio

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from PurviMusic import app
from PurviMusic.utils.database import get_served_users, get_served_chats
from config import OWNER_ID

IMAGE_URL = "https://files.catbox.moe/472piq.jpg"

MESSAGES = f"""**๏ ᴛʜɪs ɪꜱ <u>{app.mention}</u>

➻ ᴀ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ 🎧

▸ 𝐅ᴀꜱᴛ • ʟᴀɢ ꜰʀᴇᴇ • ɴᴏ ᴀᴅꜱ 🍃
▸ 𝐏ʟᴀʏʟɪꜱᴛ, ᴀᴜᴅɪᴏ, ᴠɪᴅᴇᴏ ᴘʟᴀʏ 🎥
────────────────────**"""


BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "⊚ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⊚",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ]
    ]
)


async def send_broadcast():
    users = await get_served_users()
    chats = await get_served_chats()

    user_count = len(users)
    chat_count = len(chats)

    total_sent = 0

    for user in users:
        user_id = int(user["user_id"])
        try:
            await app.send_photo(
                user_id,
                photo=IMAGE_URL,
                caption=MESSAGES,
                reply_markup=BUTTONS
            )
            total_sent += 1
            await asyncio.sleep(3)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except:
            pass

    for chat in chats:
        chat_id = int(chat["chat_id"])
        try:
            await app.send_photo(
                chat_id,
                photo=IMAGE_URL,
                caption=MESSAGES,
                reply_markup=BUTTONS
            )
            total_sent += 1
            await asyncio.sleep(3)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except:
            pass
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "ᴄʟᴏꜱᴇ",
                    callback_data="close"
                )
            ]
        ]
    )

    text = f"""**<u>✅ ᴀᴜᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴅᴏɴᴇ</u>**

**👤 ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ :** `{user_count}`
**👥 ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘꜱ :** `{chat_count}`
"""

    msg = await app.send_message(
        OWNER_ID,
        text,
        reply_markup=buttons
    )

    try:
        await msg.pin()
    except:
        pass


async def auto_broadcast():
    await asyncio.sleep(30)

    while True:
        try:
            await send_broadcast()
        except Exception as e:
            print(e)

        await asyncio.sleep(28800)


asyncio.get_event_loop().create_task(auto_broadcast())

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Hina-Music
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
