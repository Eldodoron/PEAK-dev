import os
import shutil
from PIL import Image

# -------------------------------------------------------------------------
# PALETTE DEFINITION: Netherite Monstrosity Authentic Colors
# Heavy Netherite Steel + Boiling Forge Lava + Netheroak / Brick Crust
# -------------------------------------------------------------------------
PALETTE = {
    ' ': (0, 0, 0, 0),
    # Outline & Void
    'k': (18, 12, 17, 255),       # Deepest silhouette outline (#120C11)
    'K': (24, 18, 22, 255),       # Dark netherite outline (#181216)
    
    # Heavy Netherite Steel Armor
    'S': (110, 105, 119, 255),    # Specular netherite steel highlight (#6E6977)
    's': (90, 87, 90, 255),       # Polished netherite mid-light (#5A575A)
    'N': (77, 73, 77, 255),       # Core netherite steel (#4D494D)
    'n': (60, 57, 71, 255),       # Dark netherite steel (#3C3947)
    'B': (49, 44, 54, 255),       # Deep steel shadow (#312C36)
    'b': (36, 30, 31, 255),       # Netherite basal shadow (#241E1F)
    
    # Boiling Lava Crucible Core
    'W': (255, 248, 180, 255),    # White-hot molten spark (#FFF8B4)
    'Y': (243, 218, 116, 255),    # Incandescent core yellow (#F3DA74)
    'A': (225, 166, 29, 255),     # Molten amber gold (#E1A61D)
    'O': (215, 95, 8, 255),       # Radiant lava orange (#D75F08)
    'R': (170, 35, 6, 255),       # Deep molten crimson (#AA2306)
    'r': (108, 16, 5, 255),       # Dark lava crust (#6C1005)
    'D': (65, 12, 4, 255),        # Deep magma trench shadow (#410C04)
    'M': (56, 24, 30, 255),       # Nether brick / crust maroon (#38181E)
}

