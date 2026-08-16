"""
Blockbench 3D Model Validator for Custom Flowerbed Models.
Validates model JSON geometry, elements, textures, and ensures clean Blockbench credits.
"""
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import json
import re

from tests.helpers.config import ASSETS_MODELS_DIR, FLOWERBED_MODEL_FILES
from tests.helpers.json_validator import JSONValidator


class BlockbenchModelValidator:
    def __init__(self, models_dir: Optional[Path] = None):
        self.models_dir = models_dir or ASSETS_MODELS_DIR

    def validate_flowerbed_model(self, file_path: Path) -> Tuple[bool, List[str]]:
        """
        Validates an individual flowerbed model file for:
        1. JSON parseability
        2. Clean Blockbench credit without AI mentions
        3. Valid ambientocclusion and textures dictionary
        4. Valid elements array with non-empty cubes, coordinates, and face textures
        """
        errors: List[str] = []
        is_valid, err_msg, data = JSONValidator.validate_file(file_path)

        if not is_valid or not isinstance(data, dict):
            return False, [f"Invalid JSON: {err_msg}"]

        # 1. Check Credit field
        credit = data.get("credit", "")
        if not credit:
            errors.append(f"{file_path.name}: Missing 'credit' property.")
        elif re.search(r"(?i)antigravity|openai|chatgpt|claude|prompt|fixed\s+by\s+antigravity", credit):
            errors.append(f"{file_path.name}: AI signature found in credit: '{credit}'")
        elif "Blockbench" not in credit:
            errors.append(f"{file_path.name}: 'credit' does not mention standard Blockbench: '{credit}'")

        # 2. Check ambientocclusion
        if "ambientocclusion" not in data:
            errors.append(f"{file_path.name}: Missing 'ambientocclusion' property.")

        # 3. Check textures
        textures = data.get("textures", {})
        if not isinstance(textures, dict):
            errors.append(f"{file_path.name}: 'textures' is not a dictionary.")
        else:
            required_tex = ["particle", "flowerbed", "stem"]
            for tex_key in required_tex:
                if tex_key not in textures:
                    errors.append(f"{file_path.name}: Missing required texture '{tex_key}'.")

        # 4. Check elements
        elements = data.get("elements", [])
        if not isinstance(elements, list) or len(elements) == 0:
            errors.append(f"{file_path.name}: 'elements' must be a non-empty array of cube definitions.")
        else:
            for idx, elem in enumerate(elements):
                if not isinstance(elem, dict):
                    errors.append(f"{file_path.name}: Element #{idx} is not an object.")
                    continue
                if "from" not in elem or "to" not in elem:
                    errors.append(f"{file_path.name}: Element #{idx} missing 'from' or 'to' coordinates.")
                if "faces" not in elem or not isinstance(elem["faces"], dict) or len(elem["faces"]) == 0:
                    errors.append(f"{file_path.name}: Element #{idx} missing valid 'faces' definition.")

        return len(errors) == 0, errors

    def validate_all_flowerbeds(self) -> Tuple[bool, Dict[str, List[str]]]:
        """Validates all 4 flowerbed models in the assets directory."""
        results = {}
        all_passed = True

        for model_file in FLOWERBED_MODEL_FILES:
            full_path = self.models_dir / model_file
            if not full_path.exists():
                results[model_file] = [f"File does not exist: {full_path}"]
                all_passed = False
                continue

            passed, errors = self.validate_flowerbed_model(full_path)
            results[model_file] = errors
            if not passed:
                all_passed = False

        return all_passed, results
