import os
from PIL import Image

PALETTE_IGNIS = {
    ' ': (0, 0, 0, 0),
    'K': (24, 11, 13, 255),       # Darkest volcanic silhouette outline (#180B0D)
    'B': (0, 0, 0, 255),          # Pure black furnace void window (#000000)
    'b': (20, 10, 12, 255),       # Deep recess shadow (#140A0C)
    'v': (48, 21, 26, 255),       # Deepest obsidian maroon (#30151A)
    's': (62, 30, 36, 255),       # Dark volcanic shadow (#3E1E24)
    'm': (81, 41, 48, 255),       # Igneous midtone (#512930)
    'M': (115, 59, 69, 255),      # Warm maroon highlight (#733B45)
    'W': (255, 245, 190, 255),    # White-gold incandescence
    'H': (255, 234, 144, 255),    # Radiant pale gold highlight (#FFEA90)
    'G': (255, 215, 63, 255),     # Vibrant molten gold (#FFD73F)
    'A': (205, 126, 0, 255),      # Deep amber gold (#CD7E00)
    'O': (155, 62, 0, 255),       # Burnt orange / bronze (#9B3E00)
    'o': (94, 34, 0, 255),        # Deep molten shadow (#5E2200)
}

# CANDIDATE 1: Faithful Core of Ignis (Exact 1:1 Translation)
GRID_FAITHFUL = [
    "                ", # 0
    "    KKKKKKKK    ", # 1 (x=4..11)
    "  KKMMmmmmssKK  ", # 2 (x=2..13)
    " KGMHHHHAAAAOGK ", # 3 (x=1..14)
    " KGMAHHHHAAaOGK ", # 4 (x=1..14)
    " KOMAABBBBBAOGK ", # 5 (x=1..14)
    " KOAABHGAAABAOK ", # 6 (x=1..14)
    " KOAABGbbAOBAOK ", # 7 (x=1..14)
    " KOAABGbbAOBAOK ", # 8 (x=1..14)
    " KOAABGbbAOBAOK ", # 9 (x=1..14)
    " KOMAABBBBBAOGK ", # 10 (x=1..14)
    " KGMAAAAAAAOOGK ", # 11 (x=1..14)
    " KMMMMmmmmssssK ", # 12 (x=1..14)
    "  KKMMmmmmssKK  ", # 13 (x=2..13)
    "    KKKKKKKK    ", # 14 (x=4..11)
    "                "  # 15
]

# CANDIDATE 2: Heart of the Colossus (Volcanic Heart Silhouette enclosing Core)
GRID_HEART_CORE = [
    "                ", # 0
    "   KK      KK   ", # 1 (x=3,4 and x=11,12)
    "  KMMK    KssK  ", # 2 (x=2..5 and x=10..13)
    " KMMMMK  KssssK ", # 3 (x=1..6 and x=9..14)
    " KGMHHHHAAAAOGK ", # 4 (x=1..14)
    " KGMAHHHHAAaOGK ", # 5 (x=1..14)
    " KOMAABBBBBAOGK ", # 6 (x=1..14)
    " KOAABHGAAABAOK ", # 7 (x=1..14)
    "  KOABGbbAOBOK  ", # 8 (x=2..13)
    "   KABGbbAOAK   ", # 9 (x=3..12)
    "    KMAAAAOK    ", # 10 (x=4..11)
    "     KMAAOK     ", # 11 (x=5..10)
    "      KMOK      ", # 12 (x=6..9)
    "       KK       ", # 13 (x=7,8)
    "                ", # 14
    "                "  # 15
]

# CANDIDATE 3: Overheated Ignis Furnace (Luminous Molten Spark)
GRID_OVERHEATED = [
    "                ", # 0
    "    KKKKKKKK    ", # 1
    "  KKHMmmmmssKK  ", # 2
    " KGMHHHHAAAAOGK ", # 3
    " KGMAGHHHAHaOGK ", # 4
    " KOMAABBBBBAOGK ", # 5
    " KOAABWGHAAaAOK ", # 6 (W incandescent core)
    " KOAABWbbAOBAOK ", # 7 (W incandescent core)
    " KOAABGbbAOBAOK ", # 8
    " KOAABGbbAOBAOK ", # 9
    " KOMAABBBBBAOGK ", # 10
    " KGMAAAAAAAOOGK ", # 11
    " KMMMMmmmmssssK ", # 12
    "  KKMMmmmmssKK  ", # 13
    "    KKKKKKKK    ", # 14
    "                "  # 15
]

# CANDIDATE 4: Crowned Ignis Relic (Horned Crown Spurs)
GRID_CROWNED = [
    "  KK        KK  ", # 0: Golden horn tips
    " KGGK      KAOK ", # 1: Horns
    " KGMKKKKKKAAOGK ", # 2: Horns meeting top rim
    " KGMHHHHAAAAOGK ", # 3
    " KGMAHHHHAAaOGK ", # 4
    " KOMAABBBBBAOGK ", # 5
    " KOAABHGAAABAOK ", # 6
    " KOAABGbbAOBAOK ", # 7
    " KOAABGbbAOBAOK ", # 8
    " KOAABGbbAOBAOK ", # 9
    " KOMAABBBBBAOGK ", # 10
    " KGMAAAAAAAOOGK ", # 11
    " KMMMMmmmmssssK ", # 12
    "  KKMMmmmmssKK  ", # 13
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
    out_dir = r"scrapped_tools\preview_heart_of_inferno"
    os.makedirs(out_dir, exist_ok=True)
    
    items = {
        "opt1_faithful_ignis_core": GRID_FAITHFUL,
        "opt2_colossus_heart": GRID_HEART_CORE,
        "opt3_overheated_furnace": GRID_OVERHEATED,
        "opt4_crowned_relic": GRID_CROWNED,
    }
    
    for name, grid in items.items():
        for y, r in enumerate(grid):
            assert len(r) == 16, f"{name} Row {y} len is {len(r)}"
            left_mask = ''.join('#' if c != ' ' else '.' for c in r[:8])
            right_mask = ''.join('#' if c != ' ' else '.' for c in r[8:])
            assert left_mask == right_mask[::-1], f"{name} Row {y} asymmetry: {left_mask} vs {right_mask[::-1]}"
        
        img = render_sprite(grid, PALETTE_IGNIS)
        img.save(os.path.join(out_dir, f"{name}_16.png"))
        upscaled = img.resize((256, 256), Image.Resampling.NEAREST)
        upscaled.save(os.path.join(out_dir, f"{name}_256.png"))
        print(f"Verified & generated: {name}")

if __name__ == '__main__':
    verify_and_generate()
