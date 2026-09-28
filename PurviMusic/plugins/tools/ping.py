# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup
from PurviMusic import app
from PurviMusic.core.call import Purvi
from PurviMusic.utils import bot_sys_stats
from PurviMusic.utils.inline.extras import botplaylist_markup
from PurviMusic.utils.decorators.language import language
from config import BANNED_USERS, PING_IMG_URL
import aiohttp
import asyncio

 
@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS & filters.group)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    start = datetime.now()
    pytgping = await Purvi.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit(
        _["ping_2"].format(
            resp,
            app.mention,
            UP,
            RAM,
            CPU,
            DISK,
            pytgping,
        ),
        reply_markup=InlineKeyboardMarkup(botplaylist_markup(_)),
        )

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Hina-Music
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
