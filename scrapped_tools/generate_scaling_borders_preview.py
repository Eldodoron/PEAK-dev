import os
from PIL import Image, ImageDraw

OUTPUT_DIR = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568\scaling_borders"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_canvas():
    return Image.new("RGBA", (32, 32), (0, 0, 0, 0))

# -------------------------------------------------------------
# BASE COFFER (Darker, richer chestnut/ironwood for maximum contrast)
# -------------------------------------------------------------
def draw_base_coffer(darken=False):
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    outline = (22, 16, 12, 255)
    # Balanced, rich wood palette
    body_dark = (58, 36, 22, 255) if not darken else (40, 26, 18, 255)
    body_mid = (92, 58, 36, 255) if not darken else (68, 44, 28, 255)
    body_light = (124, 80, 50, 255) if not darken else (96, 62, 40, 255)
    body_hi = (156, 102, 66, 255) if not darken else (122, 80, 52, 255)

    # Fill
    for y in range(5, 27):
        for x in range(4, 28):
            draw.point((x, y), body_mid)

    # Lid planks (y: 5..11)
    for y in range(5, 12):
        for x in range(5, 27):
            draw.point((x, y), body_light if y < 8 else body_mid)

    # Highlights & shadows
    for x in range(5, 27):
        draw.point((x, 5), body_hi)
        draw.point((x, 11), (32, 20, 14, 255)) # Seam
        draw.point((x, 12), body_hi)
        draw.point((x, 26), body_dark)

    for y in range(6, 26):
        draw.point((4, y), body_hi)
        draw.point((27, y), body_dark)

    # Outer outline
    draw.rectangle([3, 4, 28, 27], outline=outline)
    draw.point((3, 4), (0, 0, 0, 0))
    draw.point((28, 4), (0, 0, 0, 0))
    draw.point((3, 27), (0, 0, 0, 0))
    draw.point((28, 27), (0, 0, 0, 0))

    # Center socket recess (x 8..23, y 9..24) - enlarged to 16x16 for bold emblems
    socket_dark = (26, 18, 14, 255)
    socket_mid = (38, 26, 20, 255)
    for y in range(10, 24):
        for x in range(9, 23):
            draw.point((x, y), socket_mid)
    draw.rectangle([8, 9, 23, 24], outline=socket_dark)

    return img

# -------------------------------------------------------------
# PROGRESSIVELY SCALING BORDER GEOMETRY (5 DISTINCT TIERS)
# -------------------------------------------------------------

# 1. COMMON: Humble flat tin L-brackets (3x3), no fancy trim, 1 rivet
def draw_border_common():
    img = create_canvas()
    draw = ImageDraw.Draw(img)
    hi = (205, 210, 215, 255)
    mid = (135, 140, 150, 255)
    dark = (70, 75, 85, 255)
    rivet = (40, 42, 48, 255)

    # Tiny 3x3 L-brackets
    # TL
    draw.line([(4, 5), (6, 5)], fill=hi)
    draw.line([(4, 5), (4, 7)], fill=hi)
    draw.point((5, 6), rivet)

    # TR
    draw.line([(25, 5), (27, 5)], fill=hi)
    draw.line([(27, 5), (27, 7)], fill=mid)
    draw.point((26, 6), rivet)

    # BL
    draw.line([(4, 24), (4, 26)], fill=hi)
    draw.line([(4, 26), (6, 26)], fill=mid)
    draw.point((5, 25), rivet)

    # BR
    draw.line([(27, 24), (27, 26)], fill=dark)
    draw.line([(25, 26), (27, 26)], fill=dark)
    draw.point((26, 25), rivet)

    # Minimal flat center latch ring
    draw.rectangle([8, 9, 23, 24], outline=dark)
    draw.line([(8, 9), (23, 9)], fill=mid)
    return img

