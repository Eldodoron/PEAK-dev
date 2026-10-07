import os
from PIL import Image, ImageDraw

BRAIN_DIR = r"C:\Users\chris\.gemini\antigravity\brain\960e2769-f3f6-4bab-91f2-18a1fcc9b568"
FINAL_DIR = os.path.join(BRAIN_DIR, "final_tier_coffers")
os.makedirs(FINAL_DIR, exist_ok=True)

def create_canvas():
    return Image.new("RGBA", (32, 32), (0, 0, 0, 0))

# -------------------------------------------------------------
# BASE COFFER WITH CLEAN WOOD GRAIN & RECESSED CENTER
# -------------------------------------------------------------
def draw_base_coffer(darken=False):
    img = create_canvas()
    draw = ImageDraw.Draw(img)

    outline = (22, 16, 12, 255)
    body_dark = (55, 34, 20, 255) if not darken else (38, 24, 16, 255)
    body_mid = (88, 55, 34, 255) if not darken else (64, 40, 26, 255)
    body_light = (120, 78, 48, 255) if not darken else (92, 58, 38, 255)
    body_hi = (152, 100, 64, 255) if not darken else (118, 76, 50, 255)

    # Coffer Fill (x: 4..27, y: 5..26)
    for y in range(5, 27):
        for x in range(4, 28):
            draw.point((x, y), body_mid)

    # Lid bevel & planks
    for y in range(5, 12):
        for x in range(5, 27):
            draw.point((x, y), body_light if y < 8 else body_mid)

    # Seams & horizontal grooves
    for x in range(5, 27):
        draw.point((x, 5), body_hi)
        draw.point((x, 11), (30, 18, 12, 255)) # Lid seam
        draw.point((x, 12), body_hi)
        draw.point((x, 26), body_dark)

    # Vertical side bevels
    for y in range(6, 26):
        draw.point((4, y), body_hi)
        draw.point((27, y), body_dark)

    # Outer border
    draw.rectangle([3, 4, 28, 27], outline=outline)
    draw.point((3, 4), (0, 0, 0, 0))
    draw.point((28, 4), (0, 0, 0, 0))
    draw.point((3, 27), (0, 0, 0, 0))
    draw.point((28, 27), (0, 0, 0, 0))

    # Center wood panel (recessed, x: 9..22, y: 10..23)
    panel_dark = (32, 20, 14, 255)
    panel_mid = (48, 32, 22, 255)
    for y in range(11, 23):
        for x in range(10, 22):
            draw.point((x, y), panel_mid)
    draw.rectangle([9, 10, 22, 23], outline=panel_dark)

    return img

# -------------------------------------------------------------
# 1. COMMON (TIER 1): TIN L-BRACKETS & FLAT IRON LOCKPLATE
# -------------------------------------------------------------
def draw_tier1_common():
    img = draw_base_coffer(darken=False)
    draw = ImageDraw.Draw(img)

    hi = (210, 215, 220, 255)
    mid = (140, 145, 155, 255)
    dark = (75, 80, 90, 255)
    out = (35, 38, 45, 255)

    # 3x3 Tin L-brackets
    draw.line([(4, 5), (7, 5)], fill=hi)
    draw.line([(4, 5), (4, 8)], fill=hi)
    draw.point((5, 6), out) # Rivet

    draw.line([(24, 5), (27, 5)], fill=hi)
    draw.line([(27, 5), (27, 8)], fill=mid)
    draw.point((26, 6), out)

    draw.line([(4, 23), (4, 26)], fill=hi)
    draw.line([(4, 26), (7, 26)], fill=mid)
    draw.point((5, 25), out)

    draw.line([(27, 23), (27, 26)], fill=dark)
    draw.line([(24, 26), (27, 26)], fill=dark)
    draw.point((26, 25), out)

    # Center Clean Iron Lockplate (x: 13..18, y: 14..19)
    draw.rectangle([13, 14, 18, 19], fill=mid, outline=out)
    draw.line([(14, 14), (17, 14)], fill=hi)
    draw.line([(13, 15), (13, 18)], fill=hi)
    draw.line([(18, 15), (18, 18)], fill=dark)
    draw.line([(14, 19), (17, 19)], fill=dark)

    # Keyhole
    draw.point((15, 16), (20, 20, 25, 255))
    draw.point((16, 16), (20, 20, 25, 255))
    draw.point((15, 17), (20, 20, 25, 255))
    draw.point((16, 17), (20, 20, 25, 255))

    return img

