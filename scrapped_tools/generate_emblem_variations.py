import os
from PIL import Image, ImageDraw, ImageFont

BRAIN_DIR = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568"
SCALING_DIR = os.path.join(BRAIN_DIR, "scaling_borders")
OUT_DIR = os.path.join(BRAIN_DIR, "emblem_redesigns")
os.makedirs(OUT_DIR, exist_ok=True)

def create_canvas():
    return Image.new("RGBA", (32, 32), (0, 0, 0, 0))

# =============================================================
# BOSS VARIATIONS
# =============================================================

# Boss Var 1: Menacing Dragon / Apex Beast Skull (Elongated, massive horns, fanged maw)
def draw_boss_dragon_skull():
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    bone_hi = (255, 255, 255, 255)
    bone_mid = (235, 225, 210, 255)
    bone_shad = (165, 150, 130, 255)
    bone_dark = (95, 80, 65, 255)
    bone_out = (35, 28, 22, 255)

    horn_hi = (210, 190, 225, 255)     # Obsidian/Draconic horn
    horn_mid = (130, 100, 145, 255)
    horn_dark = (70, 45, 85, 255)
    horn_out = (30, 15, 40, 255)

    glow_red = (255, 30, 40, 255)
    glow_core = (255, 200, 200, 255)

    # Sweeping dragon horns (Upper outer edges)
    # Left Horn: sweeping up & back (x: 8..12, y: 8..13)
    draw.line([(8, 9), (10, 11)], fill=horn_hi)
    draw.line([(9, 9), (11, 12)], fill=horn_mid)
    draw.line([(8, 8), (8, 10)], fill=horn_out)
    draw.line([(9, 11), (12, 13)], fill=horn_dark)

    # Right Horn: (x: 19..23, y: 8..13)
    draw.line([(23, 9), (21, 11)], fill=horn_hi)
    draw.line([(22, 9), (20, 12)], fill=horn_mid)
    draw.line([(23, 8), (23, 10)], fill=horn_out)
    draw.line([(22, 11), (19, 13)], fill=horn_dark)

    # Heavy Brow Ridge (x: 12..19, y: 12..13)
    draw.line([(12, 13), (19, 13)], fill=bone_mid)
    draw.line([(13, 12), (18, 12)], fill=bone_hi)
    draw.point((11, 13), bone_dark)
    draw.point((20, 13), bone_dark)

    # Cranium (y: 10..12, x: 13..18)
    for y in range(10, 13):
        for x in range(14, 18):
            draw.point((x, y), bone_mid if y > 10 else bone_hi)

    # Deep Angled Eye Slits (x: 13..14, 17..18, y: 14..15)
    draw.point((13, 14), (20, 5, 5, 255))
    draw.point((14, 14), glow_core) # Left pupil
    draw.point((14, 15), glow_red)
    draw.point((18, 14), (20, 5, 5, 255))
    draw.point((17, 14), glow_core) # Right pupil
    draw.point((17, 15), glow_red)

    # Snout / Nasal Bridge (x: 14..17, y: 14..17)
    for y in range(14, 18):
        draw.point((15, y), bone_hi)
        draw.point((16, y), bone_shad)
    draw.point((15, 17), bone_dark) # Nostril
    draw.point((16, 17), bone_dark)

    # Upper Fanged Jaw (y: 18..19, x: 12..19)
    draw.line([(12, 18), (19, 18)], fill=bone_mid)
    # Long menacing fangs
    draw.point((12, 19), bone_hi) # Left long fang
    draw.point((12, 20), bone_hi)
    draw.point((13, 19), bone_mid)
    draw.point((18, 19), bone_shad)
    draw.point((19, 19), bone_hi) # Right long fang
    draw.point((19, 20), bone_shad)

    # Dark Maw Cavity
    draw.line([(14, 19), (17, 19)], fill=(20, 10, 10, 255))

    # Lower Jaw / Chin (y: 20..22, x: 13..18)
    draw.point((14, 20), bone_hi) # Lower teeth
    draw.point((17, 20), bone_shad)
    draw.line([(14, 21), (17, 21)], fill=bone_mid)
    draw.line([(14, 22), (17, 22)], fill=bone_dark)
    draw.point((13, 21), bone_out)
    draw.point((18, 21), bone_out)

    return img

