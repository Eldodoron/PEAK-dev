#!/usr/bin/env python3
"""
FancyMenu v3 Helper Utility (fancymenu_helper.py)
Provides CLI utilities for authoring, validating, and packaging FancyMenu v3 assets & layouts:
  1. validate-layout <layout.txt>
  2. pack-fma <frames_dir> <output.fma> [--fps 30] [--loop true]
  3. create-panorama <name> <output_dir> [--speed 1.0] [--angle 25.0]
  4. check-nineslice <width> <height> <border_x> <border_y>
"""

import argparse
import os
import re
import sys
import zipfile
from pathlib import Path

VALID_ANCHOR_POINTS = {
    "top-left", "top-centered", "top-right",
    "mid-left", "mid-centered", "mid-right",
    "bottom-left", "bottom-centered", "bottom-right",
    "element", "vanilla"
}

VALID_ELEMENT_TYPES = {
    "vanilla_button", "custom_button", "input_field", "slider_v2", "checkbox",
    "text_v2", "tooltip", "ticker", "player_entity_v2",
    "fancymenu_customization_player_entity", "image", "glsl_shader",
    "json_model", "splash_text", "slideshow", "shape", "circle_shape",
    "cursor", "progress_bar", "audio_v2", "music_controller", "dragger",
    "browser", "item", "animation_controller", "video_mcef", "video_rinku",
    "drippy_vanilla_bar"
}

VALID_BACKGROUND_TYPES = {
    "color", "color_fancymenu", "panorama", "image", "slideshow",
    "video_mcef", "video_rinku", "browser", "glsl"
}


def validate_layout(layout_path: Path) -> int:
    if not layout_path.is_file():
        print(f"[ERROR] File not found: {layout_path}")
        return 1

    text = layout_path.read_text(encoding="utf-8")
    lines = text.replace("\r", "\n").split("\n")

    errors = []
    warnings = []
    set_type = None
    inside_container = False
    current_type = None
    current_props = {}
    containers = []

    for idx, raw_line in enumerate(lines, start=1):
        compact = re.sub(r"[\s]+", "", raw_line)
        if not compact:
            continue

        if compact.startswith("type=") and not inside_container:
            set_type = compact.split("=", 1)[1]
            continue

        if compact.endswith("{"):
            if inside_container:
                errors.append(f"Line {idx}: Unclosed container '{current_type}' before new '{{'")
                containers.append((current_type, current_props))
            inside_container = True
            current_type = compact[:-1]
            current_props = {}
            continue

        if compact.startswith("}") and inside_container:
            containers.append((current_type, current_props))
            inside_container = False
            current_type = None
            current_props = {}
            continue

        if inside_container and "=" in compact:
            raw_key = raw_line.split("=", 1)[0].strip()
            if " " in raw_key or "\t" in raw_key:
                warnings.append(f"Line {idx}: Property key '{raw_key}' contains whitespace (PropertiesParser strips all whitespace from keys)")
            key = compact.split("=", 1)[0]
            val = raw_line.split("=", 1)[1]
            if val.startswith(" "):
                val = val[1:]
            current_props[key] = val

    if inside_container:
        errors.append(f"EOF: Unclosed container '{current_type}' (missing '}}')")

    if set_type not in ("fancymenu_layout", "menu"):
        errors.append(f"Header: Expected 'type = fancymenu_layout', found '{set_type}'")

    seen_ids = set()
    for c_type, props in containers:
        if c_type in ("element", "vanilla_button"):
            el_type = props.get("element_type")
            if el_type not in VALID_ELEMENT_TYPES:
                errors.append(f"Container '{c_type}': Unknown element_type '{el_type}'")

            inst_id = props.get("instance_identifier")
            if not inst_id or inst_id == "null":
                errors.append(f"Container '{c_type}' ({el_type}): Missing or 'null' instance_identifier")
            elif inst_id in seen_ids:
                warnings.append(f"Container '{c_type}': Duplicate instance_identifier '{inst_id}'")
            else:
                seen_ids.add(inst_id)

            anchor = props.get("anchor_point") or props.get("orientation")
            if anchor and anchor not in VALID_ANCHOR_POINTS:
                errors.append(f"Element '{inst_id}': Invalid anchor_point '{anchor}'")
            if anchor == "element" and not (props.get("anchor_point_element") or props.get("orientation_element")):
                errors.append(f"Element '{inst_id}': anchor_point is 'element' but 'anchor_point_element' is missing")

        elif c_type == "menu_background":
            bg_type = props.get("background_type")
            if bg_type not in VALID_BACKGROUND_TYPES:
                errors.append(f"menu_background: Unknown background_type '{bg_type}'")

    print(f"=== FancyMenu Layout Validation: {layout_path.name} ===")
    print(f"Set Type   : {set_type}")
    print(f"Containers : {len(containers)}")
    for w in warnings:
        print(f"  [WARN]  {w}")
    for e in errors:
        print(f"  [ERROR] {e}")

    if not errors:
        print("Result: VALID (0 errors)")
        return 0
    print(f"Result: INVALID ({len(errors)} errors)")
    return 1


