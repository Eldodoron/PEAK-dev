import os
from PIL import Image

PALETTE = {
    ' ': (0, 0, 0, 0),
    'K': (24, 12, 14, 255),       # Darkest silhouette outline (#180C0E)
    'B': (0, 0, 0, 255),          # Pure black void furnace window (#000000)
    'H': (255, 252, 230, 255),    # Pure white-gold glint (#FFFAEE)
    'W': (255, 245, 180, 255),    # Incandescent white-gold core glint
    'Y': (255, 234, 144, 255),    # Radiant pale gold highlight (#FFEA90)
    'G': (255, 215, 63, 255),     # Vibrant molten gold (#FFD73F)
    'A': (205, 126, 0, 255),      # Deep amber gold (#CD7E00)
    'O': (155, 62, 0, 255),       # Burnt orange/bronze (#9B3E00)
    'o': (94, 34, 0, 255),        # Deep molten shadow (#5E2200)
}

# The authentic Ignis furnace window (cols 5..10, 6 pixels wide)
# Row 5: Top black border
# Row 6: Brow bar (YGGA)
# Row 7: Center bridge (GA)
# Row 8: Twin tusks (Y left, G right)
# Row 9: Lower tusks (G left, A right)
# Row 10: Bottom black border

# -------------------------------------------------------------
# 1A: Clean 12x12 Square Relic (Uniform 2px Rim All Around)
# -------------------------------------------------------------
GRID_1A = [
    "                ", # 0
    "                ", # 1
    "   KKKKKKKKKK   ", # 2: Top outline (cols 3..12, width 10)
    "  KHYYYYYYYAOK  ", # 3: Top gold bar (cols 2..13, width 12)
    "  KGYAYYYYYAOK  ", # 4: Inner top gold rim
    "  KGYBBBBBBAOK  ", # 5: Window top border
    "  KGYBYGGABAOK  ", # 6: Skull brow bar (YGGA)
    "  KGYBBGABBAOK  ", # 7: Skull center bridge (GA)
    "  KGYBYBBGBAOK  ", # 8: Skull tusks (Y, G)
    "  KGYBGBBABAOK  ", # 9: Lower tusks (G, A)
    "  KGYBBBBBBAOK  ", # 10: Window bottom border
    "  KGAOOOOOOOOK  ", # 11: Inner bottom gold rim
    "  KOOOOOOOOOOK  ", # 12: Bottom gold bar
    "   KKKKKKKKKK   ", # 13: Bottom outline (cols 3..12, width 10)
    "                ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# 1B: Balanced 14x14 Octagonal Relic Plate
# -------------------------------------------------------------
GRID_1B = [
    "                ", # 0
    "      KKKK      ", # 1: Top rim (cols 6..9, width 4)
    "    KKHYYYKK    ", # 2: Bevel 1 (cols 4..11, width 8)
    "   KHYYYYYAOK   ", # 3: Bevel 2 (cols 3..12, width 10)
    "  KGYAYYYYYAOK  ", # 4: Bevel 3 (cols 2..13, width 12)
    " KGYABBBBBBAOoK ", # 5: Window top border (cols 1..14, width 14)
    " KGYABYGGABAOoK ", # 6: Skull brow bar
    " KGYABBGABBAOoK ", # 7: Skull center bridge (GA)
    " KGYABYBBGBAOoK ", # 8: Skull tusks
    " KGYABGBBABAOoK ", # 9: Lower tusks
    " KGYABBBBBBAOoK ", # 10: Window bottom border
    "  KGAOOOOOOOoK  ", # 11: Lower bevel 3 (cols 2..13, width 12)
    "   KOOOOOOOoK   ", # 12: Lower bevel 2 (cols 3..12, width 10)
    "    KKOOOOKK    ", # 13: Lower bevel 1 (cols 4..11, width 8)
    "      KKKK      ", # 14: Bottom rim (cols 6..9, width 4)
    "                "  # 15
]

# -------------------------------------------------------------
# 1C: Sculpted Flame-Wing Crest (Reference Spurred Wings)
# -------------------------------------------------------------
GRID_1C = [
    "                ", # 0
    "  KK        KK  ", # 1: Crest corner horns (cols 2-3, 12-13)
    " KYYKKKKKKKKAOK ", # 2: Crown peaks & rim (cols 1..14)
    "  KHYYYYYYYAOK  ", # 3: Upper chest rim (cols 2..13)
    " KGYAYYYYYAAOoK ", # 4: Upper flame wings flare out (cols 1..14)
    " KGYABBBBBBAOoK ", # 5: Upper flame wings
    "  KGYBYGGABAOK  ", # 6: Waist notch (indented to cols 2..13!)
    "  KGYBBGABBAOK  ", # 7: Waist center
    " KGYABYBBGBAOoK ", # 8: Lower flame spurs flare out (cols 1..14)
    " KGYABGBBABAOoK ", # 9: Lower flame spurs
    " KGYABBBBBBAOoK ", # 10: Window bottom
    "  KGAOOOOOOOoK  ", # 11: Lower rim tapers (cols 2..13)
    "   KOOOOOOOoK   ", # 12: Chin taper (cols 3..12)
    "    KKOOOOKK    ", # 13: Chin apex (cols 4..11)
    "       KK       ", # 14: Bottom chin point (cols 7..8)
    "                "  # 15
]

# -------------------------------------------------------------
# 1D: Straightened Authentic Crest (Stepped 45° Bevels)
# -------------------------------------------------------------
GRID_1D = [
    "                ", # 0
    "                ", # 1
    "    KKKKKKKK    ", # 2: Top rim outline (cols 4..11, width 8)
    "   KYYYYYYYYK   ", # 3: Bevel 1 (cols 3..12, width 10)
    "  KGYAYYYYYAOK  ", # 4: Bevel 2 (cols 2..13, width 12)
    " KGYABBBBBBAOoK ", # 5: Window top border (cols 1..14, width 14)
    " KGYABYGGABAOoK ", # 6: Skull brow bar
    " KGYABBGABBAOoK ", # 7: Skull center bridge
    " KGYABYBBGBAOoK ", # 8: Skull tusks
    " KGYABGBBABAOoK ", # 9: Lower tusks
    " KGYABBBBBBAOoK ", # 10: Window bottom border
    "  KGAOOOOOOOoK  ", # 11: Bevel 2 (cols 2..13, width 12)
    "   KOOOOOOOoK   ", # 12: Bevel 1 (cols 3..12, width 10)
    "    KKKKKKKK    ", # 13: Bottom rim outline (cols 4..11, width 8)
    "                ", # 14
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

def verify_and_generate():
    out_dir = r"scrapped_tools\preview_heart_of_inferno"
    os.makedirs(out_dir, exist_ok=True)
    
    variations = {
        "opt1a_square_relic": (GRID_1A, "Option 1A: Clean Square Relic (Uniform 2px Rim)"),
        "opt1b_octagonal_plate": (GRID_1B, "Option 1B: Balanced Octagonal Plate (14x14 Medallion)"),
        "opt1c_flame_wing_crest": (GRID_1C, "Option 1C: Sculpted Flame-Wing Crest (Reference Spurred Wings)"),
        "opt1d_straightened_crest": (GRID_1D, "Option 1D: Straightened Authentic Crest (Stepped 45° Bevels)")
    }
    
    for key, (grid, title) in variations.items():
        assert len(grid) == 16, f"{key} row count != 16"
        for y, r in enumerate(grid):
            assert len(r) == 16, f"{key} row {y} len {len(r)} != 16: '{r}'"
            l = ''.join('#' if c != ' ' else '.' for c in r[:8])
            r_mask = ''.join('#' if c != ' ' else '.' for c in r[8:])
            assert l == r_mask[::-1], f"{key} row {y} asymmetry: {l} vs {r_mask[::-1]}"
        
        img = render_sprite(grid, PALETTE)
        img.save(os.path.join(out_dir, f"{key}_16.png"))
        upscaled = img.resize((256, 256), Image.Resampling.NEAREST)
        upscaled.save(os.path.join(out_dir, f"{key}_256.png"))
        print(f"Verified & generated: {key}")

if __name__ == '__main__':
    verify_and_generate()