# 2. UNCOMMON: Reinforced copper/bronze corner plates (5x5) with double rivets
def draw_border_uncommon():
    img = create_canvas()
    draw = ImageDraw.Draw(img)
    hi = (175, 245, 180, 255)
    mid = (65, 170, 75, 255)
    dark = (25, 80, 35, 255)
    rivet = (15, 45, 20, 255)

    # 5x5 Corner plates
    # TL (x: 4..8, y: 5..9)
    for y in range(5, 9):
        draw.point((4, y), hi)
        draw.point((5, y), mid)
    for x in range(5, 9):
        draw.point((x, 5), hi)
        draw.point((x, 6), mid)
    draw.point((4, 5), hi)
    draw.point((6, 7), rivet)
    draw.point((7, 6), rivet)

    # TR (x: 23..27, y: 5..9)
    for y in range(5, 9):
        draw.point((27, y), dark)
        draw.point((26, y), mid)
    for x in range(23, 27):
        draw.point((x, 5), hi)
        draw.point((x, 6), mid)
    draw.point((27, 5), mid)
    draw.point((25, 7), rivet)
    draw.point((24, 6), rivet)

    # BL (x: 4..8, y: 22..26)
    for y in range(22, 26):
        draw.point((4, y), hi)
        draw.point((5, y), mid)
    for x in range(5, 9):
        draw.point((x, 26), dark)
        draw.point((x, 25), mid)
    draw.point((4, 26), mid)
    draw.point((6, 24), rivet)
    draw.point((7, 25), rivet)

    # BR (x: 23..27, y: 22..26)
    for y in range(22, 26):
        draw.point((27, y), dark)
        draw.point((26, y), dark)
    for x in range(23, 27):
        draw.point((x, 26), dark)
        draw.point((x, 25), dark)
    draw.point((25, 24), rivet)
    draw.point((24, 25), rivet)

    # Center socket ring with corner studs
    draw.rectangle([8, 9, 23, 24], outline=mid)
    draw.point((8, 9), hi)
    draw.point((23, 9), hi)
    draw.point((8, 24), mid)
    draw.point((23, 24), dark)
    return img

# 3. RARE: Heavy angled steel armor plates (7x7) with bevels & vertical bands
def draw_border_rare():
    img = create_canvas()
    draw = ImageDraw.Draw(img)
    hi = (185, 230, 255, 255)
    light = (75, 175, 255, 255)
    mid = (30, 115, 215, 255)
    dark = (15, 55, 120, 255)
    rivet = (10, 30, 70, 255)

    # 7x7 Chamfered armor corners with diagonal cut
    # TL
    for y in range(5, 11):
        draw.point((4, y), hi)
        draw.point((5, y), light)
    for x in range(5, 11):
        draw.point((x, 5), hi)
        draw.point((x, 6), light)
    draw.line([(5, 10), (10, 5)], fill=mid) # Chamfer angle
    draw.point((6, 7), rivet)
    draw.point((8, 7), rivet)

    # TR
    for y in range(5, 11):
        draw.point((27, y), dark)
        draw.point((26, y), mid)
    for x in range(21, 27):
        draw.point((x, 5), hi)
        draw.point((x, 6), light)
    draw.line([(26, 10), (21, 5)], fill=mid)
    draw.point((25, 7), rivet)
    draw.point((23, 7), rivet)

    # BL
    for y in range(20, 26):
        draw.point((4, y), hi)
        draw.point((5, y), light)
    for x in range(5, 11):
        draw.point((x, 26), dark)
        draw.point((x, 25), mid)
    draw.line([(5, 21), (10, 26)], fill=mid)
    draw.point((6, 24), rivet)
    draw.point((8, 24), rivet)

    # BR
    for y in range(20, 26):
        draw.point((27, y), dark)
        draw.point((26, y), dark)
    for x in range(21, 27):
        draw.point((x, 26), dark)
        draw.point((x, 25), dark)
    draw.line([(26, 21), (21, 26)], fill=dark)
    draw.point((25, 24), rivet)
    draw.point((23, 24), rivet)

    # Heavy side vertical support bands (x=7, x=24)
    for y in range(11, 20):
        draw.point((7, y), light)
        draw.point((24, y), mid)

    # Socket ring with dual gem studs
    draw.rectangle([8, 9, 23, 24], outline=mid)
    draw.line([(9, 9), (22, 9)], fill=light)
    draw.point((8, 9), hi)
    draw.point((23, 9), hi)
    draw.point((8, 24), light)
    draw.point((23, 24), dark)
    return img

