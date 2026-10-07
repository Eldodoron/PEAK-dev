import os
import shutil
from PIL import Image

PALETTE = {
    ' ': (0, 0, 0, 0),
    'K': (18, 15, 20, 255),       # Darkest silhouette outline (#120F14)
    
    # Netherite Steel Ramp (Lit by center spotlight)
    'S': (126, 122, 138, 255),    # High specular highlight (#7E7A8A)
    's': (99, 95, 108, 255),      # Light netherite steel (#635F6C)
    'N': (77, 73, 84, 255),       # Midtone netherite steel (#4D4954)
    'n': (57, 53, 62, 255),       # Dark netherite steel (#39353E)
    'B': (40, 36, 44, 255),       # Deep netherite shadow (#28242C)
    'b': (26, 23, 29, 255),       # Outermost dark shadow (#1A171D)
    
    # Heat-bounce / Magma Glow on Metal
    'H': (184, 114, 46, 255),     # Warm amber bounce reflection on metal (#B8722E)
    'h': (143, 85, 36, 255),      # Deep bronze heat reflection (#8F5524)
    
    # Blazing Core (The light source)
    'W': (255, 251, 224, 255),    # White-hot molten core (#FFFBE0)
    'Y': (250, 220, 102, 255),    # Incandescent yellow (#FADC66)
    'A': (230, 155, 30, 255),     # Molten amber gold (#E69B1E)
    'O': (215, 84, 8, 255),       # Fiery lava orange (#D75408)
    'R': (153, 28, 6, 255),       # Deep crimson magma (#991C06)
    'r': (94, 16, 5, 255),        # Dark magma crust (#5E1005)
}

