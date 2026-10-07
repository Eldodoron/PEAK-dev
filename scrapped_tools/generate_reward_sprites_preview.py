import os
from PIL import Image, ImageDraw

OUTPUT_DIR = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568\sprite_preview"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 32x32 RGBA Canvas
def create_canvas():
    return Image.new("RGBA", (32, 32), (0, 0, 0, 0))

# -------------------------------------------------------------
# LAYER 1: BASE CONTAINER SILHOUETTE & BODY (Heavy Reinforced Coffer)
# -------------------------------------------------------------
def draw_layer1_base():
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    # Base Coffer Dimensions: x: 3..28, y: 4..27 (26x24 px)
    # Outer dark outline (#1e140d)
    outline = (30, 20, 13, 255)
    body_dark = (75, 48, 30, 255)
    body_mid = (112, 73, 46, 255)
    body_light = (145, 96, 61, 255)
    body_hi = (176, 120, 80, 255)

    # Silhouette fill
    for y in range(5, 27):
        for x in range(4, 28):
            draw.point((x, y), body_mid)

    # Wood planks & shading
    for y in range(5, 12): # Lid
        for x in range(5, 27):
            draw.point((x, y), body_light if y < 8 else body_mid)
    
    # Highlight top lid edge
    for x in range(5, 27):
        draw.point((x, 5), body_hi)
        draw.point((x, 12), (50, 32, 20, 255)) # Lid groove shadow
        draw.point((x, 13), body_hi) # Lower body rim highlight
        draw.point((x, 26), body_dark) # Bottom shadow

    # Left edge highlight, right edge shadow
    for y in range(6, 26):
        draw.point((4, y), body_hi)
        draw.point((27, y), body_dark)

    # Outer outline box
    draw.rectangle([3, 4, 28, 27], outline=outline)
    # Rounded corners (remove corner pixel)
    draw.point((3, 4), (0, 0, 0, 0))
    draw.point((28, 4), (0, 0, 0, 0))
    draw.point((3, 27), (0, 0, 0, 0))
    draw.point((28, 27), (0, 0, 0, 0))

    # Inner medallion recess (circular / rounded 14x14 area in center: x 9..22, y 10..23)
    recess_dark = (35, 25, 18, 255)
    recess_mid = (50, 36, 26, 255)
    for y in range(11, 23):
        for x in range(10, 22):
            draw.point((x, y), recess_mid)
    # Recess border
    draw.rectangle([9, 10, 22, 23], outline=recess_dark)
    draw.point((9, 10), body_mid)
    draw.point((22, 10), body_mid)
    draw.point((9, 23), body_mid)
    draw.point((22, 23), body_mid)

    return img

# -------------------------------------------------------------
# LAYER 2: RARITY BORDER & TRIM (Corner brackets, latch, rivets)
# -------------------------------------------------------------
RARITY_PALETTES = {
    "common": {
        "name": "Common (Iron/Slate)",
        "dark": (50, 50, 55, 255),
        "mid": (100, 105, 115, 255),
        "light": (160, 165, 175, 255),
        "hi": (220, 225, 235, 255),
        "gem": (140, 145, 155, 255)
    },
    "uncommon": {
        "name": "Uncommon (Verdant Emerald)",
        "dark": (20, 60, 25, 255),
        "mid": (45, 125, 55, 255),
        "light": (76, 175, 80, 255),
        "hi": (165, 235, 170, 255),
        "gem": (105, 240, 174, 255)
    },
    "rare": {
        "name": "Rare (Cobalt Sapphire)",
        "dark": (15, 45, 95, 255),
        "mid": (25, 105, 195, 255),
        "light": (50, 155, 245, 255),
        "hi": (175, 220, 255, 255),
        "gem": (68, 210, 255, 255)
    },
    "epic": {
        "name": "Epic (Royal Amethyst)",
        "dark": (50, 15, 80, 255),
        "mid": (115, 30, 160, 255),
        "light": (170, 65, 225, 255),
        "hi": (235, 165, 255, 255),
        "gem": (224, 64, 251, 255)
    },
    "mythic": {
        "name": "Mythic (Netherite Flame / Gold)",
        "dark": (60, 15, 10, 255),
        "mid": (195, 35, 30, 255),
        "light": (255, 145, 0, 255),
        "hi": (255, 230, 120, 255),
        "gem": (255, 60, 0, 255)
    }
}

