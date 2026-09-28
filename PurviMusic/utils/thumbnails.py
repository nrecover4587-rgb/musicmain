# =======================================================
# ©️ 2026-27 All Rights Reserved by Purvi Bots (Im-Notcoder) 🚀

# This source code is under MIT License 📜 Unauthorized forking, importing, or using this code without giving proper credit will result in legal action ⚠️
 
# 📩 DM for permission : @TheSigmaCoder
# =======================================================

import os, random, aiofiles, aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from ytSearch import VideosSearch
from config import YOUTUBE_IMG_URL
from PurviMusic import app

CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)

ACCENT_COLORS = [
    (120, 140, 255),
    (255, 100, 190),
    (255, 210, 90),
    (255, 90, 90),
    (180, 120, 255),
]

def trim(text, font, max_w):
    if font.getlength(text) <= max_w:
        return text
    while font.getlength(text + "…") > max_w and text:
        text = text[:-1]
    return text + "…"

def draw_round_rect(img, xy, r, fill=None):
    x0, y0, x1, y1 = map(int, xy)
    if x1 <= x0 or y1 <= y0:
        return

    draw = ImageDraw.Draw(img)
    r = min(r, (x1 - x0) // 2, (y1 - y0) // 2)

    draw.rectangle((x0 + r, y0, x1 - r, y1), fill=fill)
    draw.rectangle((x0, y0 + r, x1, y1 - r), fill=fill)

    draw.pieslice((x0, y0, x0 + 2*r, y0 + 2*r), 180, 270, fill=fill)
    draw.pieslice((x1 - 2*r, y0, x1, y0 + 2*r), 270, 360, fill=fill)
    draw.pieslice((x0, y1 - 2*r, x0 + 2*r, y1), 90, 180, fill=fill)
    draw.pieslice((x1 - 2*r, y1 - 2*r, x1, y1), 0, 90, fill=fill)

async def get_thumb(videoid: str, player_username: str = None) -> str:
    if not player_username:
        player_username = app.username

    path = f"cache/{videoid}.png"
    temp = f"cache/{videoid}_temp.png"

    if os.path.isfile(path):
        return path

    try:
        vs = VideosSearch(f"https://www.youtube.com/watch?v={videoid}", limit=1)
        data = (await vs.next())["result"][0]
        title = data.get("title", "Unknown")
        thumb = data["thumbnails"][0]["url"]
        duration = data.get("duration", "LIVE")
        views = data.get("viewCount", {}).get("short", "0 views")
    except:
        title, thumb, duration, views = "Unknown", YOUTUBE_IMG_URL, "LIVE", "0 views"

    accent = random.choice(ACCENT_COLORS)

    try:
        async with aiohttp.ClientSession() as s:
            async with s.get(thumb) as r:
                if r.status != 200:
                    return None
                data = await r.read()
                if not data:
                    return None
                async with aiofiles.open(temp, "wb") as f:
                    await f.write(data)
    except:
        return None

    try:
        bg = Image.open(temp).resize((1280, 720)).convert("RGBA")
    except:
        if os.path.exists(temp):
            os.remove(temp)
        return None

    bg = bg.filter(ImageFilter.GaussianBlur(35))
    bg = ImageEnhance.Brightness(bg).enhance(0.35)
    draw = ImageDraw.Draw(bg)

    cx, cy = 90, 120
    cw, ch = 420, 420

    draw_round_rect(bg, (cx-8, cy-8, cx+cw+8, cy+ch+8), 50, fill=accent)
    draw_round_rect(bg, (cx, cy, cx+cw, cy+ch), 45, fill=(15, 15, 15))

    yt = Image.open(temp).resize((360, 360))
    bg.paste(yt, (cx+30, cy+30))

    try:
        title_f = ImageFont.truetype("PurviMusic/assets/f.ttf", 48)
        meta_f = ImageFont.truetype("PurviMusic/assets/font.ttf", 30)
        small_f = ImageFont.truetype("PurviMusic/assets/font.ttf", 26)
    except:
        title_f = meta_f = small_f = ImageFont.load_default()

    ix = cx + cw + 90

    label = "NOW PLAYING"
    pad_x, pad_y = 30, 12

    text_w = small_f.getlength(label)
    text_h = small_f.size

    draw_round_rect(bg, (ix, 160, ix + text_w + pad_x*2, 160 + text_h + pad_y*2), 30, fill=accent)
    draw.text((ix + pad_x, 160 + pad_y), label, font=small_f, fill=(0, 0, 0))

    title = trim(title, title_f, 620)
    draw.text((ix, 230), title, font=title_f, fill=(255,255,255))
    draw.line((ix, 295, ix+620, 295), fill=accent, width=4)

    draw.text((ix, 330), "Duration :", font=meta_f, fill=(200,200,200))
    draw.text((ix+160, 330), duration, font=meta_f, fill=accent)

    draw.text((ix, 375), "Views :", font=meta_f, fill=(200,200,200))
    draw.text((ix+160, 375), views, font=meta_f, fill=accent)

    draw.text((ix, 420), "Player :", font=meta_f, fill=(200,200,200))
    draw.text((ix+160, 420), f"@{player_username}", font=meta_f, fill=accent)

    bx, by, bw = ix, 490, 600
    draw.line((bx, by, bx+bw, by), fill=(170,170,170), width=6)
    draw.line((bx, by, bx+bw*0.45, by), fill=accent, width=6)

    draw.text((bx, by+18), "00:00", font=small_f, fill=(180,180,180))
    draw.text((bx+bw-55, by+18), duration, font=small_f, fill=(180,180,180))

    wm = "Dev :- @sexypym"
    w = small_f.getlength(wm)
    draw.text((1280-w-40, 680), wm, font=small_f, fill=(255, 255, 0))

    bg.save(path)

    if os.path.exists(temp):
        os.remove(temp)

    return path

# ======================================================
# ©️ 2025-26 All Rights Reserved by Purvi Bots (Im-Notcoder) 😎

# 🧑‍💻 Developer : t.me/TheSigmaCoder
# 🔗 Source link : GitHub.com/Im-Notcoder/Hina-Music
# 📢 Telegram channel : t.me/Purvi_Bots
# =======================================================
