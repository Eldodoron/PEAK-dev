import os
import shutil
from PIL import Image

PALETTE = {
    ' ': (0, 0, 0, 0),
    'K': (18, 15, 20, 255),       # Darkest silhouette outline (#120F14)
    'S': (126, 122, 138, 255),    # High specular highlight (#7E7A8A)
    's': (99, 95, 108, 255),      # Light netherite steel (#635F6C)
    'N': (77, 73, 84, 255),       # Midtone netherite steel (#4D4954)
    'n': (57, 53, 62, 255),       # Dark netherite steel (#39353E)
    'B': (40, 36, 44, 255),       # Deep netherite shadow (#28242C)
    'b': (26, 23, 29, 255),       # Outermost dark shadow (#1A171D)
    
    # Molten Core Tones
    'W': (255, 251, 224, 255),    # White-hot molten core (#FFFBE0)
    'Y': (250, 220, 102, 255),    # Incandescent yellow (#FADC66)
    'A': (230, 155, 30, 255),     # Molten amber gold (#E69B1E)
    'O': (215, 84, 8, 255),       # Fiery lava orange (#D75408)
    'R': (153, 28, 6, 255),       # Deep crimson magma (#991C06)
    'r': (94, 16, 5, 255),        # Dark magma crust (#5E1005)
}

def make_full_grid(core_rows):
    return [
        "  KK        KK  ", # 0: Horn tips
        " KbnK      KnbK ", # 1: Horns dark gunmetal
        " KbbnKKKKKKnbbK ", # 2: Outer horns deep shadow
        "  KbnSSSSSSnbK  ", # 3: Specular rim lit by core blast
        f"  Kbn{core_rows[0]}nbK  ", # 4: Core row 0
        f"  Kbn{core_rows[1]}nbK  ", # 5: Core row 1
        f"  Kbn{core_rows[2]}nbK  ", # 6: Core row 2
        f"  Kbn{core_rows[3]}nbK  ", # 7: Core row 3
        f"  Kbn{core_rows[4]}nbK  ", # 8: Core row 4
        f"  Kbn{core_rows[5]}nbK  ", # 9: Core row 5
        "  KbbnnnnnnbbK  ", # 10: Waist in deep shadow
        "   KbbnNNnbbK   ", # 11: Base shelf
        "   KbbBBBBbbK   ", # 12: Base lower facet
        "    KKbbbbKK    ", # 13: Bottom rim
        "      KKKK      ", # 14: Base tip
        "                "  # 15
    ]

VARIANTS = {
    "opt2c_v1_magma_orb": {
        "title": "Option 2C-1: Symmetrical Rounded Magma Orb",
        "description": "Smooth chamfered octagonal core. 2x2 white-hot center surrounded by concentric yellow, amber, and fiery orange. Corners are cleanly recessed with dark steel.",
        "core": [
            "nROORn",
            "OAYYAO",
            "AYWWYA",
            "AYWWYA",
            "OAYYAO",
            "nROORn"
        ]
    },
    "opt2c_v2_caldera_gradient": {
        "title": "Option 2C-2: Geothermal Caldera Gradient",
        "description": "Natural downward magma pool gradient. Warm fiery upper flare, white-hot center heart, graduating smoothly into cooling crimson magma at the base.",
        "core": [
            "nOAAOn",
            "OAYYAO",
            "AYWWYA",
            "OAYYAO",
            "ROAAOR",
            "nROORn"
        ]
    },
    "opt2c_v3_faceted_diamond": {
        "title": "Option 2C-3: Faceted Volcanic Diamond",
        "description": "Geometric crystalline rhombus core. Width expands cleanly from 2 to 4 to 6 pixels at the center and contracts back symmetrically, zero irregular pixels.",
        "core": [
            "nnOOnn",
            "nOYYOn",
            "OAWWAO",
            "OAWWAO",
            "nOYYOn",
            "nnRRnn"
        ]
    },
    "opt2c_v4_flush_furnace": {
        "title": "Option 2C-4: Flush Magma Chamber",
        "description": "Full 6-pixel wide lava vat. Fills the casing flush on left and right with crust bevels on top and bottom, completely eliminating stepped outer pixels.",
        "core": [
            "rROORr",
            "ROAAOR",
            "OAYYAO",
            "OYWWYO",
            "ROAAOR",
            "rROORr"
        ]
    },
    "opt2c_v5_vertical_slot": {
        "title": "Option 2C-5: Framed Furnace Aperture",
        "description": "Recessed 4x6 vertical hearth flanked by straight dark-steel bevel columns. Completely straight vertical side walls with zero jagged pixel steps.",
        "core": [
            "nROORn",
            "nOAAOn",
            "nAYYAn",
            "nYWWTn".replace("T", "Y").replace("W", "W"),
            "nOAAOn",
            "nROORn"
        ]
    }
}

# Fix row 7 for v5
VARIANTS["opt2c_v5_vertical_slot"]["core"][3] = "nYWWYn"

def render_sprite(grid, palette):
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    for y in range(16):
        row = grid[y]
        for x in range(16):
            ch = row[x]
            img.putpixel((x, y), palette.get(ch, (0, 0, 0, 0)))
    return img

def main():
    out_dir = r"scrapped_tools\preview_netheric_core"
    artifact_dir = r"C:\Users\chris\.gemini\antigravity\brain\6d94d33a-8771-44bb-b233-6e02f1167405"
    os.makedirs(out_dir, exist_ok=True)
    
    for key, data in VARIANTS.items():
        grid = make_full_grid(data["core"])
        
        # Verify 100% bilateral symmetry across all 16 rows
        for y, row in enumerate(grid):
            assert len(row) == 16, f"{key} row {y} len != 16: '{row}'"
            for x in range(8):
                left_c = row[x]
                right_c = row[15 - x]
                assert left_c == right_c, f"{key} symmetry mismatch at y={y}, x={x} ('{left_c}') vs x={15-x} ('{right_c}'): '{row}'"
        
        # Render 16x16
        img16 = render_sprite(grid, PALETTE)
        p16 = os.path.join(out_dir, f"{key}_16.png")
        p256 = os.path.join(out_dir, f"{key}_256.png")
        img16.save(p16)
        
        # Render 256x256 nearest-neighbor upscale
        upscaled = img16.resize((256, 256), Image.Resampling.NEAREST)
        upscaled.save(p256)
        
        # Also create a cropped core preview (6x6 region scaled to 256x256) for direct zoom comparison
        core_crop = img16.crop((4, 3, 12, 11)) # 8x8 region covering the furnace window
        crop256 = core_crop.resize((256, 256), Image.Resampling.NEAREST)
        p_crop256 = os.path.join(out_dir, f"{key}_crop256.png")
        crop256.save(p_crop256)
        
        # Copy to artifact dir for in-chat embedding
        shutil.copy2(p16, os.path.join(artifact_dir, f"{key}_16.png"))
        shutil.copy2(p256, os.path.join(artifact_dir, f"{key}_256.png"))
        shutil.copy2(p_crop256, os.path.join(artifact_dir, f"{key}_crop256.png"))
        print(f"Generated and verified: {key}")

if __name__ == "__main__":
    main()
