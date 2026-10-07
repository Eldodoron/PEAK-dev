import os
import shutil
from PIL import Image

PALETTE = {
    ' ': (0, 0, 0, 0),
    'K': (16, 12, 18, 255),       # Pitch gothic outline (#100C12)
    'k': (32, 24, 36, 255),       # Soft gothic outline (#201824)
    
    # Twilight Gold / Royal Brass Ramp
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
    
    # Glass Glints
    'L': (210, 240, 250, 220),    # Bright glass reflection glint (#D2F0FA)
    'l': (140, 185, 205, 180),    # Soft glass reflection (#8CB9CD)
    
    # Necrotic Lich Accents
    'R': (255, 60, 60, 255),      # Trapped red soul eye (#FF3C3C)
    'P': (180, 110, 220, 255),    # Twilight purple wisp (#B46EDC)
    'p': (120, 55, 160, 255),     # Deep purple shadow (#7837A0)
    
    # Bone Accents (for skull variant)
    'B': (230, 225, 215, 255),    # Ghostly bone (#E6E1D7)
    'v': (170, 160, 145, 255),    # Shaded bone (#AAA091)
}

# -------------------------------------------------------------
# REFINEMENT 2A: The Crowned Soul Reliquary (Regal Amphora)
# • Miniature 3-point gold crown on the lid
# • Curved amphora handles framing the body
# • Clean glass window with specular glare and swirling soul
# -------------------------------------------------------------
GRID_2A = [
    "   KyK    KyK   ", # 0: Crown finial tips (width 10, 3sp)
    "   KyYy  KyYy   ", # 1: Crown side peaks (width 10, 3sp)
    "    KyYYYYyK    ", # 2: Crown base / lid crest (width 8, 4sp)
    "    KgYYYYgK    ", # 3: Golden lid rim (width 8, 4sp)
    "   KYGggggGgK   ", # 4: Urn neck ring (width 10, 3sp)
    "  KyYKKLLKKGgK  ", # 5: Glass shoulder with white reflection (width 12, 2sp)
    "  KYGKEeeCKGgK  ", # 6: Trapped soul fire 'E' (width 12, 2sp)
    "  KYGLeWEcKGgK  ", # 7: Radiant soul heart 'W' (width 12, 2sp)
    "  KYGKeEeCKGgK  ", # 8: Swirling vortex (width 12, 2sp)
    "  KgGKKccKKGgK  ", # 9: Lower glass bezel (width 12, 2sp)
    "   KYGggggGgK   ", # 10: Urn waist (width 10, 3sp)
    "   KyYYYYYYyK   ", # 11: Ornate decorative band (width 10, 3sp)
    "    KgGGGGgK    ", # 12: Base plinth (width 8, 4sp)
    "     KKKKKK     ", # 13: Foot pedestal (width 6, 5sp)
    "                ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# REFINEMENT 2B: The Spectral Visage Phylactery (Ghost Skull Inside)
# • Inside the cyan soul mist, the trapped skeletal face of the Lich peers out
# • Glowing red soul eyes shining through the mist
# -------------------------------------------------------------
GRID_2B = [
    "      KyyK      ", # 0: Golden urn finial (width 4, 6sp)
    "     KyYYyK     ", # 1: Urn lid cap (width 6, 5sp)
    "      KgGK      ", # 2: Lid neck (width 4, 6sp)
    "    KyYYYYgK    ", # 3: Upper urn rim (width 8, 4sp)
    "   KYGggggGgK   ", # 4: Filigree shoulder (width 10, 3sp)
    "  KyYKLeeLKGgK  ", # 5: Glass top with specular reflection 'L' (width 12, 2sp)
    "  KYGKeBvBeKgK  ", # 6: Cranium of the trapped soul 'BvB' (width 12, 2sp)
    "  KYGLeRReRLgK  ", # 7: Glowing red soul eyes 'R' peering out! (width 12, 2sp)
    "  KYGKeBvBeKgK  ", # 8: Ghostly skeletal jaw in cyan mist (width 12, 2sp)
    "  KgGKKccKKGgK  ", # 9: Lower glass bezel (width 12, 2sp)
    "   KYGggggGgK   ", # 10: Urn waist (width 10, 3sp)
    "   KyYYYYYYyK   ", # 11: Lower decorative band (width 10, 3sp)
    "    KgGGGGgK    ", # 12: Base plinth (width 8, 4sp)
    "     KKKKKK     ", # 13: Foot (width 6, 5sp)
    "                ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# REFINEMENT 2C: The Twilight Lantern Vortex (Cyan + Purple Wisps)
# • The soul fire swirls with both cyan and Twilight purple necrotic wisps
# • Elegant glass container with seamless brass framing (no awkward black pillars)
# -------------------------------------------------------------
GRID_2C = [
    "      KyyK      ", # 0: Golden urn finial (width 4, 6sp)
    "     KyYYyK     ", # 1: Urn lid cap (width 6, 5sp)
    "      KgGK      ", # 2: Lid neck (width 4, 6sp)
    "    KyYYYYgK    ", # 3: Upper urn rim (width 8, 4sp)
    "   KYGggggGgK   ", # 4: Filigree shoulder (width 10, 3sp)
    "  KyGKLEeCKGgK  ", # 5: Glass glare 'L', pure soul 'E' (width 12, 2sp)
    "  KYGLeWEcKGgK  ", # 6: White-hot soul core 'W' (width 12, 2sp)
    "  KYGKePePcKgK  ", # 7: Swirling purple Twilight wisps 'P' (width 12, 2sp)
    "  KYGKcecpKGgK  ", # 8: Cyan and purple mist (width 12, 2sp)
    "  KgGKKCCKKGgK  ", # 9: Lower glass bezel (width 12, 2sp)
    "   KYGggggGgK   ", # 10: Urn waist (width 10, 3sp)
    "   KyYYYYYYyK   ", # 11: Lower decorative band (width 10, 3sp)
    "    KgGGGGgK    ", # 12: Base plinth (width 8, 4sp)
    "     KKKKKK     ", # 13: Foot (width 6, 5sp)
    "                ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# REFINEMENT 2D: Pure Polished Canopic Urn (Seamless Glass Aperture)
# • Polished version of Option 2: removes internal black divider bars
# • The golden frame directly hugs the glowing soul chamber
# • Maximum clean readability and rich volumetric lighting
# -------------------------------------------------------------
GRID_2D = [
    "      KyyK      ", # 0: Golden urn finial (width 4, 6sp)
    "     KyYYyK     ", # 1: Urn lid cap (width 6, 5sp)
    "      KgGK      ", # 2: Lid neck (width 4, 6sp)
    "    KyYYYYgK    ", # 3: Upper urn rim (width 8, 4sp)
    "   KYGggggGgK   ", # 4: Filigree shoulder (width 10, 3sp)
    "  KyGLEeeeCGgK  ", # 5: Glass glare 'L', wide soul window (width 12, 2sp)
    "  KYGLEWeeCGgK  ", # 6: White-hot center 'W' (width 12, 2sp)
    "  KYGLeEeeCGgK  ", # 7: Swirling soul radiance (width 12, 2sp)
    "  KYGLccecCGgK  ", # 8: Deep spectral teal floor (width 12, 2sp)
    "  KgGKKccccKGgK ", # 9: Lower glass bezel (width 12, 2sp) -> wait, width 12: let's check length
    "   KYGggggGgK   ", # 10: Urn waist (width 10, 3sp)
    "   KyYYYYYYyK   ", # 11: Lower decorative band (width 10, 3sp)
    "    KgGGGGgK    ", # 12: Base plinth (width 8, 4sp)
    "     KKKKKK     ", # 13: Foot (width 6, 5sp)
    "                ", # 14
    "                "  # 15
]

# Fix row 9 of GRID_2D to be exactly length 16:
# "  KgGKKccccKGgK " has 2 spaces + 13 chars + 1 space!
# Change to: "  KgGKKcccKGgK  " (2 + 12 + 2 = 16)
GRID_2D[9] = "  KgGKKcccKGgK  "

def render_sprite(grid, palette):
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    for y in range(16):
        row = grid[y]
        assert len(row) == 16, f"Row {y} len={len(row)}: '{row}'"
        for x in range(16):
            ch = row[x]
            img.putpixel((x, y), palette.get(ch, (0, 0, 0, 0)))
    return img

def main():
    out_dir = r"scrapped_tools\preview_lich_soul_urn"
    artifact_dir = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405"
    os.makedirs(out_dir, exist_ok=True)
    
    variations = {
        "opt2a_crowned_reliquary": GRID_2A,
        "opt2b_spectral_visage": GRID_2B,
        "opt2c_twilight_vortex": GRID_2C,
        "opt2d_polished_canopic": GRID_2D,
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
        crop_core = img.crop((3, 4, 13, 11)).resize((256, 179), Image.Resampling.NEAREST)
        p_crop = os.path.join(out_dir, f"{key}_core_crop256.png")
        crop_core.save(p_crop)
        
        shutil.copy2(p16, os.path.join(artifact_dir, f"{key}_16.png"))
        shutil.copy2(p256, os.path.join(artifact_dir, f"{key}_256.png"))
        shutil.copy2(p_crop, os.path.join(artifact_dir, f"{key}_core_crop256.png"))
        print(f"Verified & generated: {key}")

if __name__ == "__main__":
    main()