# -------------------------------------------------------------
# 2. UNCOMMON (TIER 2): BRONZE CORNER PLATES & EMERALD GEM LATCH
# -------------------------------------------------------------
def draw_tier2_uncommon():
    img = draw_base_coffer(darken=False)
    draw = ImageDraw.Draw(img)

    bronze_hi = (245, 210, 150, 255)
    bronze_mid = (185, 125, 60, 255)
    bronze_dark = (105, 60, 25, 255)
    rivet = (45, 25, 10, 255)

    em_hi = (215, 255, 220, 255)
    em_light = (76, 217, 100, 255)
    em_mid = (46, 125, 50, 255)
    em_dark = (20, 60, 25, 255)

    # 5x5 Bronze Plates
    # TL
    for y in range(5, 9):
        draw.point((4, y), bronze_hi)
        draw.point((5, y), bronze_mid)
    for x in range(5, 9):
        draw.point((x, 5), bronze_hi)
        draw.point((x, 6), bronze_mid)
    draw.point((4, 5), bronze_hi)
    draw.point((6, 7), rivet)
    draw.point((7, 6), rivet)

    # TR
    for y in range(5, 9):
        draw.point((27, y), bronze_dark)
        draw.point((26, y), bronze_mid)
    for x in range(23, 27):
        draw.point((x, 5), bronze_hi)
        draw.point((x, 6), bronze_mid)
    draw.point((27, 5), bronze_mid)
    draw.point((25, 7), rivet)
    draw.point((24, 6), rivet)

    # BL
    for y in range(22, 26):
        draw.point((4, y), bronze_hi)
        draw.point((5, y), bronze_mid)
    for x in range(5, 9):
        draw.point((x, 26), bronze_dark)
        draw.point((x, 25), bronze_mid)
    draw.point((4, 26), bronze_mid)
    draw.point((6, 24), rivet)
    draw.point((7, 25), rivet)

    # BR
    for y in range(22, 26):
        draw.point((27, y), bronze_dark)
        draw.point((26, y), bronze_dark)
    for x in range(23, 27):
        draw.point((x, 26), bronze_dark)
        draw.point((x, 25), bronze_dark)
    draw.point((25, 24), rivet)
    draw.point((24, 25), rivet)

    # Bronze Medallion Bezel (x: 11..20, y: 12..21)
    draw.rectangle([11, 12, 20, 21], outline=bronze_mid)
    draw.line([(12, 12), (19, 12)], fill=bronze_hi)
    draw.line([(11, 13), (11, 20)], fill=bronze_hi)
    draw.line([(20, 13), (20, 20)], fill=bronze_dark)
    draw.line([(12, 21), (19, 21)], fill=bronze_dark)

    # Cut Emerald Gemstone Core (x: 13..18, y: 14..19)
    draw.rectangle([13, 14, 18, 19], fill=em_mid, outline=em_dark)
    draw.line([(14, 14), (17, 14)], fill=em_light)
    draw.line([(13, 15), (13, 18)], fill=em_light)
    draw.point((14, 15), em_hi) # Specular shine
    draw.point((15, 15), em_hi)
    draw.point((14, 16), em_hi)

    return img

