
# =======================================================
# JOIN REQUEST WELCOME
# =======================================================

from pyrogram import Client
from pyrogram.types import (
    ChatJoinRequest,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from pyrogram.errors import PeerIdInvalid, UserIsBlocked

from PurviMusic import app


PHOTO_URL = "https://graph.org/file/2b3018967643235f9a59f-6de55f5df207151c2b.jpg"


@app.on_chat_join_request()
async def welcome_join_request(client: Client, request: ChatJoinRequest):

    user = request.from_user
    chat = request.chat

    if not user:
        return

    caption = (
        f"<blockquote><b>💐 ʜᴇʏ {user.mention} 👋</b></blockquote>\n"
        f"<blockquote expandable><b>💮 ᴛʜᴀɴᴋs ғᴏʀ ʀᴇǫᴜᴇsᴛɪɴɢ ᴛᴏ ᴊᴏɪɴ {chat.title} 🎵</b>\n\n"
        f"<b>ɪ'ᴍ {app.mention} - ᴀ ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴍᴜsɪᴄ sᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs & ᴄʜᴀɴɴᴇʟs 🚀</b>\n\n"
        f"<b>📋 ᴊᴜsᴛ sᴇɴᴅ /start ᴛᴏ sᴇᴇ ʙᴏᴛ ᴍᴇɴᴜ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs 📋</b></blockquote>"
    )

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "➕ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                    url=f"https://t.me/{app.username}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    "🎁 ᴛᴀᴘ ᴛᴏ ᴄʟᴀɪᴍ ʏᴏᴜʀ sᴜʀᴘʀɪsᴇ 🎁",
                    url=f"https://t.me/{app.username}?start=start",
                )
            ],
            [
                InlineKeyboardButton(
                    "🛒 ʙᴜʏ ᴛɢ ᴀᴄᴄᴏᴜɴᴛ ғʀᴏᴍ ʜᴇʀᴇ",
                    url="https://t.me/AccountStoreTGbot",
                )
            ],
        ]
    )

    try:
        await client.send_photo(
            chat_id=user.id,
            photo=PHOTO_URL,
            caption=caption,
            reply_markup=keyboard,
            parse_mode="html",
        )

        try:
            await client.send_message(
                chat_id=user.id,
                text="/start",
            )

        except Exception as e:
            print(f"Failed to send /start to {user.id}: {e}")

    except (PeerIdInvalid, UserIsBlocked):
        pass

    except Exception as e:
        print(f"Join request welcome failed for {user.id}: {e}")


# =======================================================
