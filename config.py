import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = 16457832
API_HASH = "3030874d0befdb5d05597deacc3e83ab"
BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)
DB_NAME = getenv("DB_NAME", "Purvi")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 10000))

LOGGER_ID = -1003670305112
OWNER_ID = 8455283974

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/nrecover4587-rgb/musicbots")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", "")

SUPPORT_CHANNEL = "https://t.me/Mistubots"
SUPPORT_CHAT = "https://t.me/Mistubots"

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/x5lytj.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/leaexg.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/u5ux0j.jpg"
STATS_IMG_URL = "https://files.catbox.moe/97v75k.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/leaexg.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/leaexg.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/leaexg.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/leaexg.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/leaexg.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/leaexg.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/leaexg.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/leaexg.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://")

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit("[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://")
