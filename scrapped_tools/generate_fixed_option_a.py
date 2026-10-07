import os
from PIL import Image

PALETTE = {
    ' ': (0, 0, 0, 0),          # Transparent
    'K': (7, 40, 56, 255),       # Deep glacial shadow outline (#072838)
    'D': (27, 114, 137, 255),    # Dark glacial cyan (#1B7289)
    'M': (71, 189, 218, 255),    # Crystal facet midtone (#47BDDA)
    'B': (57, 199, 236, 255),    # Vibrant electric cyan (#39C7EC)
    'G': (105, 255, 255, 255),   # Glowing frost highlight (#69FFFF)
    'W': (255, 255, 255, 255),   # Specular white reflection (#FFFFFF)
}

# REV 1: Symmetrical Rim-Light Balance (Recommended)
# Primary glint on left lobe, secondary specular glint on right lobe,
# clean facet gradient, 100% mathematically symmetric outline.
REV_1 = [
    "                ", # 0
    "   KK      KK   ", # 1
    "  KWWK    KGWK  ", # 2
    " KWWGBK  KGBMDK ", # 3
    " KWGGBMKKGBMDDK ", # 4
    " KWGBBBMDGBMDDK ", # 5
    " KGBBBMMDMMDDDK ", # 6
    "  KGBBMMDMMDDK  ", # 7
    "  KBBMGMDMDDDK  ", # 8
    "   KBMMDMDDDK   ", # 9
    "    KBMDDDDK    ", # 10
    "     KMDDDK     ", # 11
    "      KMDK      ", # 12
    "       KK       ", # 13
    "                ", # 14
    "                "  # 15
]

# REV 2: Pure Directional Lighting (Classic Minecraft Style)
# Light strictly from top-left, shaded right lobe, sharp diagonal cut.
REV_2 = [
    "                ", # 0
    "   KK      KK   ", # 1
    "  KWWK    KGDK  ", # 2
    " KWWGBK  KGBMDK ", # 3
    " KWGGBMKKGBMDDK ", # 4
    " KWGBBBMDGBMDDK ", # 5
    " KGBBBMMDMMDDDK ", # 6
    "  KGBBMMDMMDDK  ", # 7
    "  KBBMGMDMDDDK  ", # 8
    "   KBMMDMDDDK   ", # 9
    "    KBMDDDDK    ", # 10
    "     KMDDDK     ", # 11
    "      KMDK      ", # 12
    "       KK       ", # 13
    "                ", # 14
    "                "  # 15
]

# REV 3: Luminous Frost Core (Inner Chamber Glow)
# Glowing internal cyan core flanked by symmetrical crystal facet walls.
REV_3 = [
    "                ", # 0
    "   KK      KK   ", # 1
    "  KWWK    KWWK  ", # 2
    " KWWGBK  KBGWDK ", # 3
    " KWGBBMKKMBBGDK ", # 4
    " KWGBGGWWGGBMDK ", # 5
    " KGBBGGWWGGBMDK ", # 6
    "  KBBGGWWGGBDK  ", # 7
    "  KBBMBGGGBMDK  ", # 8
    "   KBMMDMDDDK   ", # 9
    "    KBMDMDDK    ", # 10
    "     KMDDDK     ", # 11
    "      KMDK      ", # 12
    "       KK       ", # 13
    "                ", # 14
    "                "  # 15
]

# REV 4: Slender Icicle Apex (Extended Sharp Glacial Needle)
# 1-pixel extended vertical drop at the bottom tip for an icicle aesthetic.
REV_4 = [
    "                ", # 0
    "   KK      KK   ", # 1
    "  KWWK    KGWK  ", # 2
    " KWWGBK  KGBMDK ", # 3
    " KWGGBMKKGBMDDK ", # 4
    " KWGBBBMDGBMDDK ", # 5
    " KGBBBMMDMMDDDK ", # 6
    "  KGBBMMDMMDDK  ", # 7
    "  KBBMGMDMDDDK  ", # 8
    "   KBMMDMDDDK   ", # 9
    "    KBMDDDDK    ", # 10
    "     KMDDDK     ", # 11
    "      KMDK      ", # 12
    "       KK       ", # 13
    "       KK       ", # 14
    "                "  # 15
]

def verify_and_build(name, grid):
    for y, r in enumerate(grid):
        assert len(r) == 16, f"{name} Row {y} len={len(r)}"
        left_mask = ''.join('#' if c != ' ' else '.' for c in r[:8])
        right_mask = ''.join('#' if c != ' ' else '.' for c in r[8:])
        assert left_mask == right_mask[::-1], f"{name} Row {y} asymmetry: {left_mask} vs {right_mask[::-1]}"
    
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    for y in range(16):
        for x in range(16):
            ch = grid[y][x]
            img.putpixel((x, y), PALETTE.get(ch, (0, 0, 0, 0)))
    return img

if __name__ == '__main__':
    out_dir = r"scrapped_tools\preview_frozen_heart"
    os.makedirs(out_dir, exist_ok=True)

    variations = {
        "opt_a_fixed_balanced": REV_1,
        "opt_a_fixed_directional": REV_2,
        "opt_a_fixed_luminous": REV_3,
        "opt_a_fixed_needle": REV_4,
    }

    for name, g in variations.items():
        img = verify_and_build(name, g)
        img.save(os.path.join(out_dir, f"{name}_16.png"))
        upscaled = img.resize((256, 256), Image.Resampling.NEAREST)
        upscaled.save(os.path.join(out_dir, f"{name}_256.png"))
        print(f"Verified 100% symmetry & generated: {name}")
