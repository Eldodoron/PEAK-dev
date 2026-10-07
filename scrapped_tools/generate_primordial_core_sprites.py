import os
from PIL import Image

PALETTE_FIERY_STEEL = {
    ' ': (0, 0, 0, 0),
    'K': (24, 28, 34, 255),       # Outer dark silhouette border (#181C22)
    'C': (52, 60, 72, 255),       # Dark slate corner cutout / bevel (#343C48)
    's': (82, 94, 106, 255),      # Deep slate shadow (right chassis)
    'S': (116, 130, 142, 255),    # Midtone slate (right chassis)
    'm': (154, 168, 178, 255),    # Light steel midtone (left chassis)
    'M': (194, 204, 212, 255),    # Bright brushed steel highlight (left chassis)
    'H': (235, 242, 248, 255),    # Pure specular white glint
    'g': (40, 46, 56, 255),       # Left trench groove
    't': (68, 78, 90, 255),       # Right trench groove
    # Fiery Cross Core (from screenshot: #EE651C, #DC3838, #A52131)
    'W': (255, 238, 175, 255),    # Hot white-gold incandescence
    'Y': (255, 175, 45, 255),     # Glowing solar amber
    'O': (238, 101, 28, 255),     # Vibrant fiery orange (#EE651C)
    'R': (220, 56, 56, 255),      # Bold crimson red (#DC3838)
    'D': (165, 33, 49, 255),      # Deep crimson shadow (#A52131)
    'N': (96, 18, 30, 255),       # Dark core shadow base
}

PALETTE_ANCIENT_BRONZE = {
    ' ': (0, 0, 0, 0),
    'K': (26, 18, 14, 255),       # Dark ancient metal outline
    'C': (55, 32, 24, 255),       # Deep shadow corner
    's': (88, 52, 38, 255),       # Bronze shadow
    'S': (132, 85, 52, 255),      # Bronze mid-dark
    'm': (175, 130, 68, 255),     # Ancient brass midtone
    'M': (218, 182, 104, 255),    # Ancient brass bright
    'H': (255, 232, 154, 255),    # Ancient gold glint
    'g': (46, 28, 22, 255),
    't': (76, 48, 34, 255),
    'W': (255, 238, 175, 255),
    'Y': (255, 175, 45, 255),
    'O': (238, 101, 28, 255),
    'R': (220, 56, 56, 255),
    'D': (165, 33, 49, 255),
    'N': (96, 18, 30, 255),
}

PALETTE_VIOLET_STEEL = {
    ' ': (0, 0, 0, 0),
    'K': (24, 28, 34, 255),
    'C': (52, 60, 72, 255),
    's': (82, 94, 106, 255),
    'S': (116, 130, 142, 255),
    'm': (154, 168, 178, 255),
    'M': (194, 204, 212, 255),
    'H': (235, 242, 248, 255),
    'g': (40, 46, 56, 255),
    't': (68, 78, 90, 255),
    'W': (255, 230, 255, 255),    # Pure cosmic white-magenta flash
    'Y': (240, 130, 255, 255),    # Brilliant lavender-magenta
    'O': (213, 0, 249, 255),      # Electric primordial purple (#D500F9)
    'R': (170, 0, 215, 255),      # Deep royal amethyst
    'D': (115, 0, 155, 255),      # Dark void violet
    'N': (65, 0, 95, 255),        # Deepest shadow base
}

GRID_FAITHFUL = [
    "                ", # 0
    "    KKKKKKKK    ", # 1
    "  KKMMMMSSSSKK  ", # 2
    " KKMMMMMMSsSSSK ", # 3
    " KMMMggggtssSSK ", # 4
    " KMMgtOORDttSSK ", # 5
    " KMMgtOORDttSSK ", # 6
    " KMgOOOWRDDDtSK ", # 7
    " KMgOOORRDDDtSK ", # 8
    " KMMgtDDRDttSSK ", # 9
    " KMMgtDDRDttSSK ", # 10
    " KMMMggggtssSSK ", # 11
    " KKMMMMMMSsSSSK ", # 12
    "  KKMMMMSSSSKK  ", # 13
    "    KKKKKKKK    ", # 14
    "                "  # 15
]

GRID_OVERCHARGE = [
    "                ", # 0
    "    KKKKKKKK    ", # 1
    "  KKHMMMSSSSKK  ", # 2
    " KKCMMMMMSsSCKK ", # 3
    " KMMMggggtssSSK ", # 4
    " KMMgtYYRDttSSK ", # 5
    " KMMgtOORDttSSK ", # 6
    " KMgYYWWRDDDtSK ", # 7
    " KMgOOORRDDDtSK ", # 8
    " KMMgtDDRDttSSK ", # 9
    " KMMgtDDRDttSSK ", # 10
    " KMMMggggtssSSK ", # 11
    " KKCMMMMMSsSCKK ", # 12
    "  KKMMMMSSSSKK  ", # 13
    "    KKKKKKKK    ", # 14
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

def verify_and_generate():
    out_dir = r"scrapped_tools\preview_primordial_core"
    os.makedirs(out_dir, exist_ok=True)
    
    items = {
        "opt1_faithful_plate": (GRID_FAITHFUL, PALETTE_FIERY_STEEL),
        "opt2_overcharge_plate": (GRID_OVERCHARGE, PALETTE_FIERY_STEEL),
        "opt3_ancient_bronze": (GRID_FAITHFUL, PALETTE_ANCIENT_BRONZE),
        "opt4_violet_amethyst": (GRID_OVERCHARGE, PALETTE_VIOLET_STEEL)
    }
    
    for name, (grid, pal) in items.items():
        for y, r in enumerate(grid):
            left_mask = ''.join('#' if c != ' ' else '.' for c in r[:8])
            right_mask = ''.join('#' if c != ' ' else '.' for c in r[8:])
            assert left_mask == right_mask[::-1], f"{name} Row {y} asymmetry: {left_mask} vs {right_mask[::-1]}"
        
        img = render_sprite(grid, pal)
        img.save(os.path.join(out_dir, f"{name}_16.png"))
        upscaled = img.resize((256, 256), Image.Resampling.NEAREST)
        upscaled.save(os.path.join(out_dir, f"{name}_256.png"))
        print(f"Verified & generated: {name}")

if __name__ == '__main__':
    verify_and_generate()
