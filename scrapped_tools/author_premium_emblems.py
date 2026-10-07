import os
from PIL import Image, ImageDraw

OUTPUT_DIR = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568\premium_emblems"
SCALING_DIR = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568\scaling_borders"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_canvas():
    return Image.new("RGBA", (32, 32), (0, 0, 0, 0))

# -------------------------------------------------------------
# 1. BOSS CONQUEST: THE CROWNED DEMON SKULL
# Centered in socket: x 9..22, y 10..23 (14x14)
# -------------------------------------------------------------
def draw_emblem_boss():
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    # Palette
    bone_hi = (255, 255, 255, 255)
    bone_mid = (240, 235, 225, 255)
    bone_shad = (185, 175, 160, 255)
    bone_dark = (115, 100, 85, 255)
    bone_out = (45, 38, 30, 255)

    horn_hi = (245, 220, 170, 255)
    horn_mid = (195, 155, 100, 255)
    horn_dark = (120, 85, 45, 255)
    horn_out = (55, 35, 18, 255)

    gold_hi = (255, 245, 160, 255)
    gold_mid = (255, 195, 30, 255)
    gold_dark = (175, 115, 10, 255)

    eye_glow = (255, 40, 50, 255)
    eye_core = (255, 200, 180, 255)
    eye_deep = (70, 10, 15, 255)

    # --- HORNS ---
    # Left Horn sweeping outward and up
    draw.point((9, 11), horn_hi)
    draw.point((9, 12), horn_mid)
    draw.point((10, 12), horn_hi)
    draw.point((10, 13), horn_mid)
    draw.point((11, 13), horn_dark)
    draw.point((11, 14), horn_dark)
    draw.point((8, 11), horn_out)
    draw.point((8, 12), horn_out)
    draw.point((9, 13), horn_out)

    # Right Horn
    draw.point((22, 11), horn_hi)
    draw.point((22, 12), horn_mid)
    draw.point((21, 12), horn_mid)
    draw.point((21, 13), horn_dark)
    draw.point((20, 13), horn_dark)
    draw.point((20, 14), horn_dark)
    draw.point((23, 11), horn_out)
    draw.point((23, 12), horn_out)
    draw.point((22, 13), horn_out)

    # --- GOLDEN CROWN ON BROW (y: 10..12, x: 13..18) ---
    draw.line([(13, 12), (18, 12)], fill=gold_dark)
    draw.point((13, 11), gold_mid)
    draw.point((15, 10), gold_hi) # Center spike
    draw.point((16, 10), gold_hi)
    draw.point((18, 11), gold_mid)
    draw.point((14, 11), gold_hi)
    draw.point((17, 11), gold_mid)
    draw.point((15, 11), (255, 30, 60, 255)) # Crown Ruby gem!
    draw.point((16, 11), (255, 30, 60, 255))

    # --- SKULL CRANIUM (y: 13..16, x: 12..19) ---
    for y in range(13, 17):
        for x in range(13, 19):
            draw.point((x, y), bone_mid)
    # Highlights (top-left)
    draw.point((13, 13), bone_hi)
    draw.point((14, 13), bone_hi)
    draw.point((13, 14), bone_hi)
    draw.point((14, 14), bone_hi)
    # Shadows (bottom-right)
    draw.point((18, 13), bone_shad)
    draw.point((18, 14), bone_shad)
    draw.point((17, 16), bone_shad)
    draw.point((18, 16), bone_dark)

    # Outer cranium contour
    draw.line([(12, 14), (12, 16)], fill=bone_out)
    draw.line([(19, 14), (19, 16)], fill=bone_out)

    # --- EYE SOCKETS & GLOWING PUPILS ---
    # Left eye socket (13..14, 16)
    draw.point((13, 16), eye_deep)
    draw.point((14, 16), eye_glow)
    draw.point((14, 15), eye_deep)
    draw.point((14, 16), eye_core) # Pupil glint

    # Right eye socket (17..18, 16)
    draw.point((17, 16), eye_glow)
    draw.point((18, 16), eye_deep)
    draw.point((17, 15), eye_deep)
    draw.point((17, 16), eye_core)

    # Nasal cavity (15..16, 17)
    draw.point((15, 17), bone_dark)
    draw.point((16, 17), bone_out)

    # --- JAW & FANGED TEETH (y: 18..20, x: 13..18) ---
    draw.line([(13, 18), (18, 18)], fill=bone_dark) # Mouth seam
    # Top teeth
    draw.point((13, 18), bone_hi) # Left fang
    draw.point((14, 18), bone_mid)
    draw.point((15, 18), bone_hi)
    draw.point((16, 18), bone_mid)
    draw.point((17, 18), bone_hi)
    draw.point((18, 18), bone_shad) # Right fang

    # Lower jaw
    for x in range(14, 18):
        draw.point((x, 19), bone_mid if x < 16 else bone_shad)
    draw.line([(14, 20), (17, 20)], fill=bone_out) # Chin shadow
    draw.point((13, 19), bone_out)
    draw.point((18, 19), bone_out)

    return img

