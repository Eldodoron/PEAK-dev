import os
from PIL import Image

# -------------------------------------------------------------
# PALETTES
# -------------------------------------------------------------
# Derived directly from user's screenshot:
# Purple Frame & Concentric Gradient:
# Deep dark border: (28, 18, 52) #1C1234
# Outer purple frame: (80, 64, 176) #5040B0
# Indigo mid-dark: (96, 96, 208) #6060D0
# Periwinkle light: (144, 168, 248) #90A8F8
# Pale lavender field: (208, 214, 248) #D0D6F8
# Pure white resonant glyph: (255, 255, 255) #FFFFFF
# Soft white glint: (235, 240, 255) #EBF0FF

# Cyan Void Rift (from screenshot background):
# Vibrant cyan glow: (32, 248, 248) #20F8F8
# Deep turquoise energy: (16, 168, 208) #10A8D0
# Dark void cyan: (8, 90, 120) #085A78

PALETTE_VOID = {
    ' ': (0, 0, 0, 0),
    'K': (24, 16, 46, 255),       # Deep void border (#18102E)
    'P': (78, 62, 172, 255),      # Rich purple frame (#4E3EAC)
    'p': (62, 48, 142, 255),      # Shadow purple bevel (#3E308E)
    'I': (96, 96, 208, 255),      # Indigo step layer (#6060D0)
    'L': (144, 168, 248, 255),    # Periwinkle step layer (#90A8F8)
    'V': (208, 214, 250, 255),    # Pale lavender field (#D0D6FA)
    'W': (255, 255, 255, 255),    # Glowing white resonator core (#FFFFFF)
    'w': (235, 240, 255, 255),    # Specular white accent (#EBF0FF)
    # Cyan Void Energy Accents
    'C': (32, 248, 248, 255),     # Vibrant cyan void spark (#20F8F8)
    'c': (16, 168, 208, 255),     # Deep turquoise accent (#10A8D0)
    'd': (8, 90, 120, 255),       # Dark cyan corner trench (#085A78)
}

# -------------------------------------------------------------
# CANDIDATE 1: Faithful Resonant Plaque (Direct 1:1 Translation)
# -------------------------------------------------------------
GRID_1 = [
    "                ", # 0
    "    KKKKKKKK    ", # 1
    "  KKPPPPPPPPKK  ", # 2
    " KKPIWWVVWWIPKK ", # 3
    " KPPIWWVVWWIPPK ", # 4
    " KPILWWVVWWLIPK ", # 5
    " KPILLWWWWLLIPK ", # 6
    " KPILLWWWWLLIPK ", # 7
    " KPILLWWWWLLIPK ", # 8
    " KPILLWWWWLLIPK ", # 9
    " KPILWWVVWWLIPK ", # 10
    " KPPIWWVVWWIPPK ", # 11
    " KKPIWWVVWWIPKK ", # 12
    "  KKPPPPPPPPKK  ", # 13
    "    KKKKKKKK    ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# CANDIDATE 2: Void Rift Matrix (Corner Cyan Energy Sparks)
# Captures the cyan rift aura from the background into corner quantum nodes
# -------------------------------------------------------------
GRID_2 = [
    "                ", # 0
    "    KKKKKKKK    ", # 1
    "  KKCPPPPPPCKK  ", # 2 (C cyan corner spark)
    " KKcIWWVVWWicKK ", # 3 (c turquoise emitter)
    " KPPIWWVVWWIPPK ", # 4
    " KPILWWVVWWLIPK ", # 5
    " KPILLWWWWLLIPK ", # 6
    " KPILLWWWWLLIPK ", # 7
    " KPILLWWWWLLIPK ", # 8
    " KPILLWWWWLLIPK ", # 9
    " KPILWWVVWWLIPK ", # 10
    " KPPIWWVVWWIPPK ", # 11
    " KKcIWWVVWWicKK ", # 12 (c turquoise emitter)
    "  KKCPPPPPPCKK  ", # 13 (C cyan corner spark)
    "    KKKKKKKK    ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# CANDIDATE 3: Shaded Dimensional Relic (Top-Left Light Ramp)
# Asymmetrical lighting on the frame (brighter top-left, darker shadow bevel)
# while keeping the white resonator core brilliantly centered and symmetric.
# -------------------------------------------------------------
GRID_3 = [
    "                ", # 0
    "    KKKKKKKK    ", # 1
    "  KKLLPPPPppKK  ", # 2 (L light bevel on left, p shadow on right)
    " KKLIWWVVWWppKK ", # 3
    " KPLIWWVVWWipPK ", # 4
    " KPILWWVVWWLpPK ", # 5
    " KPILLWWWWLLipK ", # 6
    " KPILLWWWWLLipK ", # 7
    " KPILLWWWWLLipK ", # 8
    " KPILLWWWWLLipK ", # 9
    " KPILWWVVWWLpPK ", # 10
    " KPLIWWVVWWipPK ", # 11
    " KKLIWWVVWWppKK ", # 12
    "  KKLLPPPPppKK  ", # 13
    "    KKKKKKKK    ", # 14
    "                "  # 15
]

# -------------------------------------------------------------
# CANDIDATE 4: Resonant Frequency Core (Pulsing Diamond Waisted Tines)
# Pronounced hour-glass waist with pure white glints on the tine tips.
# -------------------------------------------------------------
GRID_4 = [
    "                ", # 0
    "    KKKKKKKK    ", # 1
    "  KKPPPPPPPPKK  ", # 2
    " KKPIwwVVwwIPKK ", # 3 (ww specular tine tips)
    " KPPIWWVVWWIPPK ", # 4
    " KPILWWVVWWLIPK ", # 5
    " KPILLVWWVLIPPK ", # 6 (tapered waist)
    " KPILVVWWVVLIPK ", # 7 (condensed core bridge)
    " KPILVVWWVVLIPK ", # 8
    " KPILLVWWVLIPPK ", # 9
    " KPILWWVVWWLIPK ", # 10
    " KPPIWWVVWWIPPK ", # 11
    " KKPIwwVVwwIPKK ", # 12 (ww specular tine tips)
    "  KKPPPPPPPPKK  ", # 13
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
    out_dir = r"scrapped_tools\preview_void_resonator"
    os.makedirs(out_dir, exist_ok=True)
    
    items = {
        "opt1_faithful_plaque": GRID_1,
        "opt2_cyan_rift_matrix": GRID_2,
        "opt3_directional_relic": GRID_3,
        "opt4_tine_frequency": GRID_4,
    }
    
    for name, grid in items.items():
        for y, r in enumerate(grid):
            left_mask = ''.join('#' if c != ' ' else '.' for c in r[:8])
            right_mask = ''.join('#' if c != ' ' else '.' for c in r[8:])
            assert left_mask == right_mask[::-1], f"{name} Row {y} asymmetry: {left_mask} vs {right_mask[::-1]}"
        
        img = render_sprite(grid, PALETTE_VOID)
        img.save(os.path.join(out_dir, f"{name}_16.png"))
        upscaled = img.resize((256, 256), Image.Resampling.NEAREST)
        upscaled.save(os.path.join(out_dir, f"{name}_256.png"))
        print(f"Verified & generated: {name}")

if __name__ == '__main__':
    verify_and_generate()
