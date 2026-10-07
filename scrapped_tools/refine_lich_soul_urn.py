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
    
    # Necrotic Lich Accents
    'R': (255, 60, 60, 255),      # Trapped red soul eye (#FF3C3C)
    'r': (180, 30, 45, 255),      # Deep ruby eye shadow (#B41E2D)
    'P': (180, 110, 220, 255),    # Twilight purple wisp (#B46EDC)
    'p': (120, 55, 160, 255),     # Deep purple shadow (#7837A0)
    'B': (235, 230, 220, 255),    # Ghostly bone (#EBE6DC)
    'v': (175, 165, 150, 255),    # Shaded bone (#AFA596)
}

# -------------------------------------------------------------
# CANDIDATE 2A: The Classic Canopic Reliquary (Pure Refined Urn)
# • Clean seamless glass aperture with diagonal specular glare 'L'
# • Swirling cyan soul fire with radiant white-hot core 'W'
# • Textbook top-left directional lighting across all brass components
# -------------------------------------------------------------
GRID_2A = [
    "      KyYK      ", # 0: Finial peak (width 4, 6sp)
    "     KyYYgK     ", # 1: Urn lid cap (width 6, 5sp)
    "      KgGK      ", # 2: Lid neck (width 4, 6sp)
    "    KyYYGgbK    ", # 3: Upper urn rim (width 8, 4sp)
    "   KyYYGGggbK   ", # 4: Upper shoulder bezel (width 10, 3sp)
    "  KyYLEeeeCGbK  ", # 5: Glass glare 'L', wide soul window (width 12, 2sp)
    "  KyYLEWeeCGbK  ", # 6: White-hot soul core 'W' (width 12, 2sp)
    "  KYGLeEeeCGbK  ", # 7: Swirling soul radiance (width 12, 2sp)
    "  KYGLceecCGbK  ", # 8: Deep spectral teal floor (width 12, 2sp)
    "  KgGCzzzzCGbK  ", # 9: Shadowed chamber base (width 12, 2sp)
    "   KYGGgggbbK   ", # 10: Urn waist ring (width 10, 3sp)
    "   KyYYGGggbK   ", # 11: Lower decorative band (width 10, 3sp)
    "    KgGGGGbK    ", # 12: Base plinth (width 8, 4sp)
    "     KggbbK     ", # 13: Foot pedestal (width 6, 5sp)
    "      KbbK      ", # 14: Base bottom rim (width 4, 6sp)
    "                "  # 15
]

# -------------------------------------------------------------
# CANDIDATE 2B: The Spectral Visage Phylactery (Trapped Lich Face & Red Eyes)
# • Perfectly aligned bone cranium 'BvvB' with twin piercing red eyes 'ReeR'
# • Ghostly skeletal jaw 'BvvB' submerged in swirling cyan soul mist
# -------------------------------------------------------------
GRID_2B = [
    "      KyYK      ", # 0: Finial peak (width 4, 6sp)
    "     KyYYgK     ", # 1: Urn lid cap (width 6, 5sp)
    "      KgGK      ", # 2: Lid neck (width 4, 6sp)
    "    KyYYGgbK    ", # 3: Upper urn rim (width 8, 4sp)
    "   KyYYGGggbK   ", # 4: Upper shoulder bezel (width 10, 3sp)
    "  KyYLBvvBCGbK  ", # 5: Bone cranium 'BvvB' framed in mist (width 12, 2sp)
    "  KyYLReeRCGbK  ", # 6: Twin glowing red soul eyes 'R' (width 12, 2sp)
    "  KYGLBvvBCGbK  ", # 7: Ghostly jawbone & nasal cavity (width 12, 2sp)
    "  KYGLceecCGbK  ", # 8: Deep spectral teal mist floor (width 12, 2sp)
    "  KgGCzzzzCGbK  ", # 9: Shadowed chamber base (width 12, 2sp)
    "   KYGGgggbbK   ", # 10: Urn waist ring (width 10, 3sp)
    "   KyYYGGggbK   ", # 11: Lower decorative band (width 10, 3sp)
    "    KgGGGGbK    ", # 12: Base plinth (width 8, 4sp)
    "     KggbbK     ", # 13: Foot pedestal (width 6, 5sp)
    "      KbbK      ", # 14: Base bottom rim (width 4, 6sp)
    "                "  # 15
]