def draw_layer2_trim(rarity_key):
    pal = RARITY_PALETTES[rarity_key]
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    d = pal["dark"]
    m = pal["mid"]
    l = pal["light"]
    h = pal["hi"]

    # Top-Left Bracket (x: 4..8, y: 5..9)
    for y in range(5, 9):
        draw.point((4, y), h)
        draw.point((5, y), l)
    for x in range(5, 9):
        draw.point((x, 5), h)
        draw.point((x, 6), l)
    draw.point((4, 5), h)
    draw.point((6, 7), d) # Rivet

    # Top-Right Bracket (x: 23..27, y: 5..9)
    for y in range(5, 9):
        draw.point((27, y), d)
        draw.point((26, y), m)
    for x in range(23, 27):
        draw.point((x, 5), h)
        draw.point((x, 6), l)
    draw.point((27, 5), l)
    draw.point((25, 7), d) # Rivet

    # Bottom-Left Bracket (x: 4..8, y: 22..26)
    for y in range(22, 26):
        draw.point((4, y), h)
        draw.point((5, y), l)
    for x in range(5, 9):
        draw.point((x, 26), d)
        draw.point((x, 25), m)
    draw.point((4, 26), l)
    draw.point((6, 23), d) # Rivet

    # Bottom-Right Bracket (x: 23..27, y: 22..26)
    for y in range(22, 26):
        draw.point((27, y), d)
        draw.point((26, y), m)
    for x in range(23, 27):
        draw.point((x, 26), d)
        draw.point((x, 25), m)
    draw.point((27, 26), d)
    draw.point((25, 23), d) # Rivet

    # Vertical Reinforced Metal Straps (x=7, x=24)
    for y in range(9, 23):
        draw.point((7, y), l)
        draw.point((24, y), m)

    # Center Medallion Border Ring (x 9..22, y 10..23)
    draw.rectangle([9, 10, 22, 23], outline=m)
    draw.point((10, 10), h)
    draw.point((11, 10), h)
    draw.point((12, 10), h)
    draw.point((9, 11), h)
    draw.point((9, 12), h)

    # 4 Gem corner studs on medallion ring
    draw.point((9, 10), pal["gem"])
    draw.point((22, 10), pal["gem"])
    draw.point((9, 23), pal["gem"])
    draw.point((22, 23), pal["gem"])

    return img

# -------------------------------------------------------------
# LAYER 3: CATEGORY EMBLEMS (10x10 inside center medallion: x 11..20, y 12..21)
# -------------------------------------------------------------
def draw_layer3_emblem(category):
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    white = (245, 245, 250, 255)
    light_grey = (195, 200, 210, 255)
    mid_grey = (130, 135, 145, 255)
    dark_grey = (60, 60, 70, 255)

    if category == "boss":
        # Horned Skull / Demon Crown
        # Horns
        horn = (210, 180, 140, 255)
        horn_tip = (240, 220, 180, 255)
        draw.point((11, 12), horn_tip)
        draw.point((12, 13), horn)
        draw.point((20, 12), horn_tip)
        draw.point((19, 13), horn)

        # Cranium (x 13..18, y 13..16)
        for y in range(14, 17):
            for x in range(13, 19):
                draw.point((x, y), white)
        draw.point((14, 13), white)
        draw.point((15, 13), white)
        draw.point((16, 13), white)
        draw.point((17, 13), white)

        # Eye Sockets (dark glowing or black)
        eye_color = (20, 15, 25, 255)
        draw.point((14, 16), eye_color)
        draw.point((17, 16), eye_color)

        # Nose cavity
        draw.point((15, 17), light_grey)
        draw.point((16, 17), dark_grey)

        # Jaw & Teeth (x 14..17, y 18..19)
        draw.point((14, 18), white)
        draw.point((15, 18), dark_grey)
        draw.point((16, 18), white)
        draw.point((17, 18), dark_grey)

        draw.point((14, 19), light_grey)
        draw.point((15, 19), white)
        draw.point((16, 19), white)
        draw.point((17, 19), light_grey)

    elif category == "weapons":
        # Crossed Dual Blades
        blade = (230, 235, 245, 255)
        blade_edge = (175, 185, 205, 255)
        gold = (245, 195, 65, 255)
        pommel = (185, 130, 30, 255)

        # Blade 1: Top-Left to Bottom-Right (12,12 to 19,19)
        coords1 = [(12,12), (13,13), (14,14), (15,15), (16,16), (17,17), (18,18), (19,19)]
        for pt in coords1:
            draw.point(pt, blade)

        # Blade 2: Top-Right to Bottom-Left (19,12 to 12,19)
        coords2 = [(19,12), (18,13), (17,14), (16,15), (15,16), (14,17), (13,18), (12,19)]
        for pt in coords2:
            draw.point(pt, blade)

        # Crossguards (gold)
        draw.point((13, 18), gold)
        draw.point((14, 19), gold)
        draw.point((18, 18), gold)
        draw.point((17, 19), gold)

        # Center clash highlight
        draw.point((15, 15), (255, 255, 255, 255))
        draw.point((16, 16), (255, 255, 255, 255))

        # Pommels
        draw.point((11, 20), pommel)
        draw.point((20, 20), pommel)

    elif category == "food":
        # Gourmet Apple & Chef Hat / Feast
        apple_red = (225, 45, 40, 255)
        apple_hi = (255, 110, 100, 255)
        apple_dark = (140, 20, 25, 255)
        leaf_green = (80, 185, 60, 255)
        stem_brown = (110, 70, 35, 255)

        # Stem & Leaf
        draw.point((15, 12), stem_brown)
        draw.point((16, 12), leaf_green)
        draw.point((17, 12), leaf_green)

        # Apple body (x 13..18, y 13..18)
        for y in range(14, 18):
            for x in range(13, 19):
                draw.point((x, y), apple_red)

        # Top indent
        draw.point((15, 13), apple_dark)
        draw.point((14, 13), apple_red)
        draw.point((16, 13), apple_red)
        draw.point((17, 13), apple_red)

        # Highlight
        draw.point((14, 14), apple_hi)
        draw.point((14, 15), apple_hi)

        # Shadow bottom
        draw.point((14, 18), apple_dark)
        draw.point((15, 18), apple_dark)
        draw.point((16, 18), apple_dark)
        draw.point((17, 18), apple_dark)

        # Fork silhouette beside apple (x 19, y 13..19)
        fork = (210, 215, 225, 255)
        draw.point((19, 13), fork)
        draw.point((21, 13), fork)
        draw.point((20, 14), fork)
        draw.point((20, 15), fork)
        draw.point((20, 16), fork)
        draw.point((20, 17), fork)
        draw.point((20, 18), fork)

    elif category == "pioneer":
        # 4-Point Compass Rose / Star
        star_gold = (255, 205, 50, 255)
        star_hi = (255, 245, 160, 255)
        star_dark = (180, 135, 25, 255)
        center_gem = (80, 215, 255, 255)

        # Center core
        draw.point((15, 15), center_gem)
        draw.point((16, 15), center_gem)
        draw.point((15, 16), center_gem)
        draw.point((16, 16), center_gem)

        # North pointer (up to y=11)
        draw.point((15, 14), star_hi)
        draw.point((16, 14), star_gold)
        draw.point((15, 13), star_hi)
        draw.point((16, 13), star_gold)
        draw.point((15, 12), star_hi)
        draw.point((16, 12), star_dark)

        # South pointer (down to y=19)
        draw.point((15, 17), star_gold)
        draw.point((16, 17), star_dark)
        draw.point((15, 18), star_gold)
        draw.point((16, 18), star_dark)
        draw.point((15, 19), star_dark)

        # West pointer (left to x=11)
        draw.point((14, 15), star_hi)
        draw.point((14, 16), star_gold)
        draw.point((13, 15), star_hi)
        draw.point((13, 16), star_gold)
        draw.point((12, 15), star_hi)

        # East pointer (right to x=20)
        draw.point((17, 15), star_gold)
        draw.point((17, 16), star_dark)
        draw.point((18, 15), star_gold)
        draw.point((18, 16), star_dark)
        draw.point((19, 15), star_dark)

    return img

