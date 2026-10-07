import os
from PIL import Image, ImageDraw, ImageFont

BRAIN_DIR = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568"
REDESIGN_DIR = os.path.join(BRAIN_DIR, "emblem_redesigns")
PREMIUM_DIR = os.path.join(BRAIN_DIR, "premium_emblems")
POSTER_PATH = os.path.join(BRAIN_DIR, "redesigns_poster.png")

WIDTH, HEIGHT = 1200, 1020
canvas = Image.new("RGBA", (WIDTH, HEIGHT), (10, 14, 23, 255))
draw = ImageDraw.Draw(canvas)

# Subtle grid
for x in range(0, WIDTH, 40):
    draw.line([(x, 0), (x, HEIGHT)], fill=(16, 22, 36, 255), width=1)
for y in range(0, HEIGHT, 40):
    draw.line([(0, y), (WIDTH, y)], fill=(16, 22, 36, 255), width=1)

def get_scaled(path, size=110):
    img = Image.open(path)
    return img.resize((size, size), Image.Resampling.NEAREST)

try:
    font_large = ImageFont.truetype("arial.ttf", 24)
    font_mid = ImageFont.truetype("arial.ttf", 15)
    font_bold = ImageFont.truetype("arialbd.ttf", 15)
    font_small = ImageFont.truetype("arial.ttf", 12)
except:
    font_large = ImageFont.load_default()
    font_mid = ImageFont.load_default()
    font_bold = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Header
draw.rectangle([40, 25, WIDTH - 40, 95], fill=(15, 23, 42, 255), outline=(30, 41, 59, 255), width=2)
draw.text((60, 37), "PEAK - EMBLEM REDESIGN CANDIDATES (Pick Your Favorites)", fill=(255, 255, 255, 255), font=font_large)
draw.text((60, 67), "Comparing New Boss & Pioneer Concepts + Simply Swords Touch-ups | Culinary Kept Approved", fill=(148, 163, 184, 255), font=font_mid)

# ==========================================
# ROW 1: BOSS SLAYING (2 New Options) + CULINARY (Approved)
# ==========================================
draw.rectangle([40, 115, WIDTH - 40, 395], fill=(15, 23, 42, 220), outline=(30, 41, 59, 255), width=2)
draw.text((60, 130), "1. BOSS SLAYING (Replacing old skull)  &  CULINARY (Your Approved Favorite)", fill=(239, 68, 68, 255), font=font_bold)

boss_cards = [
    ("comp_boss_v1_dragon_skull.png", "BOSS OPTION A", "Ancient Dragon Skull", (248, 113, 113, 255), "Elongated beast skull, sweeping obsidian horns, fanged maw, glowing red eye slits", REDESIGN_DIR),
    ("comp_boss_v2_void_eye.png", "BOSS OPTION B", "The Apex Void Eye", (192, 132, 252, 255), "Mesmerizing Cataclysm/Ender Eye with vertical pupil & obsidian talons (matches 12 Eyes!)", REDESIGN_DIR),
    ("final_cache_culinary_epic.png", "CULINARY (APPROVED)", "Steaming Glazed Roast", (251, 191, 36, 255), "Kept exactly as you liked it! Caramelized roast, bone, parsley sprig & steam wisps", PREMIUM_DIR)
]

x_start_1 = 65
spacing_1 = 365
for i, (fname, badge, title, col, desc, folder) in enumerate(boss_cards):
    x = x_start_1 + i * spacing_1
    y = 160
    draw.rectangle([x, y, x + 340, y + 215], fill=(8, 12, 20, 255), outline=(40, 50, 70, 255), width=1)
    
    img_path = os.path.join(folder, fname)
    if os.path.exists(img_path):
        scaled = get_scaled(img_path, 110)
        canvas.paste(scaled, (x + 115, y + 12), scaled)
        
    draw.text((x + 16, y + 135), badge, fill=col, font=font_bold)
    draw.text((x + 16, y + 155), title, fill=(255, 255, 255, 255), font=font_mid)
    draw.text((x + 16, y + 178), desc[:52], fill=(148, 163, 184, 255), font=font_small)
    draw.text((x + 16, y + 195), desc[52:105], fill=(148, 163, 184, 255), font=font_small)