# -------------------------------------------------------------
# CANDIDATE 2C: The Crowned Reliquary Urn (Royal 3-Point Lich Crown Lid)
# • Ornate 3-point miniature Twilight Lich crown resting atop the reliquary
# • Smooth continuous circlet and peaks, pure cyan soul within
# -------------------------------------------------------------
GRID_2C = [
    "      KyYK      ", # 0: Tall center crown peak (width 4, 6sp)
    "   KyKyYYgKgK   ", # 1: 3-point crown crest with 1-pixel notches (width 10, 3sp)
    "   KyYYYYGgbK   ", # 2: Crown base circlet band (width 10, 3sp)
    "    KgYYGGbK    ", # 3: Crown collar rim (width 8, 4sp)
    "   KyYYGGggbK   ", # 4: Upper shoulder bezel (width 10, 3sp)
    "  KyYLEeeeCGbK  ", # 5: Glass glare 'L', wide soul window (width 12, 2sp)
    "  KyYLEWeeCGbK  ", # 6: White-hot soul core 'W' (width 12, 2sp)
    "  KYGLeEeeCGbK  ", # 7: Swirling soul radiance (width 12, 2sp)
    "  KYGLceecCGbK  ", # 8: Deep spectral teal floor (width 12, 2sp)
    "  KgGCzzzzCGbK  ", # 9: Shadowed chamber base (width 12, 2sp)
    "   KYGGgggbbK   ", # 10: Urn waist ring (width 10, 3sp)
    "   KyYYGGggbK   ", # 11: Lower decorative band (width 10, 3sp)
    "    KgGGGGbK    ", # 12: Base plinth (width 8, 4sp)
    "     KggbbK     ", # 13: Foot pedestal (width 6, 5sp)
    "      KbbK      ", # 14: Base bottom rim (width 4, 6sp)
    "                "  # 15
]

# -------------------------------------------------------------
# CANDIDATE 2D: The Twilight Necrotic Vortex (Dual Cyan Mist & Violet Wisps)
# • Soul chamber swirls with both cyan soul energy and necrotic Twilight purple wisps
# • Dynamic arcane vortex aesthetic
# -------------------------------------------------------------
GRID_2D = [
    "      KyYK      ", # 0: Finial peak (width 4, 6sp)
    "     KyYYgK     ", # 1: Urn lid cap (width 6, 5sp)
    "      KgGK      ", # 2: Lid neck (width 4, 6sp)
    "    KyYYGgbK    ", # 3: Upper urn rim (width 8, 4sp)
    "   KyYYGGggbK   ", # 4: Upper shoulder bezel (width 10, 3sp)
    "  KyYLEeePCGbK  ", # 5: Glass glare 'L', purple wisp 'P' (width 12, 2sp)
    "  KyYLEWePCGbK  ", # 6: White-hot soul core 'W' and curling purple wisp 'P' (width 12, 2sp)
    "  KYGLPeEpCGbK  ", # 7: Necrotic purple energy swirl 'P'/'p' (width 12, 2sp)
    "  KYGLceepCGbK  ", # 8: Deep violet into teal (width 12, 2sp)
    "  KgGCzzzzCGbK  ", # 9: Shadowed chamber base (width 12, 2sp)
    "   KYGGgggbbK   ", # 10: Urn waist ring (width 10, 3sp)
    "   KyYYGGggbK   ", # 11: Lower decorative band (width 10, 3sp)
    "    KgGGGGbK    ", # 12: Base plinth (width 8, 4sp)
    "     KggbbK     ", # 13: Foot pedestal (width 6, 5sp)
    "      KbbK      ", # 14: Base bottom rim (width 4, 6sp)
    "                "  # 15
]

def render_sprite(grid, palette):
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    for y in range(16):
        row = grid[y]
        for x in range(16):
            ch = row[x]
            img.putpixel((x, y), palette.get(ch, (0, 0, 0, 0)))
    return img

def main():
    out_dir = r"scrapped_tools\preview_lich_soul_urn"
    artifact_dir = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405"
    os.makedirs(out_dir, exist_ok=True)
    
    variations = {
        "opt2a_classic_canopic": GRID_2A,
        "opt2b_spectral_visage": GRID_2B,
        "opt2c_crowned_reliquary": GRID_2C,
        "opt2d_twilight_vortex": GRID_2D,
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
        
        # Center crop (soul chamber zoom)
        crop_core = img.crop((2, 3, 14, 12)).resize((256, 192), Image.Resampling.NEAREST)
        p_crop = os.path.join(out_dir, f"{key}_core_crop256.png")
        crop_core.save(p_crop)
        
        shutil.copy2(p16, os.path.join(artifact_dir, f"{key}_16.png"))
        shutil.copy2(p256, os.path.join(artifact_dir, f"{key}_256.png"))
        shutil.copy2(p_crop, os.path.join(artifact_dir, f"{key}_core_crop256.png"))
        print(f"Verified & generated: {key}")

if __name__ == "__main__":
    main()
