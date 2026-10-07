import os
import shutil
from PIL import Image

PALETTE = {
    ' ': (0, 0, 0, 0),
    'K': (16, 12, 18, 255),       # Pitch gothic outline (#100C12)
    
    # Twilight Gold / Royal Brass (Lich Crown & Filigree)
    'y': (255, 235, 125, 255),    # High specular gold (#FFE77D)
    'Y': (235, 185, 45, 255),     # Radiant Twilight gold (#EBB92D)
    'G': (175, 125, 25, 255),     # Rich antique gold (#AF7D19)
    'g': (105, 70, 15, 255),      # Dark shadowed brass (#69460F)
    
    # Bone / Skeletal Ivory
    'W': (240, 235, 225, 255),    # Bleached bone highlight (#F0EBE1)
    'w': (205, 195, 175, 255),    # Bone midtone (#CDC3AF)
    'v': (155, 140, 120, 255),    # Shadowed bone (#9B8C78)
    'V': (95, 80, 65, 255),       # Deep bone shadow (#5F5041)
    
    # Lich Glowing Eyes / Red Soul Fire
    'R': (255, 60, 60, 255),      # Incandescent red soul eye (#FF3C3C)
    'r': (180, 20, 25, 255),      # Deep crimson eye shadow (#B41419)
    
    # Spectral Soul Glow (Cyan / Ender Mist)
    'E': (220, 255, 250, 255),    # Pure soul light (#DCFFFA)
    'e': (110, 235, 215, 255),    # Vivid cyan soul fire (#6EEBD7)
    'c': (45, 175, 160, 255),     # Twilight soul teal (#2DAFA0)
    'C': (20, 95, 90, 255),       # Deep spectral shadow (#145F5A)
    
    # Royal Twilight Robe Purple
    'P': (185, 115, 225, 255),    # Velvet purple highlight (#B973E1)
    'p': (130, 65, 170, 255),     # Royal Twilight purple (#8241AA)
    'u': (75, 30, 105, 255),      # Dark velvet shadow (#4B1E69)
    'U': (40, 15, 60, 255),       # Deep robe shadow (#280F3C)
}