# -------------------------------------------------------------
# 2. SIMPLY SWORDS: CROSSED RUNIC BROADSWORDS
# Centered in socket: x 9..22, y 10..23 (14x14)
# -------------------------------------------------------------
def draw_emblem_weapons():
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    blade_hi = (255, 255, 255, 255)
    blade_light = (215, 235, 245, 255)
    blade_mid = (130, 170, 195, 255)
    blade_dark = (55, 90, 115, 255)
    blade_out = (25, 45, 60, 255)

    rune_glow = (0, 255, 255, 255)     # Cyan magic runic channel
    rune_core = (215, 255, 255, 255)

    gold_hi = (255, 245, 160, 255)
    gold_mid = (245, 185, 35, 255)
    gold_dark = (145, 95, 15, 255)
    ruby = (255, 30, 50, 255)

    # --- BLADE 1: Top-Left to Bottom-Right ---
    # Tip at (10, 11), Hilt at (21, 22)
    # Outer light edge
    draw.line([(10, 11), (19, 20)], fill=blade_hi)
    # Center runic fuller
    draw.line([(11, 12), (18, 19)], fill=rune_glow)
    draw.point((12, 13), rune_core)
    draw.point((14, 15), rune_core)
    # Dark edge & outline
    draw.line([(11, 10), (20, 19)], fill=blade_out)
    draw.line([(12, 13), (20, 21)], fill=blade_dark)

    # --- BLADE 2: Top-Right to Bottom-Left ---
    # Tip at (21, 11), Hilt at (10, 22)
    draw.line([(21, 11), (12, 20)], fill=blade_light)
    draw.line([(20, 12), (13, 19)], fill=rune_glow)
    draw.point((19, 13), rune_core)
    draw.point((17, 15), rune_core)
    draw.line([(21, 10), (12, 19)], fill=blade_out)
    draw.line([(20, 13), (12, 21)], fill=blade_dark)

    # --- INTERSECTION CLASH BURST (x: 15..16, y: 15..16) ---
    draw.point((15, 15), (255, 255, 255, 255))
    draw.point((16, 15), (255, 255, 255, 255))
    draw.point((15, 16), (255, 255, 255, 255))
    draw.point((16, 16), rune_core)

    # --- HILT 1 (Bottom-Right: x 19..22, y 20..23) ---
    # Gold Crossguard
    draw.point((18, 20), gold_hi)
    draw.point((19, 20), gold_mid)
    draw.point((20, 21), gold_dark)
    draw.point((21, 20), gold_mid)
    draw.point((20, 19), gold_hi)
    # Red Grip
    draw.point((20, 22), (180, 25, 25, 255))
    # Pommel & Ruby
    draw.point((21, 23), gold_mid)
    draw.point((21, 22), ruby)

    # --- HILT 2 (Bottom-Left: x 9..12, y 20..23) ---
    draw.point((13, 20), gold_hi)
    draw.point((12, 20), gold_mid)
    draw.point((11, 21), gold_dark)
    draw.point((10, 20), gold_mid)
    draw.point((11, 19), gold_hi)
    draw.point((11, 22), (180, 25, 25, 255))
    draw.point((10, 23), gold_mid)
    draw.point((10, 22), ruby)

    return img

