# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from PurviMusic import app
from PurviMusic.misc import SUDOERS
from PurviMusic.utils.database import (
    autoplay_off,
    autoplay_on,
    get_authuser_names,
    is_autoplay,
    is_maintenance,
    is_nonadmin_chat,
)
from PurviMusic.utils.formatters import int_to_alpha
from PurviMusic.utils.inline.play import autoplay_markup
from config import BANNED_USERS, adminlist

ONLY_ADMINS_TEXT = "❖ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴍᴀɴᴀɢᴇ ᴀᴜᴛᴏᴘʟᴀʏ !!"
MAINTENANCE_TEXT = "❖ ʙᴏᴛ ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, ᴘʟᴇᴀsᴇ ᴛʀʏ ʟᴀᴛᴇʀ."


async def _can_manage(chat_id: int, user_id: int) -> bool:
 
    if await is_nonadmin_chat(chat_id):
        return True
    if user_id in SUDOERS:
        return True
    admins = adminlist.get(chat_id)
    if admins and user_id in admins:
        return True
    try:
        member = await app.get_chat_member(chat_id, user_id)
        if member.status in (ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR):
            return True
    except Exception:
        pass
    try:
        token = await int_to_alpha(user_id)
        if token in await get_authuser_names(chat_id):
            return True
    except Exception:
        pass
    return False


async def _under_maintenance(user_id: int) -> bool:
    return await is_maintenance() is False and user_id not in SUDOERS


@app.on_message(
    filters.command(["autoplay"], prefixes=["/", "!", ".", "#"])
    & filters.group
    & ~BANNED_USERS
)
async def autoplay_command(client, message: Message):
    if not message.from_user:
        return

    chat_id = message.chat.id
    chat_title = message.chat.title

    if await _under_maintenance(message.from_user.id):
        return await message.reply_text(MAINTENANCE_TEXT)

    if not await _can_manage(chat_id, message.from_user.id):
        return await message.reply_text(ONLY_ADMINS_TEXT)

    current = await is_autoplay(chat_id)
    status = "ᴇɴᴀʙʟᴇᴅ 🟢" if current else "ᴅɪsᴀʙʟᴇᴅ 🔴"

    caption = (
        "<b><u>❖ ᴀᴜᴛᴏ ᴘʟᴀʏ sᴇᴛᴛɪɴɢ ᴘᴀɴᴇʟ</u></b>\n\n"
        f"<b>🏵️ ɪᴅ :</b> <code>{chat_id}</code>\n"
        f"<b>🍂 sᴛᴀᴛᴜs :</b> {status}\n"
        f"<b>🏖️ ɢʀᴏᴜᴘ :</b> {chat_title}\n\n"
        "<b>❏ ᴛᴀᴘ ᴀ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ᴄʜᴀɴɢᴇ ᴀᴜᴛᴏᴘʟᴀʏ sᴇᴛᴛɪɴɢ.</b>"
    )

    buttons = [
        [
            InlineKeyboardButton(
                "🟢 ᴇɴᴀʙʟᴇ", callback_data=f"AutoPlaySet|enable|{chat_id}"
            ),
            InlineKeyboardButton(
                "🔴 ᴅɪsᴀʙʟᴇ", callback_data=f"AutoPlaySet|disable|{chat_id}"
            ),
        ],
        [InlineKeyboardButton("⌯ ᴄʟᴏsᴇ ⌯", callback_data="close")],
    ]

    await message.reply_text(caption, reply_markup=InlineKeyboardMarkup(buttons))


@app.on_callback_query(filters.regex(r"^AutoPlaySet") & ~BANNED_USERS)
async def autoplay_set_callback(client, CallbackQuery):
    user = CallbackQuery.from_user

    if await _under_maintenance(user.id):
        return await CallbackQuery.answer(MAINTENANCE_TEXT, show_alert=True)

    try:
        _, action, raw_chat_id = CallbackQuery.data.split("|")
        chat_id = int(raw_chat_id)
    except Exception:
        return await CallbackQuery.answer()

    if not await _can_manage(chat_id, user.id):
        return await CallbackQuery.answer(ONLY_ADMINS_TEXT, show_alert=True)

    chat_title = CallbackQuery.message.chat.title

    if action == "enable":
        await autoplay_on(chat_id)
        text = (
            f"<b>🟢 ᴀᴜᴛᴏᴘʟᴀʏ sᴇᴛᴛɪɴɢ ᴇɴᴀʙʟᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ʙʏ : {user.mention} ɪɴ {chat_title}</b>"
        )
    else:
        await autoplay_off(chat_id)
        text = (
            f"<b>🔴 ᴀᴜᴛᴏᴘʟᴀʏ sᴇᴛᴛɪɴɢ ᴅɪsᴀʙʟᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ʙʏ : {user.mention} ɪɴ {chat_title}</b>"
        )

    await CallbackQuery.message.edit_text(text)


@app.on_callback_query(filters.regex(r"^autoplay ") & ~BANNED_USERS)
async def autoplay_toggle_callback(client, CallbackQuery):
    
    user = CallbackQuery.from_user

    if await _under_maintenance(user.id):
        return await CallbackQuery.answer(MAINTENANCE_TEXT, show_alert=True)

    try:
        chat_id = int(CallbackQuery.data.split(None, 1)[1])
    except Exception:
        return await CallbackQuery.answer()


    if not await _can_manage(CallbackQuery.message.chat.id, user.id):
        return await CallbackQuery.answer(ONLY_ADMINS_TEXT, show_alert=True)

    if await is_autoplay(chat_id):
        await autoplay_off(chat_id)
        new_mode = False
        toast = "🔴 ᴀᴜᴛᴏᴘʟᴀʏ ᴅɪsᴀʙʟᴇᴅ"
    else:
        await autoplay_on(chat_id)
        new_mode = True
        toast = "🟢 ᴀᴜᴛᴏᴘʟᴀʏ ᴇɴᴀʙʟᴇᴅ"

    try:
        await CallbackQuery.answer(toast, show_alert=False)
    except Exception:
        pass

    markup = CallbackQuery.message.reply_markup
    if not markup:
        return

    rows = []
    for row in markup.inline_keyboard:
        new_row = []
        for button in row:
            if button.callback_data and button.callback_data.startswith("autoplay "):
                new_row.extend(autoplay_markup(chat_id, new_mode))
            else:
                new_row.append(button)
        rows.append(new_row)

    try:
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(rows)
        )
    except Exception:
        pass

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Hina-Music
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