# -------------------------------------------------------------
# OPTION 1: The Crowned Skull Reliquary (Iconic Twilight Lich)
# Golden crowned skeletal reliquary with glowing red eyes peering from darkness
# -------------------------------------------------------------
GRID_OPT1 = [
    "  KyK      KyK  ", # 0: Crown spires (width 12, 2sp)
    "  KYYK    KYYK  ", # 1: Crown side peaks (width 12, 2sp)
    "  KyYYYYYYYYyK  ", # 2: Full golden crown brow (width 12, 2sp)
    "  KYGggggggGYK  ", # 3: Crown band trim (width 12, 2sp)
    "  KgWWWWWWWWgK  ", # 4: Golden crown brow / skull cranium (width 12, 2sp)
    "  KWwwwwwwwwWK  ", # 5: Smooth bone forehead (width 12, 2sp)
    "  KwKKwwwwKKwK  ", # 6: Upper eye socket brow (width 12, 2sp)
    "  KwKRRwwRRKwK  ", # 7: Glowing red Lich eyes! (width 12, 2sp)
    "  KvwKwKKwKwvK  ", # 8: Bone cheeks with nasal cavity 'KK' (width 12, 2sp)
    "   KVvwwwwVVK   ", # 9: Cheekbones (width 10, 3sp)
    "   KgWWWWWWgK   ", # 10: Golden jaw brace (width 10, 3sp)
    "   KwKwvvvKwK   ", # 11: Skeletal teeth (width 10, 3sp)
    "    KvvvvvvK    ", # 12: Jaw base (width 8, 4sp)
    "     KKGGKK     ", # 13: Reliquary pedestal (width 6, 5sp)
    "      KKKK      ", # 14: Base finial (width 4, 6sp)
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 2: The Twilight Soul Urn (Ethereal Spectral Canister)
# Gothic brass urn with an arcane glass aperture revealing the trapped swirling soul
# -------------------------------------------------------------
GRID_OPT2 = [
    "      KyyK      ", # 0: Golden urn finial (width 4, 6sp)
    "     KyYYyK     ", # 1: Urn lid cap (width 6, 5sp)
    "      KgGK      ", # 2: Lid neck (width 4, 6sp)
    "    KyYYYYgK    ", # 3: Upper urn rim (width 8, 4sp)
    "   KYGggggGgK   ", # 4: Filigree shoulder (width 10, 3sp)
    "  KyGKEeeCKGgK  ", # 5: Glass window with swirling soul (width 12, 2sp)
    "  KYGKeEeCKGgK  ", # 6: Pure soul light 'E' (width 12, 2sp)
    "  KYGKceEcKGgK  ", # 7: Swirling spectral vortex (width 12, 2sp)
    "  KYGKceecKGgK  ", # 8: Deep soul teal (width 12, 2sp)
    "  KgGKKCCKKGgK  ", # 9: Lower glass bezel (width 12, 2sp)
    "   KYGggggGgK   ", # 10: Urn waist (width 10, 3sp)
    "   KyYYYYYYyK   ", # 11: Lower decorative band (width 10, 3sp)
    "    KgGGGGgK    ", # 12: Base plinth (width 8, 4sp)
    "     KKKKKK     ", # 13: Foot (width 6, 5sp)
    "                ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 3: The Cursed Twilight Amulet (Remake of Old Medallion)
# Heavy antique gold medallion cradling a glowing spectral Ender gem
# -------------------------------------------------------------
GRID_OPT3 = [
    "      KKKK      ", # 0: Suspension ring (width 4, 6sp)
    "      KyyK      ", # 1: Golden bail (width 4, 6sp)
    "     KyYYyK     ", # 2: Amulet crest (width 6, 5sp)
    "   KKyYYYYgKK   ", # 3: Upper golden bezel (width 10, 3sp)
    "  KyYYGggGYYgK  ", # 4: Heavy filigree (width 12, 2sp)
    "  KYYGKEeCKGgK  ", # 5: Glowing spectral gem facets (width 12, 2sp)
    "  KYGKEEEcCKgK  ", # 6: Gem table: brilliant soul light (width 12, 2sp)
    "  KYGKeEEccKgK  ", # 7: Inner refractions (width 12, 2sp)
    "  KgGKceEccKgK  ", # 8: Deep teal gem facets (width 12, 2sp)
    "  KgGKKcccKKgK  ", # 9: Lower gem bezel (width 12, 2sp)
    "  KyYYGgggGYYK  ", # 10: Lower golden frame (width 12, 2sp)
    "   KKyYYYYgKK   ", # 11: Bottom bezel (width 10, 3sp)
    "     KgYYgK     ", # 12: Lower crest (width 6, 5sp)
    "      KggK      ", # 13: Pendant teardrop finial (width 4, 6sp)
    "       KK       ", # 14: Tip (width 2, 7sp)
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 4: The Tome of the Lich (Bound Grimoire Phylactery)
# Royal purple velvet spellbook bound in brass & bone with a crowned skull seal
# -------------------------------------------------------------
GRID_OPT4 = [
    "   KKKKKKKKKK   ", # 0: Grimoire top edge (width 10, 3sp)
    "  KyYYYYYYYYyK  ", # 1: Golden corner brackets & spine head (width 12, 2sp)
    "  KYgPpuuupGgK  ", # 2: Royal velvet cover with brass corners (width 12, 2sp)
    "  KYgPpuuupGgK  ", # 3: Purple velvet (width 12, 2sp)
    "  KYgPKyYyKGgK  ", # 4: Golden crown grimoire lock (width 12, 2sp)
    "  KYgPKwRRwKGK  ", # 5: Skeletal skull with glowing red eyes! (width 12, 2sp)
    "  KYgPKwwwwKGK  ", # 6: Skull emblem center (width 12, 2sp)
    "  KYgPKKvvKKGK  ", # 7: Skull jaw (width 12, 2sp)
    "  KYgPpuuupGgK  ", # 8: Purple velvet lower cover (width 12, 2sp)
    "  KYgPpuuupGgK  ", # 9: Velvet field (width 12, 2sp)
    "  KyYYYYYYYYyK  ", # 10: Golden corner brackets & tail (width 12, 2sp)
    "   KKKKKKKKKK   ", # 11: Tome bottom edge (width 10, 3sp)
    "  KwwwwwwwwwwK  ", # 12: Weathered ancient parchment pages (width 12, 2sp)
    "   KKKKKKKKKK   ", # 13: Page rim (width 10, 3sp)
    "                ", # 14
    "                "  # 15
]

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
    out_dir = r"scrapped_tools\preview_lich_phylactery"
    artifact_dir = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405"
    os.makedirs(out_dir, exist_ok=True)
    
    variations = {
        "opt1_crowned_skull_reliquary": GRID_OPT1,
        "opt2_twilight_soul_urn": GRID_OPT2,
        "opt3_cursed_twilight_amulet": GRID_OPT3,
        "opt4_tome_of_the_lich": GRID_OPT4,
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
        
        shutil.copy2(p16, os.path.join(artifact_dir, f"{key}_16.png"))
        shutil.copy2(p256, os.path.join(artifact_dir, f"{key}_256.png"))
        print(f"Verified & generated: {key}")

if __name__ == "__main__":
    main()