# Boss Var 2: The Apex Void Eye (Cataclysm / Ender Eye Talisman)
def draw_boss_void_eye():
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    obs_hi = (110, 100, 130, 255)
    obs_mid = (60, 50, 75, 255)
    obs_dark = (30, 22, 40, 255)
    obs_out = (12, 8, 16, 255)

    cyan_hi = (220, 255, 255, 255)
    cyan_mid = (0, 230, 255, 255)
    cyan_dark = (0, 130, 180, 255)

    purp_mid = (185, 45, 255, 255)
    purp_dark = (95, 15, 145, 255)
    pupil = (10, 0, 15, 255)

    # 4 Curved Obsidian Talons clasping the eye (x 9..22, y 10..23)
    # Top talons
    draw.point((15, 10), obs_hi)
    draw.point((16, 10), obs_hi)
    draw.point((14, 11), obs_mid)
    draw.point((17, 11), obs_dark)
    # Bottom talons
    draw.point((15, 23), obs_dark)
    draw.point((16, 23), obs_dark)
    draw.point((14, 22), obs_mid)
    draw.point((17, 22), obs_dark)
    # Left talons
    draw.point((9, 16), obs_hi)
    draw.point((9, 17), obs_mid)
    draw.point((10, 15), obs_hi)
    draw.point((10, 18), obs_dark)
    # Right talons
    draw.point((22, 16), obs_dark)
    draw.point((22, 17), obs_dark)
    draw.point((21, 15), obs_mid)
    draw.point((21, 18), obs_dark)

    # Eye Sclera / Slit Orb (x 11..20, y 12..21)
    for y in range(13, 21):
        for x in range(12, 20):
            draw.point((x, y), purp_dark)

    # Swirling Vibrant Iris
    for y in range(14, 20):
        for x in range(13, 19):
            draw.point((x, y), purp_mid)

    # Electric Cyan Inner Ring
    draw.ellipse([14, 14, 17, 19], outline=cyan_mid, fill=cyan_dark)
    draw.point((14, 14), cyan_hi)

    # Menacing Vertical Slit Pupil (x 15..16, y 13..20)
    draw.line([(15, 13), (15, 20)], fill=pupil)
    draw.line([(16, 14), (16, 19)], fill=pupil)

    # Specular Gleam Reflection Dot (top-left of eye)
    draw.point((13, 14), (255, 255, 255, 255))
    draw.point((14, 13), (255, 255, 255, 255))

    return img

# =============================================================
# SIMPLY SWORDS TOUCH-UPS
# =============================================================

# Swords Touch-up 1: Heavier Broadswords with wider blades, glowing fuller, bold hilts
def draw_swords_heavy_claymores():
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    steel_hi = (255, 255, 255, 255)
    steel_light = (215, 235, 250, 255)
    steel_mid = (140, 175, 205, 255)
    steel_dark = (65, 95, 125, 255)
    steel_out = (25, 40, 55, 255)

    rune_glow = (0, 255, 255, 255)     # Glowing fuller
    rune_core = (230, 255, 255, 255)

    gold_hi = (255, 245, 175, 255)
    gold_mid = (255, 190, 30, 255)
    gold_dark = (155, 100, 15, 255)
    ruby = (255, 25, 45, 255)

    # Blade 1 (TL to BR) - 2px thick broad blade
    # Edge top
    draw.line([(10, 10), (18, 18)], fill=steel_hi)
    # Fuller channel
    draw.line([(10, 11), (19, 20)], fill=rune_glow)
    draw.point((11, 12), rune_core)
    draw.point((14, 15), rune_core)
    # Edge bottom
    draw.line([(11, 12), (19, 20)], fill=steel_mid)
    draw.line([(12, 13), (20, 21)], fill=steel_dark)
    draw.line([(9, 10), (18, 19)], fill=steel_out)

    # Blade 2 (TR to BL) - 2px thick broad blade
    draw.line([(21, 10), (13, 18)], fill=steel_light)
    draw.line([(21, 11), (12, 20)], fill=rune_glow)
    draw.point((20, 12), rune_core)
    draw.point((17, 15), rune_core)
    draw.line([(20, 12), (12, 20)], fill=steel_mid)
    draw.line([(19, 13), (11, 21)], fill=steel_dark)
    draw.line([(22, 10), (13, 19)], fill=steel_out)

    # Center Clash Burst
    draw.rectangle([14, 14, 17, 17], fill=(255, 255, 255, 255))
    draw.point((14, 14), rune_glow)
    draw.point((17, 17), rune_glow)

    # Heavy Flared Crossguards
    # Right Guard (around 19..22, 19..21)
    draw.line([(19, 19), (22, 21)], fill=gold_hi)
    draw.line([(18, 20), (21, 22)], fill=gold_mid)
    draw.point((22, 20), gold_hi) # Quillon flare
    draw.point((18, 21), gold_dark)
    # Grip & Pommel
    draw.line([(20, 21), (21, 22)], fill=(160, 20, 20, 255))
    draw.point((22, 23), gold_mid)
    draw.point((22, 22), ruby)

    # Left Guard (around 9..12, 19..21)
    draw.line([(12, 19), (9, 21)], fill=gold_hi)
    draw.line([(13, 20), (10, 22)], fill=gold_mid)
    draw.point((9, 20), gold_hi)
    draw.point((13, 21), gold_dark)
    draw.line([(11, 21), (10, 22)], fill=(160, 20, 20, 255))
    draw.point((9, 23), gold_mid)
    draw.point((9, 22), ruby)

    return img