# ==========================================
# ROW 2: PIONEER / STARTER (3 New Options)
# ==========================================
draw.rectangle([40, 415, WIDTH - 40, 705], fill=(15, 23, 42, 220), outline=(30, 41, 59, 255), width=2)
draw.text((60, 430), "2. PIONEER / STARTER REDESIGN CANDIDATES (Replacing old clock compass)", fill=(234, 179, 8, 255), font=font_bold)

pioneer_cards = [
    ("comp_pioneer_v1_pick_torch.png", "PIONEER OPTION A", "Pickaxe & Blazing Torch", (251, 191, 36, 255), "Crossed steel mining pick and flaming survival torch. Iconic Minecraft exploration feel!"),
    ("comp_pioneer_v2_backpack.png", "PIONEER OPTION B", "Explorer's Field Pack", (163, 230, 53, 255), "Leather adventurer's backpack with brass buckles and a rolled green sleeping bag on top."),
    ("comp_pioneer_v3_nautical_star.png", "PIONEER OPTION C", "Faceted Nautical Star", (56, 189, 248, 255), "Bold 3D gold compass star with diamond core. Crisp, clean emblem without cluttered dials.")
]

for i, (fname, badge, title, col, desc) in enumerate(pioneer_cards):
    x = x_start_1 + i * spacing_1
    y = 460
    draw.rectangle([x, y, x + 340, y + 225], fill=(8, 12, 20, 255), outline=(40, 50, 70, 255), width=1)
    
    img_path = os.path.join(REDESIGN_DIR, fname)
    if os.path.exists(img_path):
        scaled = get_scaled(img_path, 110)
        canvas.paste(scaled, (x + 115, y + 12), scaled)
        
    draw.text((x + 16, y + 135), badge, fill=col, font=font_bold)
    draw.text((x + 16, y + 155), title, fill=(255, 255, 255, 255), font=font_mid)
    draw.text((x + 16, y + 180), desc[:52], fill=(148, 163, 184, 255), font=font_small)
    draw.text((x + 16, y + 198), desc[52:105], fill=(148, 163, 184, 255), font=font_small)

# ==========================================
# ROW 3: SIMPLY SWORDS TOUCH-UPS (2 Options)
# ==========================================
draw.rectangle([40, 725, WIDTH - 40, 995], fill=(15, 23, 42, 220), outline=(30, 41, 59, 255), width=2)
draw.text((60, 740), "3. SIMPLY SWORDS TOUCH-UPS (Broad blades, thicker hilts, glowing runes)", fill=(6, 182, 212, 255), font=font_bold)

swords_cards = [
    ("comp_weapons_v1_heavy_claymores.png", "SWORDS TOUCH-UP A", "Broad Runic Claymores", (34, 211, 238, 255), "Double-thickness steel blades with electric cyan runic channels, prominent gold crossguards & ruby pommels."),
    ("comp_weapons_v2_anvil_blade.png", "SWORDS TOUCH-UP B", "Blade on Black Iron Anvil", (148, 163, 184, 255), "Heavy forge anvil with an imposing runic broadsword thrust down into it, sparking impact points.")
]

spacing_swords = 550
for i, (fname, badge, title, col, desc) in enumerate(swords_cards):
    x = 65 + i * spacing_swords
    y = 770
    draw.rectangle([x, y, x + 515, y + 205], fill=(8, 12, 20, 255), outline=(40, 50, 70, 255), width=1)
    
    img_path = os.path.join(REDESIGN_DIR, fname)
    if os.path.exists(img_path):
        scaled = get_scaled(img_path, 110)
        canvas.paste(scaled, (x + 202, y + 12), scaled)
        
    draw.text((x + 20, y + 135), badge, fill=col, font=font_bold)
    draw.text((x + 20, y + 155), title, fill=(255, 255, 255, 255), font=font_mid)
    draw.text((x + 20, y + 178), desc, fill=(148, 163, 184, 255), font=font_small)

canvas.save(POSTER_PATH)
print("Redesigns poster saved to:", POSTER_PATH)
