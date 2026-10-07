import os
import shutil
from PIL import Image

PALETTE = {
    ' ': (0, 0, 0, 0),
    'K': (15, 10, 25, 255),       # Deep void outline (#0F0A19)
    'k': (30, 20, 50, 255),       # Soft nebula outline (#1E1432)
    
    # Pure Celestial Starlight Core
    'W': (255, 255, 255, 255),    # Pure blinding white (#FFFFFF)
    'w': (245, 238, 255, 255),    # Starlight glimmer (#F5EEFF)
    
    # Cosmic Spectrum: Magenta & Pink
    'M': (255, 125, 200, 255),    # Radiant cosmic pink (#FF7DC8)
    'm': (215, 55, 145, 255),     # Deep nebula magenta (#D73791)
    
    # Cosmic Spectrum: Astral Violet & Purple
    'P': (190, 115, 255, 255),    # Vivid astral violet (#BE73FF)
    'p': (130, 60, 210, 255),     # Cosmic purple (#823CD2)
    'D': (70, 25, 135, 255),      # Dark void violet (#461987)
    
    # Cosmic Spectrum: Celestial Cyan & Azure
    'E': (135, 240, 255, 255),    # Radiant starlight cyan (#87F0FF)
    'e': (60, 190, 230, 255),     # Astral sky blue (#3CBE7E6)
    'c': (28, 115, 180, 255),     # Deep space azure (#1C73B4)
    'C': (18, 75, 130, 255),      # Abyssal blue (#124B82)
    'Z': (12, 40, 80, 255),       # Dark void ocean (#0C2850)
    
    # Cosmic Spectrum: Starlight Lime / Emerald
    'A': (175, 245, 115, 255),    # Astral auroral green (#AFF573)
    'a': (105, 205, 65, 255),     # Cosmic emerald (#69CD41)
    
    # Solar Gold & Amber (§6 Infinity Gold Theme)
    'Y': (255, 235, 125, 255),    # Specular solar gold (#FFE87D)
    'y': (240, 180, 45, 255),     # Radiant cosmic gold (#F0B42D)
    'O': (210, 115, 25, 255),     # Solar amber (#D27319)
    'o': (140, 60, 15, 255),      # Dark amber bronze (#8C3C0F)
    'g': (170, 125, 25, 255),     # Antique brass shade (#AA7D19)
}

