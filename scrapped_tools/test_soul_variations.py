import os
import shutil
from PIL import Image

PALETTE = {
    ' ': (0, 0, 0, 0),
    'K': (16, 12, 18, 255),       # Pitch gothic outline (#100C12)
    'k': (32, 24, 36, 255),       # Soft gothic outline (#201824)
    
    # Twilight Gold / Royal Brass Ramp (Top-Left key light)
    'y': (255, 238, 135, 255),    # High specular gold (#FFEE87)
    'Y': (235, 188, 50, 255),     # Radiant Twilight gold (#EBBC32)
    'G': (175, 128, 28, 255),     # Rich antique gold (#AF801C)
    'g': (110, 72, 16, 255),      # Dark shadowed brass (#6E4810)
    'b': (65, 42, 10, 255),       # Deepest brass shadow (#412A0A)
    
    # Spectral Soul Energy Ramp (Cyan / Mint / Teal)
    'W': (255, 255, 255, 255),    # Pure soul brilliance (#FFFFFF)
    'E': (220, 255, 250, 255),    # White-cyan soul core (#DCFFFA)
    'e': (115, 240, 220, 255),    # Vivid cyan soul fire (#73F0DC)
    'c': (50, 180, 165, 255),     # Twilight soul teal (#32B4A5)
    'C': (24, 105, 98, 255),      # Deep spectral shadow (#186962)
    'z': (12, 55, 52, 255),       # Darkest soul abyss (#0C3734)
    
    # Glass Glints & Reflections
    'L': (210, 240, 250, 230),    # Bright glass reflection glint (#D2F0FA)
    'l': (140, 185, 205, 190),    # Soft glass reflection (#8CB9CD)
}

def build_urn(soul_lines):
    return [
        "      KyYK      ", # 0
        "     KyYYgK     ", # 1
        "      KgGK      ", # 2
        "    KyYYGgbK    ", # 3
        "   KyYYGGggbK   ", # 4
        "  KyY" + soul_lines[0] + "GbK  ", # 5
        "  KyY" + soul_lines[1] + "GbK  ", # 6
        "  KYG" + soul_lines[2] + "GbK  ", # 7
        "  KYG" + soul_lines[3] + "GbK  ", # 8
        "  KgG" + soul_lines[4] + "GbK  ", # 9
        "   KYGGgggbbK   ", # 10
        "   KyYYGGggbK   ", # 11
        "    KgGGGGbK    ", # 12
        "     KggbbK     ", # 13
        "      KbbK      ", # 14
        "                "  # 15
    ]

# Original 2A soul:
# "LEeeeC"
# "LEWeeC"
# "LeEeeC"
# "LceecC"
# "CzzzzC"
# Notice col 0 is all L (L, L, L, L, C) and col 5 is all C (C, C, C, C, C)

# Sub-option 2A-1: Natural Curved Glass Glint & Swirling Soul Flanks
# Left side has specular glint L at top, soft sheen l on mid-upper, vibrant soul fire e touching the edge, then teal shadow c.
# Right side breaks the flat wall with dynamic swirl: top mist c, deep shadow C, dark core z, bottom rim C.
SOUL_1 = [
    "LEeeeC", # 5: Bright glint L, soft shadow C
    "LEWezc", # 6: Specular L, brilliant core W, swirling abyss z, soft rim c
    "leEEcz", # 7: Soft glass sheen l, glowing vortex eEE, shadow c, void z
    "cceecC", # 8: Lower soul wraps to left c, teal body ee, right shade cC
    "CczzzC"  # 9: Organic shaded floor
]

# Sub-option 2A-2: Dynamic Ethereal Flame (Flame Wisps curling away from glass)
# The soul flame curls inward, creating distinct luminous contours and curved glass shading on both sides
SOUL_2 = [
    "LEeecC", # 5: Glint L, upper mist, right shade cC
    "lEWeeC", # 6: Soft sheen l, white core W, deep shadow C
    "eEEecC", # 7: Radiant soul fire e breaks out to the left flank, right curve cC
    "ceEeCz", # 8: Teal base c, secondary flare E, deep right shadow Cz
    "CczzCC"  # 9: Rounded base
]

# Sub-option 2A-3: S-Vortex Soul (Arcane Swirl with Curving Glass Edge)
# Strong S-shaped swirl: top flame curves right, mid-flame curls around white core, bottom sweeps left
SOUL_3 = [
    "LEeeEc", # 5: Glint L, upper wisp curls up to top-right E, soft edge c
    "lEWeeC", # 6: Soft glint l, white core W, shadow C
    "eeEEzc", # 7: Soul flare e touches left glass, dark vortex eye z, soft rim c
    "cceecC", # 8: Lower soul wraps left c, teal body ee, shadow cC
    "CzzzzC"  # 9: Shadowed base
]

# Sub-option 2A-4: Pure Volumetric Sphere / Radial Soul Shading
# Shaded radially from the white core outwards: rounded contours that curve naturally inside the cylindrical urn
SOUL_4 = [
    "cEeeec", # 5: Soft upper dome, rounded corners c
    "LEWeeC", # 6: Specular glare L, radiant core W, shadow C
    "lEeeCz", # 7: Soft glare l, glowing soul, deep shadow Cz
    "cceeCC", # 8: Rounded lower soul, deep right shadow CC
    "CCzzCC"  # 9: Symmetrical dark floor
]

def render_sprite(grid, palette):
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    for y in range(16):
        row = grid[y]
        assert len(row) == 16, f"row {y} len {len(row)} != 16: '{row}'"
        for x in range(16):
            ch = row[x]
            img.putpixel((x, y), palette.get(ch, (0, 0, 0, 0)))
    return img

def main():
    out_dir = r"scrapped_tools\preview_lich_soul_urn"
    artifact_dir = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405"
    os.makedirs(out_dir, exist_ok=True)
    
    variations = {
        "opt2a_1_swirl_flanks": build_urn(SOUL_1),
        "opt2a_2_ethereal_flame": build_urn(SOUL_2),
        "opt2a_3_s_vortex": build_urn(SOUL_3),
        "opt2a_4_volumetric_sphere": build_urn(SOUL_4),
    }
    
    for key, grid in variations.items():
        assert len(grid) == 16, f"{key} row count != 16"
        for y, r in enumerate(grid):
            assert len(r) == 16, f"{key} row {y} len {len(r)} != 16: '{r}'"
            stripped = r.strip()
            if stripped:
                lead_sp = len(r) - len(r.lstrip())
                trail_sp = len(r) - len(r.rstrip())
                assert lead_sp == trail_sp, f"{key} row {y} not centered: lead={lead_sp}, trail={trail_sp}: '{r}'"
        
        img = render_sprite(grid, PALETTE)
        p16 = os.path.join(out_dir, f"{key}_16.png")
        p256 = os.path.join(out_dir, f"{key}_256.png")
        img.save(p16)
        upscaled = img.resize((256, 256), Image.Resampling.NEAREST)
        upscaled.save(p256)
        
        crop_core = img.crop((2, 3, 14, 12)).resize((256, 192), Image.Resampling.NEAREST)
        p_crop = os.path.join(out_dir, f"{key}_core_crop256.png")
        crop_core.save(p_crop)
        
        shutil.copy2(p16, os.path.join(artifact_dir, f"{key}_16.png"))
        shutil.copy2(p256, os.path.join(artifact_dir, f"{key}_256.png"))
        shutil.copy2(p_crop, os.path.join(artifact_dir, f"{key}_core_crop256.png"))
        print(f"Verified & generated: {key}")

if __name__ == "__main__":
    main()