# -------------------------------------------------------------
# 3. RARE (TIER 3): CHAMFERED COBALT ARMOR & SAPPHIRE GEMSTONE
# -------------------------------------------------------------
def draw_tier3_rare():
    img = draw_base_coffer(darken=False)
    draw = ImageDraw.Draw(img)

    cob_hi = (195, 235, 255, 255)
    cob_light = (85, 185, 255, 255)
    cob_mid = (35, 120, 225, 255)
    cob_dark = (18, 60, 130, 255)
    cob_out = (8, 25, 60, 255)

    saph_hi = (235, 250, 255, 255)
    saph_light = (65, 200, 255, 255)
    saph_mid = (15, 105, 235, 255)
    saph_dark = (5, 45, 130, 255)

    # 7x7 Chamfered Armor Corners with diagonal cuts
    # TL
    for y in range(5, 11):
        draw.point((4, y), cob_hi)
        draw.point((5, y), cob_light)
    for x in range(5, 11):
        draw.point((x, 5), cob_hi)
        draw.point((x, 6), cob_light)
    draw.line([(5, 10), (10, 5)], fill=cob_mid)
    draw.point((6, 7), cob_out)
    draw.point((8, 7), cob_out)

    # TR
    for y in range(5, 11):
        draw.point((27, y), cob_dark)
        draw.point((26, y), cob_mid)
    for x in range(21, 27):
        draw.point((x, 5), cob_hi)
        draw.point((x, 6), cob_light)
    draw.line([(26, 10), (21, 5)], fill=cob_mid)
    draw.point((25, 7), cob_out)
    draw.point((23, 7), cob_out)

    # BL
    for y in range(20, 26):
        draw.point((4, y), cob_hi)
        draw.point((5, y), cob_light)
    for x in range(5, 11):
        draw.point((x, 26), cob_dark)
        draw.point((x, 25), cob_mid)
    draw.line([(5, 21), (10, 26)], fill=cob_mid)
    draw.point((6, 24), cob_out)
    draw.point((8, 24), cob_out)

    # BR
    for y in range(20, 26):
        draw.point((27, y), cob_dark)
        draw.point((26, y), cob_dark)
    for x in range(21, 27):
        draw.point((x, 26), cob_dark)
        draw.point((x, 25), cob_dark)
    draw.line([(26, 21), (21, 26)], fill=cob_dark)
    draw.point((25, 24), cob_out)
    draw.point((23, 24), cob_out)

    # Vertical side armor bands
    for y in range(11, 20):
        draw.point((7, y), cob_light)
        draw.point((24, y), cob_mid)

    # Heavy Cobalt Bezel (x: 10..21, y: 11..22)
    draw.rectangle([10, 11, 21, 22], outline=cob_mid)
    draw.line([(11, 11), (20, 11)], fill=cob_hi)
    draw.line([(10, 12), (10, 21)], fill=cob_hi)
    draw.line([(21, 12), (21, 21)], fill=cob_dark)
    draw.line([(11, 22), (20, 22)], fill=cob_dark)

    # Radiant Faceted Sapphire Heart (x: 12..19, y: 13..20)
    draw.polygon([(15, 13), (16, 13), (19, 16), (19, 17), (16, 20), (15, 20), (12, 17), (12, 16)], fill=saph_mid, outline=saph_dark)
    draw.line([(14, 14), (16, 14)], fill=saph_light)
    draw.line([(13, 15), (13, 17)], fill=saph_light)
    draw.point((14, 15), saph_hi)
    draw.point((15, 15), saph_hi)
    draw.point((14, 16), saph_hi)
    draw.point((15, 16), (255, 255, 255, 255)) # Sparkle dot

    return img