# Swords Touch-up 2: Runic Greatsword thrust into Anvil
def draw_swords_anvil_blade():
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    steel_hi = (255, 255, 255, 255)
    steel_mid = (160, 195, 220, 255)
    steel_dark = (75, 105, 130, 255)
    steel_out = (30, 45, 60, 255)
    rune_cyan = (0, 255, 255, 255)

    gold_hi = (255, 245, 160, 255)
    gold_mid = (255, 190, 30, 255)
    ruby = (255, 30, 50, 255)

    anvil_hi = (120, 135, 150, 255)
    anvil_mid = (70, 80, 95, 255)
    anvil_dark = (35, 40, 50, 255)

    # Anvil (Bottom: y 18..23, x 10..21)
    # Anvil face (y 18..19)
    draw.line([(11, 18), (20, 18)], fill=anvil_hi)
    draw.line([(11, 19), (20, 19)], fill=anvil_mid)
    draw.point((10, 18), anvil_hi) # Horn
    # Anvil waist & base
    draw.line([(13, 20), (18, 20)], fill=anvil_mid)
    draw.line([(13, 21), (18, 21)], fill=anvil_dark)
    draw.line([(11, 22), (20, 22)], fill=anvil_mid)
    draw.line([(10, 23), (21, 23)], fill=anvil_dark)

    # Vertical Greatsword (y 9..18, x 15..16)
    # Pommel (y 9)
    draw.point((15, 9), gold_mid)
    draw.point((16, 9), ruby)
    # Grip (y 10..11)
    draw.line([(15, 10), (15, 11)], fill=(160, 25, 25, 255))
    draw.line([(16, 10), (16, 11)], fill=(110, 15, 15, 255))
    # Wide Crossguard (y 12, x 12..19)
    draw.line([(12, 12), (19, 12)], fill=gold_hi)
    draw.point((12, 11), gold_hi)
    draw.point((19, 11), gold_hi)
    draw.line([(13, 13), (18, 13)], fill=gold_mid)

    # Broad Blade thrust down into anvil (y 13..18)
    draw.line([(14, 14), (14, 18)], fill=steel_hi)
    draw.line([(15, 14), (15, 18)], fill=rune_cyan) # Runic fuller
    draw.line([(16, 14), (16, 18)], fill=steel_mid)
    draw.line([(17, 14), (17, 18)], fill=steel_dark)
    # Spark burst on anvil impact
    draw.point((13, 18), (255, 245, 150, 255))
    draw.point((18, 18), (255, 245, 150, 255))

    return img

# =============================================================
# PIONEER VARIATIONS
# =============================================================