# -------------------------------------------------------------
# COMPOSITOR & EXPORTER
# -------------------------------------------------------------
def composite(l1, l2, l3):
    comp = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    comp.alpha_composite(l1)
    comp.alpha_composite(l2)
    comp.alpha_composite(l3)
    return comp

def scale_preview(img, factor=8):
    return img.resize((img.width * factor, img.height * factor), Image.Resampling.NEAREST)

def run():
    print("Generating Normalized 32x32 Layered Sprites...")

    # 1. Base Layer
    layer1_base = draw_layer1_base()
    layer1_base.save(os.path.join(OUTPUT_DIR, "layer1_base_coffer.png"))
    scale_preview(layer1_base).save(os.path.join(OUTPUT_DIR, "layer1_base_coffer_256.png"))

    # 2. Rarity Layers
    rarity_layers = {}
    for r_key in RARITY_PALETTES.keys():
        l2 = draw_layer2_trim(r_key)
        rarity_layers[r_key] = l2
        l2.save(os.path.join(OUTPUT_DIR, f"layer2_trim_{r_key}.png"))
        scale_preview(l2).save(os.path.join(OUTPUT_DIR, f"layer2_trim_{r_key}_256.png"))

    # 3. Emblem Layers
    categories = ["boss", "weapons", "food", "pioneer"]
    emblem_layers = {}
    for cat in categories:
        l3 = draw_layer3_emblem(cat)
        emblem_layers[cat] = l3
        l3.save(os.path.join(OUTPUT_DIR, f"layer3_emblem_{cat}.png"))
        scale_preview(l3).save(os.path.join(OUTPUT_DIR, f"layer3_emblem_{cat}_256.png"))

    # 4. Generate all Combinations (4 categories x 5 rarities = 20 total)
    for cat in categories:
        for r_key in RARITY_PALETTES.keys():
            final_img = composite(layer1_base, rarity_layers[r_key], emblem_layers[cat])
            name = f"cache_{cat}_{r_key}"
            final_img.save(os.path.join(OUTPUT_DIR, f"{name}.png"))
            scale_preview(final_img).save(os.path.join(OUTPUT_DIR, f"{name}_256.png"))
            print(f"Generated: {name}.png (32x32 & 256x256)")

    print("All sprites successfully generated in:", OUTPUT_DIR)

if __name__ == "__main__":
    run()