def pack_fma(frames_dir: Path, output_fma: Path, fps: int, loop: bool) -> int:
    if not frames_dir.is_dir():
        print(f"[ERROR] Frames directory not found: {frames_dir}")
        return 1

    png_files = sorted(frames_dir.glob("*.png"))
    if not png_files:
        print(f"[ERROR] No .png frames found in {frames_dir}")
        return 1

    props_content = (
        "type = animation\n\n"
        "animation-meta {\n"
        f"  fps = {fps}\n"
        f"  loop = {str(loop).lower()}\n"
        "  replay_intro = false\n"
        "}\n"
    )

    output_fma.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_fma, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("properties.txt", props_content)
        for frame in png_files:
            zf.write(frame, arcname=f"frames/{frame.name}")

    print(f"Packed {len(png_files)} frames into {output_fma} (fps={fps}, loop={loop})")
    return 0


def create_panorama(name: str, output_dir: Path, speed: float, angle: float) -> int:
    pano_root = output_dir / name
    frames_dir = pano_root / "panorama"
    frames_dir.mkdir(parents=True, exist_ok=True)

    props_path = pano_root / "properties.txt"
    props_content = (
        "type = panorama\n\n"
        "panorama-meta {\n"
        f"  name = {name}\n"
        f"  speed = {speed}\n"
        "  fov = 85.0\n"
        f"  angle = {angle}\n"
        "}\n"
    )
    props_path.write_text(props_content, encoding="utf-8")
    print(f"Created panorama configuration at {props_path}")
    print(f"Place equirectangular cube faces (1:1 square PNGs) in {frames_dir}:")
    print("  panorama_0.png (Front/North), panorama_1.png (Right/East), panorama_2.png (Back/South),")
    print("  panorama_3.png (Left/West),   panorama_4.png (Up/Top),     panorama_5.png (Down/Bottom)")
    return 0


def check_nineslice(width: int, height: int, border_x: int, border_y: int) -> int:
    print(f"=== Nine-Slice Geometry Check ({width}x{height}px, border_x={border_x}, border_y={border_y}) ===")
    if border_x * 2 >= width:
        print(f"[ERROR] border_x * 2 ({border_x * 2}px) must be strictly less than texture width ({width}px)!")
        return 1
    if border_y * 2 >= height:
        print(f"[ERROR] border_y * 2 ({border_y * 2}px) must be strictly less than texture height ({height}px)!")
        return 1
    center_w = width - (border_x * 2)
    center_h = height - (border_y * 2)
    print(f"[OK] Valid 9-slice grid! Stretchable center slice is {center_w}x{center_h}px.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="FancyMenu v3 Designer Helper CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_val = sub.add_parser("validate-layout", help="Validate a FancyMenu .txt layout file")
    p_val.add_argument("layout", type=Path)

    p_fma = sub.add_parser("pack-fma", help="Pack PNG frames into a .fma animation archive")
    p_fma.add_argument("frames_dir", type=Path)
    p_fma.add_argument("output_fma", type=Path)
    p_fma.add_argument("--fps", type=int, default=30)
    p_fma.add_argument("--loop", type=lambda x: x.lower() == "true", default=True)

    p_pano = sub.add_parser("create-panorama", help="Scaffold a cubic panorama pack folder")
    p_pano.add_argument("name", type=str)
    p_pano.add_argument("output_dir", type=Path)
    p_pano.add_argument("--speed", type=float, default=1.0)
    p_pano.add_argument("--angle", type=float, default=25.0)

    p_ns = sub.add_parser("check-nineslice", help="Check 9-slice texture dimensions and borders")
    p_ns.add_argument("width", type=int)
    p_ns.add_argument("height", type=int)
    p_ns.add_argument("border_x", type=int)
    p_ns.add_argument("border_y", type=int)

    args = parser.parse_args()
    if args.cmd == "validate-layout":
        return validate_layout(args.layout)
    if args.cmd == "pack-fma":
        return pack_fma(args.frames_dir, args.output_fma, args.fps, args.loop)
    if args.cmd == "create-panorama":
        return create_panorama(args.name, args.output_dir, args.speed, args.angle)
    if args.cmd == "check-nineslice":
        return check_nineslice(args.width, args.height, args.border_x, args.border_y)
    return 0


if __name__ == "__main__":
    sys.exit(main())