# 4. EPIC: Gothic Arched Filigree + High-Contrast Luminous Amethyst / Silver
def draw_border_epic():
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    # HIGH-CONTRAST PALETTE: Luminous Silver & Neon Amethyst
    silver_hi = (255, 245, 255, 255)
    neon_violet = (225, 80, 255, 255)   # Vibrant neon magenta-violet
    rich_amethyst = (160, 30, 210, 255) # Saturated purple
    deep_purple = (75, 15, 105, 255)
    gem_glow = (255, 180, 255, 255)

    # Winged gothic arches on corners (8x8)
    # TL
    draw.line([(4, 5), (11, 5)], fill=silver_hi)
    draw.line([(4, 5), (4, 12)], fill=silver_hi)
    draw.line([(5, 6), (10, 6)], fill=neon_violet)
    draw.line([(5, 6), (5, 11)], fill=neon_violet)
    draw.point((6, 7), rich_amethyst)
    draw.point((7, 8), rich_amethyst)
    draw.point((8, 9), rich_amethyst)
    # Wing flairs
    draw.point((11, 4), silver_hi)
    draw.point((4, 12), silver_hi)
    draw.point((6, 6), gem_glow) # Raised Amethyst Gem

    # TR
    draw.line([(20, 5), (27, 5)], fill=silver_hi)
    draw.line([(27, 5), (27, 12)], fill=rich_amethyst)
    draw.line([(21, 6), (26, 6)], fill=neon_violet)
    draw.line([(26, 6), (26, 11)], fill=neon_violet)
    draw.point((25, 7), deep_purple)
    draw.point((24, 8), deep_purple)
    draw.point((23, 9), deep_purple)
    draw.point((20, 4), silver_hi)
    draw.point((27, 12), rich_amethyst)
    draw.point((25, 6), gem_glow)

    # BL
    draw.line([(4, 19), (4, 26)], fill=silver_hi)
    draw.line([(4, 26), (11, 26)], fill=rich_amethyst)
    draw.line([(5, 20), (5, 25)], fill=neon_violet)
    draw.line([(5, 25), (10, 25)], fill=neon_violet)
    draw.point((6, 25), gem_glow)

    # BR
    draw.line([(27, 19), (27, 26)], fill=deep_purple)
    draw.line([(20, 26), (27, 26)], fill=deep_purple)
    draw.line([(26, 20), (26, 25)], fill=rich_amethyst)
    draw.line([(21, 25), (26, 25)], fill=rich_amethyst)
    draw.point((25, 25), gem_glow)

    # Gothic Crown Arch on top lid (x 13..18, y 4..5)
    draw.point((13, 4), neon_violet)
    draw.point((14, 3), silver_hi) # Peak
    draw.point((15, 4), silver_hi)
    draw.point((16, 4), silver_hi)
    draw.point((17, 3), silver_hi) # Peak
    draw.point((18, 4), neon_violet)

    # Center socket: Ornate double-ring with 4 luminous Amethyst gems
    draw.rectangle([8, 9, 23, 24], outline=rich_amethyst)
    draw.rectangle([9, 10, 22, 23], outline=neon_violet)
    draw.point((8, 9), silver_hi)
    draw.point((23, 9), silver_hi)
    draw.point((8, 24), silver_hi)
    draw.point((23, 24), silver_hi)

    return img