# -------------------------------------------------------------
# 4. EPIC (TIER 4): WINGED GOTHIC FILIGREE & LUMINOUS AMETHYST CRYSTAL
# -------------------------------------------------------------
def draw_tier4_epic():
    img = draw_base_coffer(darken=True) # Deep ironwood contrast
    draw = ImageDraw.Draw(img)

    silver_hi = (255, 248, 255, 255)
    neon_violet = (230, 85, 255, 255)   # High-contrast luminous magenta-violet
    rich_amethyst = (165, 35, 215, 255)
    deep_purple = (75, 15, 105, 255)

    crys_hi = (255, 255, 255, 255)
    crys_light = (255, 175, 255, 255)
    crys_mid = (205, 55, 245, 255)
    crys_dark = (110, 20, 145, 255)

    # Winged gothic arches (8x8)
    # TL
    draw.line([(4, 5), (11, 5)], fill=silver_hi)
    draw.line([(4, 5), (4, 12)], fill=silver_hi)
    draw.line([(5, 6), (10, 6)], fill=neon_violet)
    draw.line([(5, 6), (5, 11)], fill=neon_violet)
    draw.point((6, 7), rich_amethyst)
    draw.point((7, 8), rich_amethyst)
    draw.point((11, 4), silver_hi)
    draw.point((4, 12), silver_hi)
    draw.point((6, 6), crys_hi) # Stud

    # TR
    draw.line([(20, 5), (27, 5)], fill=silver_hi)
    draw.line([(27, 5), (27, 12)], fill=rich_amethyst)
    draw.line([(21, 6), (26, 6)], fill=neon_violet)
    draw.line([(26, 6), (26, 11)], fill=neon_violet)
    draw.point((25, 7), deep_purple)
    draw.point((24, 8), deep_purple)
    draw.point((20, 4), silver_hi)
    draw.point((27, 12), rich_amethyst)
    draw.point((25, 6), crys_hi)

    # BL
    draw.line([(4, 19), (4, 26)], fill=silver_hi)
    draw.line([(4, 26), (11, 26)], fill=rich_amethyst)
    draw.line([(5, 20), (5, 25)], fill=neon_violet)
    draw.line([(5, 25), (10, 25)], fill=neon_violet)
    draw.point((6, 25), crys_hi)

    # BR
    draw.line([(27, 19), (27, 26)], fill=deep_purple)
    draw.line([(20, 26), (27, 26)], fill=deep_purple)
    draw.line([(26, 20), (26, 25)], fill=rich_amethyst)
    draw.line([(21, 25), (26, 25)], fill=rich_amethyst)
    draw.point((25, 25), crys_hi)

    # Gothic Crown Arch on lid (y: 3..5, x: 13..18)
    draw.point((13, 4), neon_violet)
    draw.point((14, 3), silver_hi)
    draw.point((15, 4), silver_hi)
    draw.point((16, 4), silver_hi)
    draw.point((17, 3), silver_hi)
    draw.point((18, 4), neon_violet)

    # Double Filigree Bezel (x: 9..22, y: 10..23)
    draw.rectangle([9, 10, 22, 23], outline=rich_amethyst)
    draw.rectangle([10, 11, 21, 22], outline=neon_violet)
    draw.point((9, 10), silver_hi)
    draw.point((22, 10), silver_hi)
    draw.point((9, 23), silver_hi)
    draw.point((22, 23), silver_hi)

    # Glowing Amethyst Crystal Cluster (x: 12..19, y: 13..20)
    draw.polygon([(15, 12), (16, 12), (19, 16), (18, 20), (14, 20), (12, 16)], fill=crys_mid, outline=crys_dark)
    draw.line([(14, 13), (16, 13)], fill=crys_light)
    draw.line([(13, 14), (13, 17)], fill=crys_light)
    draw.point((14, 14), crys_hi)
    draw.point((15, 15), crys_hi)
    draw.point((14, 15), crys_hi)
    draw.point((15, 14), (255, 255, 255, 255)) # Pure white sparkle star!

    return img

