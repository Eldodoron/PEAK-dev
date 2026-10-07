import os
import shutil
from PIL import Image

PALETTE = {
    ' ': (0, 0, 0, 0),
    'K': (21, 14, 27, 255),       # Darkest abyssal carapace outline (#150E1B)
    'k': (12, 8, 16, 255),        # Deep void trench slit (#0C0810)
    'B': (33, 22, 43, 255),       # Deep carapace body (#21162B)
    'b': (50, 33, 65, 255),       # Carapace midtone (#322141)
    'S': (122, 125, 161, 255),    # Sunken slate/chitin highlight (#7A7DA1)
    's': (173, 175, 203, 255),    # Pale sunken slate glint (#ADAFCB)
    'T': (48, 68, 76, 255),       # Deep trench cyan shadow (#30444C)
    'C': (72, 100, 112, 255),     # Abyssal ocean cyan (#486470)
    'c': (110, 152, 169, 255),    # Bioluminescent cyan glow (#6E98A9)
    'W': (229, 230, 242, 255),    # Core glint / white-lavender spark (#E5E6F2)
    'Y': (179, 130, 255, 255),    # Luminous radiant violet (#B382FF)
    'P': (138, 62, 255, 255),     # Vibrant abyssal purple (#8A3EFF)
    'V': (101, 0, 255, 255),      # Electric deep violet (#6500FF)
    'D': (70, 19, 147, 255),      # Dark violet shadow (#461393)
    'd': (52, 14, 111, 255),      # Deep abyssal shadow (#340E6F)
}