# -------------------------------------------------------------
# OPTION 2A: Clean Radial Spotlight (Steel Tones)
# Center core is the light source; inner faces lit (N, s), outer faces dark (b, B).
# -------------------------------------------------------------
GRID_2A = [
    "  KK        KK  ", # 0: Horn tips
    " KbNK      KNbK ", # 1: Horns: outer 'b', inner lit 'N'
    " KbnNKKKKKKNnbK ", # 2: Horns meet rim: b -> n -> N
    "  KbNssssssNbK  ", # 3: Top shelf lit by upward light 's'
    "  KbnSRRROrnbK  ", # 4: Upper core bevel: specular 'S', crust 'r'
    "  KbnROAYOnnbK  ", # 5: Core opening
    "  KbnOYWWYOnbK  ", # 6: White-hot core (YWWY)
    "  KbnOAYYAOnbK  ", # 7: Radiant core
    "  KbnROAAOnnbK  ", # 8: Lower chamber
    "  KbnRROORnnbK  ", # 9: Magma floor
    "  KbBnnnnnnBbK  ", # 10: Waist: inner 'n', outer 'B', 'b'
    "   KbBNNNNBbK   ", # 11: Base shelf lit by downward light 'N'
    "   KbbBBBBbbK   ", # 12: Base lower facet in shadow 'B'
    "    KKbbbbKK    ", # 13: Bottom rim in deep shadow 'b'
    "      KKKK      ", # 14: Base tip
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 2B: Fiery Heat-Bounce Spotlight (Warm Ambient Glow)
# Core casts fiery amber glow (H, h) onto inner horn walls and base shelf!
# -------------------------------------------------------------
GRID_2B = [
    "  KK        KK  ", # 0: Horn tips
    " KbHK      KHbK ", # 1: Inner horn face catches amber bounce 'H', outer 'b'
    " KbnHKKKKKKHnbK ", # 2: Upper horns: b -> n -> H
    "  KbHssssssHbK  ", # 3: Top shelf lit by core
    "  KbHSRRROrHbK  ", # 4: Upper core bevel
    "  KbHROAYOnHbK  ", # 5: Inner side walls bathed in core heat 'H'
    "  KbHOYWWYOHbK  ", # 6: White-hot center
    "  KbHOAYYAOHbK  ", # 7: Radiant core
    "  KbHROAAOnHbK  ", # 8: Lower inner side walls 'H'
    "  KbHRROORnHbK  ", # 9: Magma floor
    "  KbBnnnnnnBbK  ", # 10: Waist
    "   KbBhhhhBbK   ", # 11: Base shelf catches downward amber bounce 'h'
    "   KbbBBBBbbK   ", # 12: Lower base in shadow
    "    KKbbbbKK    ", # 13: Bottom rim
    "      KKKK      ", # 14: Base tip
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 2C: High-Intensity Nuclear Spotlight (Strong Contrast)
# Ultra-bright specular glare (S) on the core frame, plunging into pitch gunmetal.
# -------------------------------------------------------------
GRID_2C = [
    "  KK        KK  ", # 0: Horn tips
    " KbnK      KnbK ", # 1: Horns dark gunmetal
    " KbbnKKKKKKnbbK ", # 2: Outer horns deep shadow 'b'
    "  KbnSSSSSSnbK  ", # 3: High specular rim 'S' lit by upward blast
    "  KbnSRRROrnbK  ", # 4: Upper bevel
    "  KbnROAYOnnbK  ", # 5: Core opening
    "  KbnOYWWYOnbK  ", # 6: White-hot nuclear heart
    "  KbnOAYYAOnbK  ", # 7: Radiant core
    "  KbnROAAOnnbK  ", # 8: Lower chamber
    "  KbnRROORnnbK  ", # 9: Magma floor
    "  KbbnnnnnnbbK  ", # 10: Waist in deep shadow
    "   KbbnNNnbbK   ", # 11: Base shelf
    "   KbbBBBBbbK   ", # 12: Base lower facet
    "    KKbbbbKK    ", # 13: Bottom rim
    "      KKKK      ", # 14: Base tip
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 2D: Smooth Beveled 3D Spotlight (Multi-Tiered Anvil)
# Soft 3D planar shading across horns and casing: lit inner facets, shadow outer facets.
# -------------------------------------------------------------
GRID_2D = [
    "  KK        KK  ", # 0: Horn tips
    " KBNK      KNBK ", # 1: Horns: outer 'B', inner 'N'
    " KBNNKKKKKKNNBK ", # 2: Horns meet rim: B -> N
    "  KBNssssssNBK  ", # 3: Top plate: outer 'B', mid 'N', lit 's'
    "  KBNsRRROrNBK  ", # 4: Upper bevel
    "  KBNROAYOnNBK  ", # 5: Core opening
    "  KBNOYWWYONBK  ", # 6: White-hot core
    "  KBNOAYYAONBK  ", # 7: Radiant core
    "  KBNROAAOnNBK  ", # 8: Lower chamber
    "  KBNRROORnNBK  ", # 9: Magma floor
    "  KBNnnnnnnNBK  ", # 10: Waist
    "   KBNNNNNNBK   ", # 11: Base upper shelf lit by downward light 'N'
    "   KBBnnnnBBK   ", # 12: Base lower bevel in shadow 'B'
    "    KKbbbbKK    ", # 13: Bottom rim
    "      KKKK      ", # 14: Base tip
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
    out_dir = r"scrapped_tools\preview_netheric_core"
    artifact_dir = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405"
    os.makedirs(out_dir, exist_ok=True)
    
    variations = {
        "opt2a_radial_spotlight": (GRID_2A, "Option 2A: Clean Radial Spotlight"),
        "opt2b_heat_bounce": (GRID_2B, "Option 2B: Fiery Heat-Bounce Spotlight"),
        "opt2c_high_contrast": (GRID_2C, "Option 2C: High-Intensity Nuclear Spotlight"),
        "opt2d_beveled_3d": (GRID_2D, "Option 2D: Smooth Beveled 3D Spotlight")
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
        
        # Copy to artifact dir for markdown embedding
        shutil.copy2(p256, os.path.join(artifact_dir, f"{key}_256.png"))
        shutil.copy2(p16, os.path.join(artifact_dir, f"{key}_16.png"))
        print(f"Verified & generated: {key}")

if __name__ == '__main__':
    verify_and_generate()
