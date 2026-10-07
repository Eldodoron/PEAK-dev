import os
from PIL import Image, ImageDraw, ImageFont

BRAIN_DIR = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568"
PREMIUM_DIR = os.path.join(BRAIN_DIR, "premium_emblems")
SCALING_DIR = os.path.join(BRAIN_DIR, "scaling_borders")
POSTER_PATH = os.path.join(BRAIN_DIR, "showcase_poster.png")

# Dimensions
WIDTH, HEIGHT = 1200, 960
canvas = Image.new("RGBA", (WIDTH, HEIGHT), (10, 14, 23, 255))
draw = ImageDraw.Draw(canvas)

# Background subtle grid pattern
for x in range(0, WIDTH, 40):
    draw.line([(x, 0), (x, HEIGHT)], fill=(16, 22, 36, 255), width=1)
for y in range(0, HEIGHT, 40):
    draw.line([(0, y), (WIDTH, y)], fill=(16, 22, 36, 255), width=1)

# Helper to scale 32x32 to NxN
def get_scaled(path, size=128):
    img = Image.open(path)
    return img.resize((size, size), Image.Resampling.NEAREST)

# Header banner
draw.rectangle([40, 30, WIDTH - 40, 100], fill=(15, 23, 42, 255), outline=(30, 41, 59, 255), width=2)
# Draw title text using basic PIL font or shapes
# Simple bitmap-style title
# We can load default font
try:
    font_large = ImageFont.truetype("arial.ttf", 26)
    font_mid = ImageFont.truetype("arial.ttf", 16)
    font_bold = ImageFont.truetype("arialbd.ttf", 16)
    font_small = ImageFont.truetype("arial.ttf", 13)
except:
    font_large = ImageFont.load_default()
    font_mid = ImageFont.load_default()
    font_bold = ImageFont.load_default()
    font_small = ImageFont.load_default()

draw.text((60, 42), "PEAK MODPACK - REWARD CACHE SHOWCASE", fill=(255, 255, 255, 255), font=font_large)
draw.text((60, 72), "Normalized 32x32 Pixel Art Architecture | Scaling Border Armor | High-Contrast Palettes", fill=(148, 163, 184, 255), font=font_mid)

# ==========================================
# ROW 1: THE 4 ARTISAN EMBLEMS (y: 120..360)
# ==========================================
draw.rectangle([40, 120, WIDTH - 40, 370], fill=(15, 23, 42, 220), outline=(30, 41, 59, 255), width=2)
draw.text((60, 135), "1. ARTISAN CATEGORY EMBLEMS (Center 16x16 Medallion Icons)", fill=(56, 189, 248, 255), font=font_bold)

emblems_data = [
    ("emblem_boss.png", "BOSS SLAYING", "Crowned Demon Skull", (239, 68, 68, 255), "Ivory horns, 3D cranium gleam, glowing red eyes, ruby crown"),
    ("emblem_weapons.png", "SIMPLY SWORDS", "Crossed Runic Blades", (6, 182, 212, 255), "Claymores with electric cyan runes, gold guards, clash burst"),
    ("emblem_culinary.png", "CULINARY", "Steaming Glazed Feast", (245, 158, 11, 255), "Honey-glazed roast, score marks, herb sprig, ethereal steam wisps"),
    ("emblem_pioneer.png", "PIONEER", "Ornate Brass Compass", (234, 179, 8, 255), "Polished brass casing, parchment dial, red/blue needle, pivot cap")
]

x_start = 65
spacing = 275
for i, (fname, cat, title, col, desc) in enumerate(emblems_data):
    x = x_start + i * spacing
    y = 165

    # Card background
    draw.rectangle([x, y, x + 250, y + 185], fill=(8, 12, 20, 255), outline=(40, 50, 70, 255), width=1)
    
    # Emblem image (100x100)
    emb_path = os.path.join(PREMIUM_DIR, fname)
    if os.path.exists(emb_path):
        emb_img = get_scaled(emb_path, 96)
        canvas.paste(emb_img, (x + 77, y + 12), emb_img)
    
    draw.text((x + 15, y + 115), cat, fill=col, font=font_bold)
    draw.text((x + 15, y + 135), title, fill=(255, 255, 255, 255), font=font_mid)
    # Short desc wrapped
    draw.text((x + 15, y + 158), desc[:38], fill=(148, 163, 184, 255), font=font_small)