# Pioneer Var 1: Crossed Iron Pickaxe & Blazing Pioneer Torch
def draw_pioneer_pick_torch():
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    # Pickaxe Steel
    iron_hi = (245, 250, 255, 255)
    iron_mid = (165, 185, 205, 255)
    iron_dark = (85, 105, 125, 255)
    iron_out = (35, 45, 60, 255)

    # Wood Handle
    wood_hi = (185, 135, 80, 255)
    wood_mid = (135, 90, 45, 255)
    wood_dark = (75, 45, 20, 255)

    # Flame Palette
    flame_white = (255, 255, 220, 255)
    flame_yellow = (255, 215, 0, 255)
    flame_orange = (255, 115, 0, 255)
    flame_red = (220, 25, 10, 255)
    coal_black = (40, 35, 35, 255)

    # --- PICKAXE (Diagonal TL to BR) ---
    # Curved Iron Head at Top-Left (x 9..14, y 9..13)
    draw.line([(9, 13), (11, 10)], fill=iron_hi)
    draw.line([(11, 10), (14, 9)], fill=iron_hi)
    draw.line([(10, 13), (12, 11)], fill=iron_mid)
    draw.line([(12, 11), (15, 10)], fill=iron_mid)
    draw.line([(9, 14), (11, 12)], fill=iron_dark)
    draw.point((9, 12), iron_out) # Sharp left pick tip!
    draw.point((15, 9), iron_dark) # Right pick tip

    # Pickaxe Handle (x 13..21, y 12..22)
    coords_pick = [(13, 12), (14, 13), (15, 15), (17, 17), (18, 19), (20, 21), (21, 22)]
    for pt in coords_pick:
        draw.point(pt, wood_hi)
        draw.point((pt[0]+1, pt[1]), wood_dark)

    # --- BLAZING TORCH (Diagonal TR to BL) ---
    # Torch wooden stick (x 11..17, y 15..22)
    coords_torch = [(11, 22), (12, 21), (13, 19), (15, 17), (16, 15), (17, 14)]
    for pt in coords_torch:
        draw.point(pt, wood_mid)
        draw.point((pt[0]-1, pt[1]), wood_dark)

    # Torch Head Coal Block (x 18..19, y 12..13)
    draw.point((18, 13), coal_black)
    draw.point((19, 13), coal_black)
    draw.point((18, 12), flame_red)
    draw.point((19, 12), flame_orange)

    # Blazing Fire Particles (x 17..22, y 8..12)
    draw.point((18, 11), flame_yellow)
    draw.point((19, 11), flame_white)
    draw.point((19, 10), flame_yellow)
    draw.point((20, 10), flame_orange)
    draw.point((18, 10), flame_orange)
    draw.point((19, 9), flame_white) # Flame tip
    draw.point((20, 9), flame_red)
    draw.point((21, 10), flame_red)
    draw.point((17, 11), flame_red)
    draw.point((18, 8), flame_orange) # Spark

    return img

# Pioneer Var 2: Adventurer's Leather Field Backpack
def draw_pioneer_backpack():
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    leath_hi = (185, 130, 80, 255)
    leath_mid = (135, 85, 45, 255)
    leath_dark = (85, 50, 25, 255)
    leath_out = (40, 22, 10, 255)

    gold_hi = (255, 235, 120, 255)
    gold_mid = (255, 180, 25, 255)
    gold_dark = (145, 90, 10, 255)

    roll_hi = (135, 185, 105, 255)     # Green bedroll
    roll_mid = (85, 135, 60, 255)
    roll_dark = (45, 80, 30, 255)

    # Green Rolled Bedroll on Top (y 9..12, x 11..20)
    for y in range(9, 13):
        for x in range(12, 20):
            draw.point((x, y), roll_mid if y > 9 else roll_hi)
    draw.line([(11, 10), (11, 12)], fill=roll_dark) # Roll cap left
    draw.line([(20, 10), (20, 12)], fill=roll_dark) # Roll cap right
    # Leather bedroll tie straps
    draw.line([(13, 9), (13, 12)], fill=leath_dark)
    draw.line([(18, 9), (18, 12)], fill=leath_dark)
    draw.point((13, 11), gold_hi)
    draw.point((18, 11), gold_hi)

    # Main Leather Backpack Body (y 13..21, x 10..21)
    for y in range(13, 22):
        for x in range(11, 21):
            draw.point((x, y), leath_mid)

    # Highlights (Left) & Shadows (Right/Bottom)
    for y in range(13, 21):
        draw.point((11, y), leath_hi)
        draw.point((20, y), leath_dark)
    draw.line([(11, 21), (20, 21)], fill=leath_dark)

    # Center Pocket Flap (y 14..18, x 13..18)
    draw.rectangle([13, 14, 18, 18], fill=leath_hi, outline=leath_dark)
    draw.point((15, 17), gold_hi) # Pocket Buckle
    draw.point((16, 17), gold_mid)
    draw.point((15, 18), leath_dark)
    draw.point((16, 18), leath_dark)

    # Two Main Shoulder / Flap Straps
    draw.line([(12, 13), (12, 20)], fill=leath_dark)
    draw.line([(19, 13), (19, 20)], fill=leath_dark)
    draw.point((12, 16), gold_hi) # Left Buckle
    draw.point((19, 16), gold_hi) # Right Buckle

    # Outer Outline
    draw.line([(10, 13), (10, 21)], fill=leath_out)
    draw.line([(21, 13), (21, 21)], fill=leath_out)
    draw.line([(11, 22), (20, 22)], fill=leath_out)

    return img