# -------------------------------------------------------------
# 3. CULINARY: STEAMING ROASTED FEAST & GARNISH
# Centered in socket: x 9..22, y 10..23 (14x14)
# -------------------------------------------------------------
def draw_emblem_culinary():
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    meat_hi = (255, 230, 130, 255)     # Honey glaze specular
    meat_light = (245, 155, 25, 255)   # Golden roast
    meat_mid = (195, 85, 10, 255)      # Rich roasted mahogany
    meat_dark = (125, 45, 5, 255)      # Deep crust
    meat_out = (55, 20, 5, 255)        # Crisp edge contour

    bone_white = (255, 255, 255, 255)
    bone_shad = (185, 195, 205, 255)
    bone_dark = (100, 110, 120, 255)

    herb_hi = (125, 245, 40, 255)      # Fresh parsley sprig
    herb_dark = (35, 135, 25, 255)

    steam_bright = (255, 255, 255, 220)
    steam_soft = (210, 235, 255, 140)

    # --- ETHEREAL STEAM WISPS (y: 10..13) ---
    # Left curl
    draw.point((12, 13), steam_soft)
    draw.point((13, 12), steam_bright)
    draw.point((12, 11), steam_bright)
    draw.point((13, 10), steam_soft)

    # Right curl
    draw.point((17, 13), steam_soft)
    draw.point((16, 12), steam_bright)
    draw.point((17, 11), steam_bright)
    draw.point((16, 10), steam_soft)

    # --- PLATED CARVED MEAT (Ham / Roast Leg) (y: 14..20, x: 12..21) ---
    for y in range(15, 20):
        for x in range(13, 21):
            draw.point((x, y), meat_mid)

    # Roasted 3D Form & Glaze Highlights (top-left)
    draw.line([(14, 14), (19, 14)], fill=meat_light)
    draw.point((14, 15), meat_hi)
    draw.point((15, 15), meat_hi)
    draw.point((16, 15), meat_hi)
    draw.point((15, 16), meat_hi)
    draw.point((14, 16), meat_light)
    draw.point((16, 16), meat_light)

    # Caramelized Crosshatch Score Marks
    draw.line([(17, 15), (19, 17)], fill=meat_dark)
    draw.line([(18, 17), (20, 19)], fill=meat_dark)

    # Bottom Core Shadows
    draw.line([(14, 19), (20, 19)], fill=meat_dark)
    draw.line([(13, 20), (19, 20)], fill=meat_out)
    draw.line([(20, 15), (20, 19)], fill=meat_out)

    # --- PROTRUDING IVORY KNUCKLE BONE (Left side: x 9..12, y 16..18) ---
    draw.line([(10, 17), (13, 17)], fill=bone_white)
    draw.point((9, 16), bone_white)
    draw.point((9, 18), bone_white)
    draw.point((10, 16), bone_shad)
    draw.point((10, 18), bone_shad)
    draw.point((11, 18), bone_dark)
    draw.point((12, 18), bone_dark)

    # --- FRESH HERB GARNISH (Mint/Parsley at bottom right: x 19..22, y 19..21) ---
    draw.point((20, 20), herb_hi)
    draw.point((21, 19), herb_hi)
    draw.point((21, 20), herb_dark)
    draw.point((22, 20), herb_hi)
    draw.point((21, 21), herb_dark)

    return img