# -------------------------------------------------------------
# 5. MYTHIC (TIER 5): GILDED DRAGON CROWN, CORNER SPIKES & BURNING RUBY
# -------------------------------------------------------------
def draw_tier5_mythic():
    img = draw_base_coffer(darken=True)
    draw = ImageDraw.Draw(img)

    gold_hi = (255, 245, 180, 255)
    gold_mid = (255, 190, 35, 255)
    flame_red = (250, 45, 25, 255)
    ember_orange = (255, 135, 20, 255)

    ruby_hi = (255, 255, 255, 255)
    ruby_light = (255, 110, 110, 255)
    ruby_mid = (235, 20, 35, 255)
    ruby_dark = (120, 5, 15, 255)

    # Flared Corner Armor & Spikes
    # TL
    draw.line([(2, 3), (4, 5)], fill=gold_hi) # External spike
    draw.line([(4, 5), (12, 5)], fill=gold_hi)
    draw.line([(4, 5), (4, 13)], fill=gold_hi)
    draw.line([(5, 6), (11, 6)], fill=gold_mid)
    draw.line([(5, 6), (5, 12)], fill=gold_mid)
    draw.line([(6, 7), (10, 7)], fill=flame_red)

    # TR
    draw.line([(29, 3), (27, 5)], fill=gold_hi)
    draw.line([(19, 5), (27, 5)], fill=gold_hi)
    draw.line([(27, 5), (27, 13)], fill=gold_mid)
    draw.line([(20, 6), (26, 6)], fill=gold_mid)
    draw.line([(26, 6), (26, 12)], fill=flame_red)

    # BL
    draw.line([(2, 28), (4, 26)], fill=gold_hi)
    draw.line([(4, 18), (4, 26)], fill=gold_hi)
    draw.line([(4, 26), (12, 26)], fill=gold_mid)
    draw.line([(5, 25), (11, 25)], fill=flame_red)

    # BR
    draw.line([(29, 28), (27, 26)], fill=flame_red)
    draw.line([(27, 18), (27, 26)], fill=gold_mid)
    draw.line([(19, 26), (27, 26)], fill=gold_mid)

    # Royal Crown on lid (y: 1..5, x: 12..19) - 100% SYMMETRIC
    draw.line([(12, 4), (19, 4)], fill=gold_hi)
    # Center peak rises to y: 1
    draw.point((15, 1), (255, 255, 255, 255))
    draw.point((16, 1), (255, 255, 255, 255))
    draw.point((15, 2), gold_hi)
    draw.point((16, 2), gold_hi)
    draw.point((15, 3), gold_mid)
    draw.point((16, 3), gold_mid)
    # Outer peaks at y: 2
    draw.point((13, 2), (255, 255, 255, 255))
    draw.point((18, 2), (255, 255, 255, 255))
    draw.point((13, 3), gold_mid)
    draw.point((18, 3), gold_mid)

    # Floating Flame Embers (100% symmetric)
    draw.point((6, 16), ember_orange)
    draw.point((25, 16), ember_orange)
    draw.point((15, 7), ember_orange)
    draw.point((16, 7), ember_orange)
    draw.point((15, 26), ember_orange)
    draw.point((16, 26), ember_orange)

    # Sunburst Gold Bezel (x: 8..23, y: 9..24)
    draw.rectangle([8, 9, 23, 24], outline=gold_mid)
    draw.rectangle([9, 10, 22, 23], outline=flame_red)
    draw.point((8, 9), gold_hi)
    draw.point((23, 9), gold_hi)
    draw.point((8, 24), gold_hi)
    draw.point((23, 24), gold_hi)

    # Burning Heart Ruby Core (x: 12..19, y: 13..20)
    draw.polygon([(15, 12), (16, 12), (19, 15), (19, 17), (16, 20), (15, 20), (12, 17), (12, 15)], fill=ruby_mid, outline=ruby_dark)
    draw.line([(14, 13), (16, 13)], fill=ruby_light)
    draw.line([(13, 14), (13, 16)], fill=ruby_light)
    draw.point((14, 14), ruby_hi)
    draw.point((15, 15), ruby_hi)
    draw.point((14, 15), ruby_hi)
    draw.point((15, 14), (255, 255, 255, 255)) # Blazing white core gleam!

    return img

def scale_8x(img):
    return img.resize((img.width * 8, img.height * 8), Image.Resampling.NEAREST)

def run():
    print("Generating Final 5-Tier Gem-Centered Coffers...")
    tiers = {
        "coffer_common": draw_tier1_common(),
        "coffer_uncommon": draw_tier2_uncommon(),
        "coffer_rare": draw_tier3_rare(),
        "coffer_epic": draw_tier4_epic(),
        "coffer_mythic": draw_tier5_mythic(),
    }

    for name, img in tiers.items():
        # Save native 32x32
        img.save(os.path.join(FINAL_DIR, f"{name}.png"))
        # Save 8x scaled 256x256
        scale_8x(img).save(os.path.join(FINAL_DIR, f"{name}_256.png"))
        print(f"Generated: {name}.png (32x32 & 256x256)")

    print("All 5 final tier coffers generated in:", FINAL_DIR)

if __name__ == "__main__":
    run()
