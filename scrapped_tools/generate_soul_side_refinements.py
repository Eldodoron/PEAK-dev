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

def make_full_urn(soul_block):
    return [
        "      KyYK      ", # 0: Finial peak (width 4, 6sp)
        "     KyYYgK     ", # 1: Urn lid cap (width 6, 5sp)
        "      KgGK      ", # 2: Lid neck (width 4, 6sp)
        "    KyYYGgbK    ", # 3: Upper urn rim (width 8, 4sp)
        "   KyYYGGggbK   ", # 4: Upper shoulder bezel (width 10, 3sp)
        "  KyY" + soul_block[0] + "GbK  ", # 5: Soul chamber top (width 12, 2sp)
        "  KyY" + soul_block[1] + "GbK  ", # 6: Soul chamber core (width 12, 2sp)
        "  KYG" + soul_block[2] + "GbK  ", # 7: Soul chamber mid (width 12, 2sp)
        "  KYG" + soul_block[3] + "GbK  ", # 8: Soul chamber lower (width 12, 2sp)
        "  KgG" + soul_block[4] + "GbK  ", # 9: Soul chamber base (width 12, 2sp)
        "   KYGGgggbbK   ", # 10: Urn waist ring (width 10, 3sp)
        "   KyYYGGggbK   ", # 11: Lower decorative band (width 10, 3sp)
        "    KgGGGGbK    ", # 12: Base plinth (width 8, 4sp)
        "     KggbbK     ", # 13: Foot pedestal (width 6, 5sp)
        "      KbbK      ", # 14: Base bottom rim (width 4, 6sp)
        "                "  # 15
    ]

# -----------------------------------------------------------------
# 2A-1: Tapered Specular Glint & Dynamic Swirl
# Left flank: Specular highlight 'L' on rows 5 & 6, soft glass 'l' on row 7, body soul 'c' on row 8.
# Right flank: Shaded organically with swirl curvature ('C' -> 'z' -> 'C' -> 'z').
# -----------------------------------------------------------------
SOUL_2A1 = [
    "LEeeeC", # 5: Bright glint 'L', upper cyan mist, dark right 'C'
    "LEWeeC", # 6: Glint 'L', white-hot core 'W', deep shadow 'C'
    "leEEcz", # 7: Soft sheen 'l', glowing secondary swirl 'EE', shadow 'c', dark void 'z'
    "cceecC", # 8: Teal wraps around left 'c', soul body 'ee', right shade 'cC'
    "CczzzC"  # 9: Smooth organic floor
]

# -----------------------------------------------------------------
# 2A-2: Organic Curving Soul Flame
# The soul flame curves naturally away from the glass corners.
# Left flank: Glint 'L' at shoulder, vibrant flame 'e' reaches glass mid-left, soft 'c' at base.
# Right flank: Deep curved shadow 'C' -> 'C' -> 'z' -> 'C' conforming to cylinder shading.
# -----------------------------------------------------------------
SOUL_2A2 = [
    "LEeecC", # 5: Glint 'L', upper mist 'Eee', right shade 'cC'
    "lEWeeC", # 6: Soft sheen 'l', white core 'W', body 'ee', shadow 'C'
    "eEEecC", # 7: Radiant soul flame 'e' sweeps to left glass edge, right curve 'cC'
    "ceEeCz", # 8: Lower flame flare 'eEe', deep right shadow 'Cz'
    "CczzzC"  # 9: Rounded base
]

# -----------------------------------------------------------------
# 2A-3: Volumetric Radial Depth
# Shaded radially from the white-hot core outward to give maximum 3D cylindrical volume.
# Smooth gradient roll on both sides: no flat repeating vertical stripes.
# -----------------------------------------------------------------
SOUL_2A3 = [
    "cEeeec", # 5: Rounded upper dome: soft corners 'c', bright top mist
    "LEWeeC", # 6: Specular glint 'L', radiant core 'W', shadow 'C'
    "lEeeCz", # 7: Soft sheen 'l', cyan body 'Eee', deep right shadow 'Cz'
    "cceecC", # 8: Teal lower curve 'cc', right shadow 'cC'
    "CCzzCC"  # 9: Symmetrical shadowed base
]

# -----------------------------------------------------------------
# 2A-4: S-Curve Arcane Vortex
# Strong swirling vortex motion: flame curls in an S-path around the core.
# Sides have varied, non-linear pixels on every row.
# -----------------------------------------------------------------
SOUL_2A4 = [
    "LEeeEc", # 5: Glint 'L', wisp curls up-right 'E', soft edge 'c'
    "lEWeeC", # 6: Soft glint 'l', white core 'W', shadow 'C'
    "eeEEzc", # 7: Soul flare 'e' touches left glass, dark vortex eye 'z', soft rim 'c'
    "cceecC", # 8: Soul flame wraps left 'c', right shade 'cC'
    "CczzzC"  # 9: Organic floor
]

VARIATIONS = {
    "opt2a_1_tapered_swirl": make_full_urn(SOUL_2A1),
    "opt2a_2_curving_flame": make_full_urn(SOUL_2A2),
    "opt2a_3_volumetric_depth": make_full_urn(SOUL_2A3),
    "opt2a_4_s_vortex": make_full_urn(SOUL_2A4),
}

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
    
    for key, grid in VARIATIONS.items():
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
