import os
from PIL import Image

whimscape_book_path = "scrapped_tools/whimscape_samples/book.png"
output_item_dir = "minecraft/kubejs/assets/kubejs/textures/item"
preview_dir = "scrapped_tools/previews"

os.makedirs(output_item_dir, exist_ok=True)
os.makedirs(preview_dir, exist_ok=True)

base_img = Image.open(whimscape_book_path).convert("RGBA")

# Whimscape 10 original colors -> Target colors
COLOR_MAPS = {
    "melonbook": {
        "#36151b": "#04261d", # dark rind outline
        "#53202d": "#1d712d", # rind trim
        "#733429": "#2e7d25", # dark rind stripe
        "#8a4e34": "#388a28", # Whimscape melon base green
        "#ab633f": "#57a126", # Whimscape melon light green
        "#d17949": "#76b825", # Whimscape melon bright highlight
        "#923c2f": "#1d712d", # bottom rind fold
        "#ad5635": "#388a28", # corner green
        "#9e7e73": "#791b3e", # Whimscape melon pulp deep shadow
        "#d4ac7f": "#d43220", # Whimscape juicy red watermelon pulp pages!
    },
    "beebook": {
        "#36151b": "#261405",
        "#53202d": "#522b07",
        "#733429": "#7a4009",
        "#8a4e34": "#b86812", # amber leather
        "#ab633f": "#e08d19", # liquid honey
        "#d17949": "#f5aa22", # bright honey
        "#923c2f": "#6e3906",
        "#ad5635": "#a65d11",
        "#9e7e73": "#947847",
        "#d4ac7f": "#fae39d", # honey parchment
    },
    "hellbook": {
        "#36151b": "#1a0910", # obsidian outline
        "#53202d": "#380c13",
        "#733429": "#5c1017",
        "#8a4e34": "#85181b", # crimson nether leather
        "#ab633f": "#c2271d", # blaze fire
        "#d17949": "#f57c16", # bright flame ribbon
        "#923c2f": "#4d0b11",
        "#ad5635": "#781619",
        "#9e7e73": "#61433d",
        "#d4ac7f": "#b08a78", # ash parchment
    },
    "seabook": {
        "#36151b": "#103f44", # Whimscape prismarine dark outline
        "#53202d": "#165459",
        "#733429": "#1a5b61",
        "#8a4e34": "#297a78", # Whimscape prismarine base
        "#ab633f": "#36875f", # Whimscape sea-green
        "#d17949": "#34cc99", # Whimscape bright prismarine cyan
        "#923c2f": "#1b5252",
        "#ad5635": "#236968",
        "#9e7e73": "#3d6e6d",
        "#d4ac7f": "#b6ebd9", # pale seafoam pages
    },
    "deepbook": {
        "#36151b": "#1c1c22", # dark deepslate edge
        "#53202d": "#2e2e38",
        "#733429": "#383842",
        "#8a4e34": "#484952", # Whimscape deepslate tile gray
        "#ab633f": "#5d5e69", # deepslate highlight
        "#d17949": "#727380", # polished slate ribbon
        "#923c2f": "#282830",
        "#ad5635": "#3f4047",
        "#9e7e73": "#071a26", # dark sculk page shadow
        "#d4ac7f": "#0b3447", # Whimscape subterranean bluish sculk pages!
    },
    "sculkbook": {
        "#36151b": "#040a14", # abyssal sculk outline
        "#53202d": "#071524",
        "#733429": "#091f30",
        "#8a4e34": "#0b2538", # intense sculk navy
        "#ab633f": "#044257", # sculk tendril
        "#d17949": "#147f87", # catalyst cyan ribbon
        "#923c2f": "#061826",
        "#ad5635": "#092233",
        "#9e7e73": "#084d59",
        "#d4ac7f": "#00f0cc", # intense radiant glowing sculk soul pages!
    },
    "endbook": {
        "#36151b": "#160721", # void outline
        "#53202d": "#2b0d3d",
        "#733429": "#3b1154",
        "#8a4e34": "#4f1970", # void purple leather
        "#ab633f": "#732ba6", # chorus magenta
        "#d17949": "#9438d4", # bright ender ribbon
        "#923c2f": "#270a38",
        "#ad5635": "#431461",
        "#9e7e73": "#857859",
        "#d4ac7f": "#ebdcb2", # end stone ivory pages
    },
    "stonebook": {
        "#36151b": "#242429", # stone outline
        "#53202d": "#383840",
        "#733429": "#484852",
        "#8a4e34": "#5c5c66", # andesite cover
        "#ab633f": "#787885",
        "#d17949": "#9898a6", # polished chisel ribbon
        "#923c2f": "#303038",
        "#ad5635": "#4f4f59",
        "#9e7e73": "#6e6e78",
        "#d4ac7f": "#a6a6b0", # calcified shale pages
    }
}

def hex_to_rgba(h, alpha=255):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4)) + (alpha,)

for name, col_map in COLOR_MAPS.items():
    new_img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    for y in range(base_img.height):
        for x in range(base_img.width):
            r, g, b, a = base_img.getpixel((x, y))
            if a == 0:
                continue
            orig_hex = f"#{r:02x}{g:02x}{b:02x}"
            new_hex = col_map.get(orig_hex, orig_hex)
            new_img.putpixel((x, y), hex_to_rgba(new_hex, a))
    
    # Save 16x16 game texture
    item_path = os.path.join(output_item_dir, f"{name}.png")
    new_img.save(item_path)
    
    # Save versioned 256x256 nearest-neighbor preview (v2 busts webview cache)
    preview_img = new_img.resize((256, 256), Image.Resampling.NEAREST)
    preview_path_v2 = os.path.join(preview_dir, f"{name}_v2_256.png")
    preview_img.save(preview_path_v2)
    # Also overwrite the old one
    preview_path_old = os.path.join(preview_dir, f"{name}_256.png")
    preview_img.save(preview_path_old)
    print(f"Generated {name}: item -> {item_path}, preview -> {preview_path_v2}")

print("All books cleanly remapped from Whimscape book.png!")