# -------------------------------------------------------------
# OPTION 1: Abyssal Trench Orb (Faithful to Cataclysm Abyss Orb)
# Spherical 12x12 abyssal eye orb with specular glint & dark slit
# -------------------------------------------------------------
GRID_1_ORB = [
    "                ", # 0
    "                ", # 1
    "    KKKKKKKK    ", # 2: Top rim (cols 4..11, width 8)
    "   KWYPPVVDdK   ", # 3: Bevel 1 (cols 3..12, width 10)
    "  KWYPPPVVDDdK  ", # 4: Upper orb (cols 2..13, width 12)
    "  KYPPPVVVVDdK  ", # 5: Eye top
    " KYPPPVkKVVVDdK ", # 6: Slit pupil top (cols 1..14, width 14)
    " KYPPVkckKVVDdK ", # 7: Slit pupil center with cyan spark
    " KYPPVkckKVVDdK ", # 8: Slit pupil center
    " KYPPPVkKVVVDdK ", # 9: Slit pupil bottom
    "  KYPPPVVVVDdK  ", # 10: Eye bottom
    "  KdPVVVVDDDdK  ", # 11: Lower orb (cols 2..13, width 12)
    "   KdVDDDDDDk   ", # 12: Bevel 1 (cols 3..12, width 10)
    "    KKKKKKKK    ", # 13: Bottom rim (cols 4..11, width 8)
    "                ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 2: Abyssal Singularity Relic (Carapace Plate + Void Rift)
# 14x14 Octagonal Carapace Frame with Swirling Black Hole Core
# -------------------------------------------------------------
GRID_2_SINGULARITY = [
    "                ", # 0
    "      KKKK      ", # 1: Top rim (cols 6..9, width 4)
    "    KKsSSsKK    ", # 2: Bevel 1 (cols 4..11, width 8)
    "   KsBbddBbSK   ", # 3: Top plate (cols 3..12, width 10)
    "  KsBVDWWdVbSK  ", # 4: Outer singularity swirl (cols 2..13, width 12)
    " KSBVPYkkYPVbSK ", # 5: Black hole event horizon (cols 1..14, width 14)
    " KSdPYkkkkYPdSK ", # 6: Pure void black hole center (4k's)
    " KSdPYkkkkYPdSK ", # 7: Void center
    " KSdPYkkkkYPdSK ", # 8: Void center
    " KSBVPYkkYPVbSK ", # 9: Lower event horizon
    "  KbBVDWWdVbSK  ", # 10: Lower swirl
    "   KbBbddBbSK   ", # 11: Bottom plate
    "    KKbSSbKK    ", # 12: Bevel 1
    "      KKKK      ", # 13: Bottom rim
    "                ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 3: Chitinous Leviathan Crest (Mandible Brackets + Pearl Core)
# Jagged carapace claws cradling an incandescent abyssal crystal
# -------------------------------------------------------------
GRID_3_CREST = [
    "                ", # 0
    "  KK        KK  ", # 1: Twin carapace horn tips (cols 2-3, 12-13)
    " KsBK      KBbK ", # 2: Horn stalks (cols 1..14)
    " KsBbKKKKKKbBbK ", # 3: Horns meet rim (cols 1..14)
    "  KBbWYPPYWbBK  ", # 4: Crystal peak between horns (cols 2..13)
    " KBbWYPPPPYWbBK ", # 5: Crystal upper body (cols 1..14)
    " KBbYPPkkPPYBbK ", # 6: Central abyssal eye slit
    " KBbVPkckkPVBbK ", # 7: Eye core with cyan spark
    " KBbVPkckkPVBbK ", # 8: Eye core
    " KBbYPPkkPPYBbK ", # 9: Eye slit bottom
    "  KBbVPDDDVBbK  ", # 10: Crystal lower taper (cols 2..13)
    "  KBbVDDDDVbBK  ", # 11: Crystal base (cols 2..13)
    "   KBbDDDDbBK   ", # 12: Mandible bracket base (cols 3..12)
    "    KKBBBBKK    ", # 13: Bottom chin rim (cols 4..11)
    "       KK       ", # 14: Base apex (cols 7..8)
    "                "  # 15
]

def make_row(width, fill):
    spaces = (16 - width) // 2
    if width == 0:
        return ' ' * 16
    if len(fill) == width:
        return ' ' * spaces + fill + ' ' * spaces
    assert len(fill) == width - 2, f'width {width} expects {width-2} chars, got {len(fill)}: "{fill}"'
    return ' ' * spaces + 'K' + fill + 'K' + ' ' * spaces

# -------------------------------------------------------------
# OPTION 4: Trench Pearl Catalyst (Deep Ocean Faceted Gem)
# Diamond/Tear faceted gem with bioluminescent cyan & abyssal violet
# -------------------------------------------------------------
GRID_4_PEARL = [
    make_row(2, "KK"),
    make_row(4, "Wc"),
    make_row(6, "WYcC"),
    make_row(8, "WYPcCC"),
    make_row(10, "WYPPcCCC"),
    make_row(12, "WYPPVkcCCD"),
    make_row(14, "WYPPVkkkcCCD"),
    make_row(14, "WYPVVkkkcCDD"),
    make_row(14, "WYPVVkkkcCDD"),
    make_row(14, "WYPPVkkkcCCD"),
    make_row(12, "YPPPVkcDDCCD")[:10], # wait
    make_row(10, "YPPDDDDD"),
    make_row(8, "VPDDDD"),
    make_row(6, "VDDD"),
    make_row(4, "VD"),
    make_row(2, "KK")
]
GRID_4_PEARL[10] = make_row(12, "YPPVkcDDCD")

def render_sprite(grid, palette):
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    for y in range(16):
        row = grid[y]
        for x in range(16):
            ch = row[x]
            img.putpixel((x, y), palette.get(ch, (0, 0, 0, 0)))
    return img

def verify_and_generate():
    out_dir = r"scrapped_tools\preview_abyssal_catalyst"
    artifact_dir = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405"
    os.makedirs(out_dir, exist_ok=True)
    
    variations = {
        "opt1_trench_orb": (GRID_1_ORB, "Option 1: Abyssal Trench Orb"),
        "opt2_singularity_relic": (GRID_2_SINGULARITY, "Option 2: Abyssal Singularity Relic"),
        "opt3_chitinous_crest": (GRID_3_CREST, "Option 3: Chitinous Leviathan Crest"),
        "opt4_trench_pearl": (GRID_4_PEARL, "Option 4: Trench Pearl Catalyst")
    }
    
    for key, (grid, title) in variations.items():
        assert len(grid) == 16, f"{key} row count != 16"
        for y, r in enumerate(grid):
            assert len(r) == 16, f"{key} row {y} len {len(r)} != 16: '{r}'"
            l = ''.join('#' if c != ' ' else '.' for c in r[:8])
            r_mask = ''.join('#' if c != ' ' else '.' for c in r[8:])
            assert l == r_mask[::-1], f"{key} row {y} asymmetry: {l} vs {r_mask[::-1]}"
        
        img = render_sprite(grid, PALETTE)
        p16 = os.path.join(out_dir, f"{key}_16.png")
        p256 = os.path.join(out_dir, f"{key}_256.png")
        img.save(p16)
        upscaled = img.resize((256, 256), Image.Resampling.NEAREST)
        upscaled.save(p256)
        
        # Copy to artifact directory so markdown embeds can display it directly
        shutil.copy2(p256, os.path.join(artifact_dir, f"{key}_256.png"))
        shutil.copy2(p16, os.path.join(artifact_dir, f"{key}_16.png"))
        print(f"Verified & generated: {key}")

if __name__ == '__main__':
    verify_and_generate()