# 5. MYTHIC: Majestic Gilded Netherite Crown + Flared Spikes + Molten Embers
def draw_border_mythic():
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    gold_hi = (255, 245, 175, 255)
    gold_mid = (255, 185, 30, 255)
    flame_red = (245, 45, 25, 255)
    netherite = (45, 35, 40, 255)
    ember_glow = (255, 120, 20, 255)

    # Massive Spiked Corner Wings
    # TL Spikes
    draw.line([(2, 3), (4, 5)], fill=gold_hi) # Extended external corner spike
    draw.line([(4, 5), (12, 5)], fill=gold_hi)
    draw.line([(4, 5), (4, 13)], fill=gold_hi)
    draw.line([(5, 6), (11, 6)], fill=gold_mid)
    draw.line([(5, 6), (5, 12)], fill=gold_mid)
    draw.line([(6, 7), (10, 7)], fill=flame_red)
    draw.line([(6, 7), (6, 11)], fill=flame_red)

    # TR Spikes
    draw.line([(29, 3), (27, 5)], fill=gold_hi)
    draw.line([(19, 5), (27, 5)], fill=gold_hi)
    draw.line([(27, 5), (27, 13)], fill=gold_mid)
    draw.line([(20, 6), (26, 6)], fill=gold_mid)
    draw.line([(26, 6), (26, 12)], fill=flame_red)

    # BL Spikes
    draw.line([(2, 28), (4, 26)], fill=gold_hi)
    draw.line([(4, 18), (4, 26)], fill=gold_hi)
    draw.line([(4, 26), (12, 26)], fill=gold_mid)
    draw.line([(5, 25), (11, 25)], fill=flame_red)

    # BR Spikes
    draw.line([(29, 28), (27, 26)], fill=flame_red)
    draw.line([(27, 18), (27, 26)], fill=gold_mid)
    draw.line([(19, 26), (27, 26)], fill=gold_mid)

    # Grand Royal Crown on top lid (x 11..20, y 2..5)
    crown_pts = [(12, 4), (13, 2), (14, 4), (15, 3), (16, 3), (17, 4), (18, 2), (19, 4)]
    for pt in crown_pts:
        draw.point(pt, gold_hi if pt[1] < 4 else gold_mid)
    draw.point((13, 2), (255, 255, 255, 255)) # Crown gem
    draw.point((18, 2), (255, 255, 255, 255))
    draw.point((15, 2), (255, 255, 255, 255))

    # Center socket: Sunburst / Runic Dragon Crest
    draw.rectangle([7, 8, 24, 25], outline=gold_mid)
    draw.rectangle([8, 9, 23, 24], outline=flame_red)
    # 4 Embers floating
    draw.point((6, 16), ember_glow)
    draw.point((25, 16), ember_glow)
    draw.point((16, 7), ember_glow)
    draw.point((16, 26), ember_glow)

    return img

def scale_8x(img):
    return img.resize((img.width * 8, img.height * 8), Image.Resampling.NEAREST)

def composite(base, border):
    comp = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    comp.alpha_composite(base)
    comp.alpha_composite(border)
    return comp

def run():
    print("Generating Scaling Borders Comparison...")
    base = draw_base_coffer(darken=False)
    base_dark = draw_base_coffer(darken=True) # For Epic purple high-contrast

    tiers = [
        ("common", draw_border_common(), base),
        ("uncommon", draw_border_uncommon(), base),
        ("rare", draw_border_rare(), base),
        ("epic", draw_border_epic(), base_dark),
        ("mythic", draw_border_mythic(), base_dark),
    ]

    for name, border, b_img in tiers:
        # Save border alone
        border.save(os.path.join(OUTPUT_DIR, f"border_{name}.png"))
        scale_8x(border).save(os.path.join(OUTPUT_DIR, f"border_{name}_256.png"))

        # Save composite on box
        comp = composite(b_img, border)
        comp.save(os.path.join(OUTPUT_DIR, f"coffer_{name}.png"))
        scale_8x(comp).save(os.path.join(OUTPUT_DIR, f"coffer_{name}_256.png"))
        print(f"Generated tier: {name}")

    print("Completed in:", OUTPUT_DIR)

if __name__ == "__main__":
    run()