# ==========================================
# ROW 2: THE 5 SCALING BORDER COFFERS (y: 390..660)
# ==========================================
draw.rectangle([40, 390, WIDTH - 40, 660], fill=(15, 23, 42, 220), outline=(30, 41, 59, 255), width=2)
draw.text((60, 405), "2. PROGRESSIVE SCALING BORDER ARMOR (Common -> Mythic Evolution)", fill=(168, 85, 247, 255), font=font_bold)

tiers_data = [
    ("coffer_common.png", "TIER 1 • COMMON", "Tin L-Brackets", (148, 163, 184, 255), "Minimal 3x3 flat corners, single rivets"),
    ("coffer_uncommon.png", "TIER 2 • UNCOMMON", "Bronze Plates", (74, 222, 128, 255), "Solid 5x5 reinforced plates, double rivets"),
    ("coffer_rare.png", "TIER 3 • RARE", "Cobalt Armor", (96, 165, 250, 255), "7x7 chamfered plates, side bands"),
    ("coffer_epic.png", "TIER 4 • EPIC", "Winged Filigree", (232, 121, 249, 255), "Silver bevels, neon magenta arches, crown"),
    ("coffer_mythic.png", "TIER 5 • MYTHIC", "Gilded Dragon Crown", (251, 191, 36, 255), "Flared corner spikes, 3-point crown, embers")
]

x_start_t = 60
spacing_t = 220
for i, (fname, tier, title, col, desc) in enumerate(tiers_data):
    x = x_start_t + i * spacing_t
    y = 435

    draw.rectangle([x, y, x + 205, y + 205], fill=(8, 12, 20, 255), outline=(40, 50, 70, 255), width=1)
    cof_path = os.path.join(SCALING_DIR, fname)
    if os.path.exists(cof_path):
        cof_img = get_scaled(cof_path, 110)
        canvas.paste(cof_img, (x + 47, y + 10), cof_img)

    draw.text((x + 12, y + 130), tier, fill=col, font=font_bold)
    draw.text((x + 12, y + 152), title, fill=(255, 255, 255, 255), font=font_mid)
    draw.text((x + 12, y + 175), desc[:30], fill=(148, 163, 184, 255), font=font_small)

# ==========================================
# ROW 3: FINAL COMPOSITE HIGHLIGHTS (y: 680..930)
# ==========================================
draw.rectangle([40, 680, WIDTH - 40, 940], fill=(15, 23, 42, 220), outline=(30, 41, 59, 255), width=2)
draw.text((60, 695), "3. FINAL COMPOSITE CACHES IN-GAME (Ready 32x32 Production Sprites)", fill=(245, 158, 11, 255), font=font_bold)

finals_data = [
    ("final_cache_boss_mythic.png", "APEX RELIQUARY", "Mythic Boss Cache", (251, 191, 36, 255)),
    ("final_cache_boss_epic.png", "CONQUEROR COFFER", "Epic Boss Spoils", (232, 121, 249, 255)),
    ("final_cache_weapons_rare.png", "RUNIC ARSENAL", "Rare Smithing Crate", (96, 165, 250, 255)),
    ("final_cache_culinary_epic.png", "MASTER BANQUET", "Epic Culinary Feast", (232, 121, 249, 255)),
    ("final_cache_pioneer_uncommon.png", "PIONEER KIT", "Uncommon Starter Pack", (74, 222, 128, 255))
]

for i, (fname, sub, title, col) in enumerate(finals_data):
    x = x_start_t + i * spacing_t
    y = 725

    draw.rectangle([x, y, x + 205, y + 195], fill=(8, 12, 20, 255), outline=(40, 50, 70, 255), width=1)
    fin_path = os.path.join(PREMIUM_DIR, fname)
    if os.path.exists(fin_path):
        fin_img = get_scaled(fin_path, 110)
        canvas.paste(fin_img, (x + 47, y + 10), fin_img)

    draw.text((x + 12, y + 130), sub, fill=col, font=font_bold)
    draw.text((x + 12, y + 152), title, fill=(255, 255, 255, 255), font=font_mid)
    draw.text((x + 12, y + 173), "32x32 Native KubeJS", fill=(100, 116, 139, 255), font=font_small)

canvas.save(POSTER_PATH)
print("Showcase poster successfully saved to:", POSTER_PATH)