# Pioneer Var 3: Gleaming 8-Point Golden Nautical Star
def draw_pioneer_nautical_star():
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    star_hi = (255, 255, 200, 255)
    star_gold = (255, 210, 50, 255)
    star_mid = (235, 160, 20, 255)
    star_dark = (165, 95, 10, 255)
    star_shad = (85, 45, 5, 255)

    gem_hi = (220, 255, 255, 255)
    gem_core = (0, 230, 255, 255)
    gem_dark = (0, 120, 175, 255)

    # Faceted 3D Nautical Star (x 9..22, y 9..22)
    # NORTH Point (up to y=9)
    draw.polygon([(15, 15), (15, 9), (14, 15)], fill=star_hi)
    draw.polygon([(15, 15), (15, 9), (16, 15)], fill=star_dark)

    # SOUTH Point (down to y=22)
    draw.polygon([(15, 16), (15, 22), (16, 16)], fill=star_hi)
    draw.polygon([(15, 16), (15, 22), (14, 16)], fill=star_dark)

    # WEST Point (left to x=9)
    draw.polygon([(15, 15), (9, 15), (15, 16)], fill=star_hi)
    draw.polygon([(15, 15), (9, 15), (15, 14)], fill=star_dark)

    # EAST Point (right to x=22)
    draw.polygon([(16, 15), (22, 15), (16, 14)], fill=star_hi)
    draw.polygon([(16, 15), (22, 15), (16, 16)], fill=star_dark)

    # 4 Secondary Corner Points (NE, NW, SE, SW)
    draw.line([(13, 13), (11, 11)], fill=star_gold) # NW
    draw.line([(18, 13), (20, 11)], fill=star_gold) # NE
    draw.line([(13, 18), (11, 20)], fill=star_gold) # SW
    draw.line([(18, 18), (20, 20)], fill=star_gold) # SE

    # Center Radiant Diamond Gem (x 14..17, y 14..17)
    draw.rectangle([14, 14, 17, 17], fill=gem_core, outline=star_dark)
    draw.point((14, 14), gem_hi)
    draw.point((17, 17), gem_dark)

    return img

def scale_8x(img):
    return img.resize((img.width * 8, img.height * 8), Image.Resampling.NEAREST)

def composite(base, emblem):
    comp = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    comp.alpha_composite(base)
    comp.alpha_composite(emblem)
    return comp

def run():
    print("Generating Emblem Redesigns...")

    # Load coffers
    coffer_epic = Image.open(os.path.join(SCALING_DIR, "coffer_epic.png"))
    coffer_rare = Image.open(os.path.join(SCALING_DIR, "coffer_rare.png"))
    coffer_uncommon = Image.open(os.path.join(SCALING_DIR, "coffer_uncommon.png"))
    coffer_mythic = Image.open(os.path.join(SCALING_DIR, "coffer_mythic.png"))

    variants = {
        # Boss
        "boss_v1_dragon_skull": draw_boss_dragon_skull(),
        "boss_v2_void_eye": draw_boss_void_eye(),
        # Weapons
        "weapons_v1_heavy_claymores": draw_swords_heavy_claymores(),
        "weapons_v2_anvil_blade": draw_swords_anvil_blade(),
        # Pioneer
        "pioneer_v1_pick_torch": draw_pioneer_pick_torch(),
        "pioneer_v2_backpack": draw_pioneer_backpack(),
        "pioneer_v3_nautical_star": draw_pioneer_nautical_star(),
    }

    for name, img in variants.items():
        img.save(os.path.join(OUT_DIR, f"{name}.png"))
        scale_8x(img).save(os.path.join(OUT_DIR, f"{name}_256.png"))
        
        # Also composite on appropriate coffer
        if "boss" in name:
            comp = composite(coffer_epic, img)
        elif "weapons" in name:
            comp = composite(coffer_rare, img)
        else:
            comp = composite(coffer_uncommon, img)
            
        comp.save(os.path.join(OUT_DIR, f"comp_{name}.png"))
        scale_8x(comp).save(os.path.join(OUT_DIR, f"comp_{name}_256.png"))
        print(f"Generated: {name}")

    print("Emblem redesign variations generated in:", OUT_DIR)

if __name__ == "__main__":
    run()
