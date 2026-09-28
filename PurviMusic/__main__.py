# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

import asyncio
import importlib

from pytgcalls.exceptions import NoActiveGroupCall
from pyrogram import idle

import config
from PurviMusic import LOGGER, app, userbot
from PurviMusic.core.call import Purvi
from PurviMusic.misc import sudo
from PurviMusic.plugins import ALL_MODULES
from PurviMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "𝗦𝗧𝗥𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡 𝗡𝗢𝗧 𝗙𝗜𝗟𝗟𝗘𝗗 🙃, 𝗣𝗟𝗘𝗔𝗦𝗘 𝗙𝗜𝗟𝗟 𝗔 𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠 𝗦𝗘𝗦𝗦𝗜𝗢𝗡...🙂"
        )
        return

    await sudo()

    try:
        for user_id in await get_gbanned():
            BANNED_USERS.add(user_id)

        for user_id in await get_banned_users():
            BANNED_USERS.add(user_id)
    except:
        pass

    await app.start()

    for module in ALL_MODULES:
        importlib.import_module("PurviMusic.plugins" + module)

    LOGGER("PurviMusic.plugins").info(
        "𝗔𝗟𝗟 𝗣𝗟𝗨𝗚𝗜𝗡𝗦 𝗟𝗢𝗔𝗗𝗘𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬....🥳.."
    )

    await userbot.start()
    await Purvi.start()

    try:
        await Purvi.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("PurviMusic").error(
            "𝗣𝗟𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣/𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧... 😒\n\n𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........🤕"
        )

    await Purvi.decorators()

    LOGGER("PurviMusic").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎ 𝗠𝗔𝗗𝗘 𝗕𝗬 𝗣𝗨𝗥𝗩𝗜 𝗕𝗢𝗧𝗦 ☠︎︎ \n╚═════ஜ۩۞۩ஜ════╝"
    )

    await idle()

    await app.stop()
    await userbot.stop()

    LOGGER("PurviMusic").info("𝗦𝗧𝗢𝗣 𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧...🥹")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Hina-Music
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