# -------------------------------------------------------------
# OPTION 1: The Crucible Caldera Core (Forging Vat of Lava)
# Heavy netherite crucible with molten lava pool & overflow drip
# -------------------------------------------------------------
GRID_1_CRUCIBLE = [
    "                ", # 0
    "   KKKK  KKKK   ", # 1: Twin crucible rim walls (cols 3..6 and 9..12)
    "  KssNKKKKNssK  ", # 2: Netherite rim lips with lava trench center
    "  KsNNORROONsK  ", # 3: Lava pool surface (ORRO)
    "  KnNOAYYAONnK  ", # 4: Incandescent molten pool (AYYA)
    "  KnNOYWWYONnK  ", # 5: White-hot caldera center (YWWY)
    "  KBnOAYYAOnBK  ", # 6: Molten boiling lava
    "  KBnNORROOnBK  ", # 7: Lava pool bottom
    "  KbBNORROnBbK  ", # 8: Netherite crucible floor + lava drain
    "  KbBNOAONnBbK  ", # 9: Center lava overflow drip (OAO)
    "  KbBnOAnBnBbK  ", # 10: Magma drip narrowing (OA)
    "   KbbNOnbbBK   ", # 11: Molten drip apex (O)
    "   KbbbNbbbBK   ", # 12: Netherite basal support
    "    KKbMMbKK    ", # 13: Bottom brick foundation (MM)
    "      KKKK      ", # 14: Base apex
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 2: Horned Monstrosity Core (Anvil Horns + Magma Core)
# Heavy upward netherite anvil horns framing a blazing core
# -------------------------------------------------------------
GRID_2_HORNED = [
    "  KK        KK  ", # 0: Netherite horn tips (cols 2-3 and 12-13)
    " KsNK      KNsK ", # 1: Anvil horn upper stalks
    " KsNNKKKKKKNNsK ", # 2: Horns meet top rim
    "  KsNssssssNsK  ", # 3: Polished netherite upper plate
    "  KnNSRRROrnNK  ", # 4: Core rim with lava vent
    "  KnNROAYOnnNK  ", # 5: Core chamber
    "  KnNOYWWYOnNK  ", # 6: White-hot nuclear core (YWWY)
    "  KnNOAYYAOnNK  ", # 7: Radiant core
    "  KnNROAAOnnNK  ", # 8: Core lower chamber
    "  KbNRROORnBNK  ", # 9: Magma chamber floor
    "  KbBnnnnnnBbK  ", # 10: Heavy netherite waist
    "   KbBNNNNBbK   ", # 11: Lower base bevel
    "   KbBBBBBBbK   ", # 12: Basal plate
    "    KKbbbbKK    ", # 13: Bottom rim
    "      KKKK      ", # 14: Base tip
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 3: Industrial Forge Reactor (Vent Ports + Slag Core)
# Octagonal plate with Monstrosity shoulder vents & lava core
# -------------------------------------------------------------
GRID_3_REACTOR = [
    "                ", # 0
    "      KKKK      ", # 1: Top rim (cols 6..9, width 4)
    "    KKssNNKK    ", # 2: Bevel 1 (cols 4..11, width 8)
    "   KsNROORnNK   ", # 3: Top vent exhaust port (ROOR)
    "  KsNRWYYWRnNK  ", # 4: Upper vent flare (RWYYWR)
    " KsNnOAYYAOnNBK ", # 5: Outer netherite casing (cols 1..14)
    " KsNRORrrROrnBK ", # 6: Netherite grill bars over core
    " KNnOAYWWYAOnBK ", # 7: Pure molten heart behind grill
    " KNnOAYWWYAOnBK ", # 8: Pure molten heart
    " KsNRORrrROrnBK ", # 9: Netherite grill bars
    " KsNnOAYYAOnNBK ", # 10: Lower vent flare
    "  KbNROAAORnBK  ", # 11: Bottom vent exhaust
    "   KbBNNNNBbK   ", # 12: Lower bevel 2
    "    KKbbbbKK    ", # 13: Lower bevel 1
    "      KKKK      ", # 14: Bottom rim
    "                "  # 15
]

# -------------------------------------------------------------
# OPTION 4: Volcanic Netherite Singularity (Cracked Geo-Core)
# Faceted Netherite ingot diamond cracked with magma veins
# -------------------------------------------------------------
GRID_4_FISSURE = [
    "       KK       ", # 0: Top apex
    "      KsNK      ", # 1: Diamond top peak
    "     KssNNK     ", # 2: Netherite facet
    "    KssNNNnK    ", # 3: Outer steel plate
    "   KssNRROnnK   ", # 4: Magma vein crack starts (RRO)
    "  KssNROAYOnnK  ", # 5: Vein widens into molten core
    " KssNROAYYAOnnK ", # 6: Blazing magma chamber (AYYA)
    " KssNOAYWWYAOnK ", # 7: White-hot fissure center (YWWY)
    " KssNOAYWWYAOnK ", # 8: Center fissure axis
    " KssNROAYYAOnnK ", # 9: Lower fissure
    "  KbnNROAAOnnK  ", # 10: Vein taper
    "   KbnNRROnnK   ", # 11: Vein fissure narrowing
    "    KbnNNNnK    ", # 12: Netherite lower facet
    "     KbnnnK     ", # 13: Steel base
    "      KbbK      ", # 14: Bottom tip
    "       KK       "  # 15: Base apex
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
        "opt1_crucible_core": (GRID_1_CRUCIBLE, "Option 1: The Crucible Caldera Core"),
        "opt2_horned_core": (GRID_2_HORNED, "Option 2: Horned Monstrosity Core"),
        "opt3_reactor_plate": (GRID_3_REACTOR, "Option 3: Industrial Forge Reactor"),
        "opt4_volcanic_fissure": (GRID_4_FISSURE, "Option 4: Volcanic Netherite Fissure")
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
        
        # Copy to artifact dir for direct markdown in-chat embedding
        shutil.copy2(p256, os.path.join(artifact_dir, f"{key}_256.png"))
        shutil.copy2(p16, os.path.join(artifact_dir, f"{key}_16.png"))
        print(f"Verified & generated: {key}")

if __name__ == '__main__':
    verify_and_generate()
