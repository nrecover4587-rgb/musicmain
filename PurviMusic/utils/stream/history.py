# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

MAX_HISTORY = 30

_history = {}


def record_played(chat_id, video_id):
    if not video_id:
        return
    played = _history.setdefault(chat_id, [])
    if video_id in played:
        played.remove(video_id)
    played.append(video_id)
    if len(played) > MAX_HISTORY:
        del played[: len(played) - MAX_HISTORY]


def was_recently_played(chat_id, video_id) -> bool:
    return video_id in _history.get(chat_id, [])

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Hina-Music
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