# -------------------------------------------------------------
# CANDIDATE 1: The Prismatic Star Shard (Avaritia Cosmic Crystal)
# • Sharp, crystalline celestial shard that chipped from the Infinity Catalyst
# -------------------------------------------------------------
GRID_1 = [
    "       KK       ", # 0
    "      KWWK      ", # 1
    "     KWWwMK     ", # 2
    "    KwWWwMPK    ", # 3
    "    KwEwwMPK    ", # 4
    "   KwEEwwMPpK   ", # 5
    "   KEeEwwMPDK   ", # 6
    "    KeewwMpK    ", # 7
    "    KcewmpPK    ", # 8
    "     KcwPpK     ", # 9
    "     KcppDK     ", # 10
    "      KcpK      ", # 11
    "      KZDK      ", # 12
    "       KK       ", # 13
    "                ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# CANDIDATE 2: The Cosmic Nova Starburst (Catalyst Pinwheel Star)
# • Radiant 8-ray starburst directly inspired by the Avaritia Catalyst star
# • Crisp rays: magenta top, violet right, azure bottom, cyan left, with diagonal sparks
# -------------------------------------------------------------
GRID_2 = [
    "       KK       ", # 0: Top magenta ray tip (width 2, 7sp)
    "      KMMK      ", # 1: Magenta ray (width 4, 6sp)
    "      KmwK      ", # 2: Ray neck (width 4, 6sp)
    "     KMwWMK     ", # 3: Diagonal magenta sparks (width 6, 5sp)
    "   KKMwWWwMKK   ", # 4: Diagonal sparks flare (width 10, 3sp)
    "  KeEwWWWWwPpK  ", # 5: Arm shoulders: Cyan to Violet (width 12, 2sp)
    " KEEewWWWWwePPK ", # 6: Horizontal arm span (width 14, 1sp)
    "  KeEwWWWWwPpK  ", # 7: Lower arm shoulders (width 12, 2sp)
    "   KKAwWWwAKK   ", # 8: Lower diagonal auroral green sparks (width 10, 3sp)
    "     KAwWAK     ", # 9: Lower diagonal sparks (width 6, 5sp)
    "      KaeK      ", # 10: Azure lower ray neck (width 4, 6sp)
    "      KeeK      ", # 11: Azure lower ray (width 4, 6sp)
    "       KK       ", # 12: Bottom ray tip (width 2, 7sp)
    "                ", # 13
    "                ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# CANDIDATE 3: The Celestial Relic Shard (Gold-Clad Cosmic Crystal)
# • Unifies the §6 Gold name with the Avaritia Cosmic Crystal
# • A sharp prismatic cosmic starlight shard cradled in antique gold filigree claws
# -------------------------------------------------------------
GRID_3 = [
    "      KyyK      ", # 0: width 4, 6sp
    "     KyYYgK     ", # 1: width 6, 5sp
    "    KyYWWYgK    ", # 2: width 8, 4sp
    "   KyYWWwMYgK   ", # 3: width 10, 3sp
    "  KyYwWWwMPGgK  ", # 4: width 12, 2sp
    "  KYEwEwMPpGbK  ", # 5: 2sp + 12 + 2sp = 16
    "  KYEewMpPpGbK  ", # 6: 2sp + 12 + 2sp = 16
    "  KYcewmPpDGbK  ", # 7: 2sp + 12 + 2sp = 16
    "   KgGcwPpDGK   ", # 8: 3sp + 10 + 3sp = 16
    "   KgGcpppDGK   ", # 9: 3sp + 10 + 3sp = 16
    "    KgGcpDGK    ", # 10: 4sp + 8 + 4sp = 16: "KgGcpDGK" = 8 chars!
    "     KgZDGK     ", # 11: 5sp + 6 + 5sp = 16: "KgZDGK" = 6 chars!
    "      KggK      ", # 12: 6sp + 4 + 6sp = 16: "KggK" = 4 chars!
    "       KK       ", # 13: 7sp + 2 + 7sp = 16: "KK" = 2 chars!
    "                ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# CANDIDATE 4: The Cosmic Octahedron (Faceted Diamond Gem)
# • Classic faceted diamond / octahedron cut gem pulsing with the Avaritia spectrum
# • High-contrast facet shading: white top table, prismatic crown, deep void pavilion
# -------------------------------------------------------------
GRID_4 = [
    "      KKKK      ", # 0: Gem table top edge (width 4, 6sp)
    "    KKWWWWKK    ", # 1: Brilliant starlight table (width 8, 4sp)
    "   KWWWWWWwwK   ", # 2: Diamond table facet (width 10, 3sp)
    "  KwwWWWWWWwwK  ", # 3: Upper crown facet (width 12, 2sp)
    " KEEEwWWWWwPPPK ", # 4: Prismatic girdle: Astral Cyan to Violet (width 14, 1sp)
    " KEEEewWWwePPPK ", # 5: Girdle line (width 14, 1sp)
    "  KeEewWWwePpK  ", # 6: Pavilion slope begins (width 12, 2sp)
    "  KeeewWWwePpK  ", # 7: Pavilion facets (width 12, 2sp)
    "   KcewWWwpPK   ", # 8: Tapering pavilion (width 10, 3sp)
    "   KcewWWwpDK   ", # 9: Deep space facets (width 10, 3sp)
    "    KcwWWpDK    ", # 10: Deepening void (width 8, 4sp)
    "    KcwWWpDK    ", # 11: Lower pavilion (width 8, 4sp)
    "     KZwPDK     ", # 12: Culet approach (width 6, 5sp)
    "      KZDK      ", # 13: Culet point (width 4, 6sp)
    "       KK       ", # 14: Culet tip (width 2, 7sp)
    "                "  # 15
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
    out_dir = r"scrapped_tools\preview_infinity_fragment"
    artifact_dir = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405"
    os.makedirs(out_dir, exist_ok=True)
    
    candidates = {
        "opt1_prismatic_shard": GRID_1,
        "opt2_catalyst_star": GRID_2,
        "opt3_celestial_relic": GRID_3,
        "opt4_cosmic_octahedron": GRID_4,
    }
    
    for key, grid in candidates.items():
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
        
        # Center crop (zoom)
        crop = img.crop((1, 1, 15, 15)).resize((256, 256), Image.Resampling.NEAREST)
        p_crop = os.path.join(out_dir, f"{key}_crop256.png")
        crop.save(p_crop)
        
        shutil.copy2(p16, os.path.join(artifact_dir, f"{key}_16.png"))
        shutil.copy2(p256, os.path.join(artifact_dir, f"{key}_256.png"))
        shutil.copy2(p_crop, os.path.join(artifact_dir, f"{key}_crop256.png"))
        print(f"Verified & generated: {key}")

if __name__ == "__main__":
    main()