# -------------------------------------------------------------
# 4. PIONEER: ORNATE GILDED POCKET COMPASS
# Centered in socket: x 9..22, y 10..23 (14x14)
# -------------------------------------------------------------
def draw_emblem_pioneer():
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    brass_hi = (255, 250, 175, 255)
    brass_light = (255, 215, 65, 255)
    brass_mid = (215, 150, 20, 255)
    brass_dark = (130, 85, 10, 255)
    brass_out = (50, 30, 5, 255)

    dial_face = (245, 245, 240, 255)   # Parchment white dial
    dial_shad = (205, 210, 215, 255)

    red_hi = (255, 120, 120, 255)      # North needle
    red_mid = (225, 20, 20, 255)
    red_dark = (140, 10, 10, 255)

    blue_hi = (140, 215, 255, 255)     # South needle
    blue_mid = (20, 120, 215, 255)
    blue_dark = (5, 55, 125, 255)

    # --- TOP WATCH HANGING LOOP (x: 14..17, y: 10..11) ---
    draw.line([(15, 10), (16, 10)], fill=brass_hi)
    draw.point((14, 11), brass_mid)
    draw.point((17, 11), brass_dark)

    # --- CIRCULAR BRASS BEZEL (Outer Dia 12px, x: 10..21, y: 12..23) ---
    # Draw circular outer brass housing
    for y in range(13, 23):
        for x in range(11, 21):
            draw.point((x, y), dial_face)

    # Circular bevel outline
    draw.line([(13, 12), (18, 12)], fill=brass_hi) # Top rim highlight
    draw.line([(11, 14), (11, 21)], fill=brass_hi) # Left rim highlight
    draw.line([(20, 14), (20, 21)], fill=brass_dark) # Right rim shadow
    draw.line([(13, 23), (18, 23)], fill=brass_dark) # Bottom rim shadow

    # Corner roundings
    draw.point((12, 13), brass_hi)
    draw.point((19, 13), brass_light)
    draw.point((12, 22), brass_mid)
    draw.point((19, 22), brass_dark)

    # Dial shadow border
    for y in range(14, 22):
        draw.point((12, y), dial_shad)
        draw.point((19, y), dial_shad)
    draw.line([(13, 13), (18, 13)], fill=dial_shad)
    draw.line([(13, 22), (18, 22)], fill=dial_shad)

    # --- 4 CARDINAL TICK MARKS (N, S, E, W) ---
    draw.point((15, 14), (70, 75, 80, 255))
    draw.point((16, 14), (70, 75, 80, 255))
    draw.point((15, 21), (70, 75, 80, 255))
    draw.point((16, 21), (70, 75, 80, 255))
    draw.point((13, 17), (70, 75, 80, 255))
    draw.point((13, 18), (70, 75, 80, 255))
    draw.point((18, 17), (70, 75, 80, 255))
    draw.point((18, 18), (70, 75, 80, 255))

    # --- MAGNETIZED NEEDLE (Angled Dynamic Compass) ---
    # North Arrow (Pointing North-West)
    draw.point((14, 15), red_hi)
    draw.point((15, 15), red_mid)
    draw.point((14, 16), red_mid)
    draw.point((15, 16), red_dark)
    draw.point((13, 14), red_hi) # Sharp North tip!

    # South Arrow (Pointing South-East)
    draw.point((16, 18), blue_mid)
    draw.point((17, 18), blue_dark)
    draw.point((16, 19), blue_hi)
    draw.point((17, 19), blue_mid)
    draw.point((18, 20), blue_dark) # Sharp South tip!

    # Center Brass Pivot Cap (15..16, 17)
    draw.point((15, 17), brass_hi)
    draw.point((16, 17), brass_dark)
    draw.point((15, 18), brass_mid)

    return img

def scale_8x(img):
    return img.resize((img.width * 8, img.height * 8), Image.Resampling.NEAREST)

def composite(base_coffer, emblem):
    comp = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    comp.alpha_composite(base_coffer)
    comp.alpha_composite(emblem)
    return comp

def run():
    print("Generating Artisan Premium Emblems...")

    # Load the 5 Scaling Base Coffers (Common, Uncommon, Rare, Epic, Mythic)
    coffers = {}
    for tier in ["common", "uncommon", "rare", "epic", "mythic"]:
        coffer_path = os.path.join(SCALING_DIR, f"coffer_{tier}.png")
        coffers[tier] = Image.open(coffer_path)

    # 1. Author and save individual emblems
    emblems = {
        "boss": draw_emblem_boss(),
        "weapons": draw_emblem_weapons(),
        "culinary": draw_emblem_culinary(),
        "pioneer": draw_emblem_pioneer()
    }

    for name, img in emblems.items():
        img.save(os.path.join(OUTPUT_DIR, f"emblem_{name}.png"))
        scale_8x(img).save(os.path.join(OUTPUT_DIR, f"emblem_{name}_256.png"))
        print(f"Emblem generated: {name}")

    # 2. Composite all 20 final caches (4 categories x 5 tiers)
    for cat_name, emb_img in emblems.items():
        for tier_name, cof_img in coffers.items():
            final_sprite = composite(cof_img, emb_img)
            fname = f"final_cache_{cat_name}_{tier_name}"
            final_sprite.save(os.path.join(OUTPUT_DIR, f"{fname}.png"))
            scale_8x(final_sprite).save(os.path.join(OUTPUT_DIR, f"{fname}_256.png"))
            print(f"Composited: {fname}")

    print("All premium sprites successfully generated in:", OUTPUT_DIR)

if __name__ == "__main__":
    run()
