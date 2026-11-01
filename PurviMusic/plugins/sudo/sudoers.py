from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from PurviMusic import app
from PurviMusic.misc import SUDOERS
from PurviMusic.utils.database import add_sudo, remove_sudo
from PurviMusic.utils.decorators.language import language
from PurviMusic.utils.extraction import extract_user
from config import BANNED_USERS, OWNER_ID

PREFIXES = ["/", "!", "%", ",", "", ".", "@", "#"]
SUDO_PHOTO = "https://files.catbox.moe/fu6jk3.jpg"
SUDO_CAPTION = (
    "**» ᴄʜᴇᴄᴋ sᴜᴅᴏ ʟɪsᴛ ʙʏ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.**\n\n"
    "**» ɴᴏᴛᴇ:** ᴏɴʟʏ sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴠɪᴇᴡ."
)


def view_markup():
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("๏ ᴠɪᴇᴡ sᴜᴅᴏʟɪsᴛ ๏", callback_data="check_sudo_list")]]
    )


@app.on_message(filters.command(["addsudo"], prefixes=PREFIXES) & filters.user(OWNER_ID))
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if not user:
        return await message.reply_text(_["general_1"])
    if user.id in SUDOERS:
        return await message.reply_text(_["sudo_1"].format(user.mention))
    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(_["sudo_2"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(
    filters.command(["delsudo", "rmsudo"], prefixes=PREFIXES) & filters.user(OWNER_ID)
)
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if not user:
        return await message.reply_text(_["general_1"])
    if user.id not in SUDOERS:
        return await message.reply_text(_["sudo_3"].format(user.mention))
    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.discard(user.id)
        await message.reply_text(_["sudo_4"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(
    filters.command(["sudolist", "listsudo", "sudoers"], prefixes=PREFIXES)
    & ~BANNED_USERS
)
async def sudoers_list(client, message: Message):
    await message.reply_photo(
        photo=SUDO_PHOTO,
        caption=SUDO_CAPTION,
        reply_markup=view_markup(),
    )


@app.on_callback_query(filters.regex("^check_sudo_list$"))
async def check_sudo_list(client, callback_query: CallbackQuery):
    if callback_query.from_user.id not in SUDOERS:
        return await callback_query.answer(
            "ᴏɴʟʏ sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴠɪᴇᴡ ᴛʜɪs ʟɪsᴛ.", show_alert=True
        )

    try:
        owner = await app.get_users(OWNER_ID)
        owner_mention = owner.mention
    except Exception:
        owner_mention = f"`{OWNER_ID}`"

    caption = f"**˹ ʟɪsᴛ ᴏғ ʙᴏᴛ ᴍᴏᴅᴇʀᴀᴛᴏʀs ˼**\n\n**🌹 ᴏᴡɴᴇʀ** ➥ {owner_mention}\n\n"
    keyboard = [
        [InlineKeyboardButton("๏ ᴠɪᴇᴡ ᴏᴡɴᴇʀ ๏", url=f"tg://user?id={OWNER_ID}")]
    ]

    count = 1
    for user_id in SUDOERS:
        if user_id == OWNER_ID:
            continue
        try:
            sudo_user = await app.get_users(user_id)
            mention = sudo_user.mention
        except Exception:
            mention = f"`{user_id}`"
        caption += f"**🎁 sᴜᴅᴏ** {count} **»** {mention}\n"
        keyboard.append(
            [
                InlineKeyboardButton(
                    f"๏ ᴠɪᴇᴡ sᴜᴅᴏ {count} ๏",
                    url=f"tg://user?id={user_id}",
                )
            ]
        )
        count += 1

    keyboard.append([InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="back_to_main_menu")])
    await callback_query.message.edit_caption(
        caption=caption,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


@app.on_callback_query(filters.regex("^back_to_main_menu$"))
async def back_to_main_menu(client, callback_query: CallbackQuery):
    if callback_query.from_user.id not in SUDOERS:
        return await callback_query.answer(
            "ᴏɴʟʏ sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs.", show_alert=True
        )
    await callback_query.message.edit_caption(
        caption=SUDO_CAPTION,
        reply_markup=view_markup(),
    )


@app.on_message(
    filters.command(["delallsudo"], prefixes=PREFIXES) & filters.user(OWNER_ID)
)
@language
async def del_all_sudo(client, message: Message, _):
    count = 0
    for user_id in list(SUDOERS):
        if user_id == OWNER_ID:
            continue
        removed = await remove_sudo(user_id)
        if removed:
            SUDOERS.discard(user_id)
            count += 1
    await message.reply_text(f"**» ʀᴇᴍᴏᴠᴇᴅ** `{count}` **ᴜsᴇʀs ғʀᴏᴍ sᴜᴅᴏʟɪsᴛ.**")
