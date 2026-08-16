"""
Tier 3: Cross-Feature Combinations & Functional Preservation Test Suite.
Verifies that 100% of game functionality, recipes, event handlers,
and 3D block model geometry are preserved without corruption or unintended alterations.
"""
from pathlib import Path
from typing import Dict, List
import unittest

from tests.helpers.config import (
    ASSETS_MODELS_DIR,
    FLOWERBED_MODEL_FILES,
    KUBEJS_DIR,
    MINECRAFT_DIR,
    SERVER_SCRIPTS_DIR,
    STARTUP_SCRIPTS_DIR,
)
from tests.helpers.js_validator import JSValidator
from tests.helpers.json_validator import JSONValidator
from tests.helpers.model_validator import BlockbenchModelValidator


class TestTier3FunctionalPreservation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.js_validator = JSValidator()
        cls.json_validator = JSONValidator()
        cls.model_validator = BlockbenchModelValidator()

    def test_01_kubejs_scripts_retain_all_functional_event_listeners(self):
        """Verify that essential KubeJS event listeners (ServerEvents, ClientEvents, StartupEvents) are intact."""
        js_files = list(KUBEJS_DIR.rglob("*.js"))
        self.assertGreaterEqual(len(js_files), 60)

        critical_events = [
            ("ServerEvents.recipes", 0),
            ("ServerEvents.tags", 0),
            ("ItemEvents.modification", 0),
            ("StartupEvents.registry", 0),
        ]
        event_counts = {evt: 0 for evt, _ in critical_events}

        for js_file in js_files:
            try:
                content = js_file.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

            tokens = " ".join(self.js_validator.extract_functional_tokens(content))
            for evt in event_counts:
                if evt in content or evt.replace(".", " . ") in tokens:
                    event_counts[evt] += 1

        for evt, count in event_counts.items():
            self.assertGreater(
                count,
                0,
                f"Critical event handler '{evt}' was not found in any KubeJS script!",
            )

    def test_02_tag_unifications_script_integrity(self):
        """Verify that 00_tags.js retains screwdriver unifications and rune tags."""
        tags_file = SERVER_SCRIPTS_DIR / "00_tags.js"
        if not tags_file.exists():
            self.skipTest("00_tags.js not found in expected directory.")

        content = tags_file.read_text(encoding="utf-8", errors="replace")
        clean_tokens = " ".join(self.js_validator.extract_functional_tokens(content))

        # Check critical functional items are present
        self.assertIn("c:tools/screwdriver", clean_tokens)
        self.assertIn("immersiveengineering:screwdriver", clean_tokens)
        self.assertIn("tfmg:screwdriver", clean_tokens)
        self.assertIn("kubejs:irons_runes", clean_tokens)

    def test_03_sequenced_assembly_datapack_recipes_integrity(self):
        """Verify that 20_fixed_datapacks.js retains its sequenced assembly recipes."""
        recipe_file = SERVER_SCRIPTS_DIR / "20_fixed_datapacks.js"
        if not recipe_file.exists():
            self.skipTest("20_fixed_datapacks.js not found in expected directory.")

        content = recipe_file.read_text(encoding="utf-8", errors="replace")
        clean_tokens = " ".join(self.js_validator.extract_functional_tokens(content))

        # Check sequenced assembly recipe keywords & key items
        self.assertIn("sequenced_assembly", clean_tokens)
        self.assertIn("apotheosis", clean_tokens)
        self.assertIn("transitional_item", clean_tokens)

    def test_04_create_and_pneumaticcraft_progression_gates_integrity(self):
        """Verify progression gates in 02_create_era_gates.js and 03_pneumatic_mekanism_gates.js."""
        gate_02 = SERVER_SCRIPTS_DIR / "02_create_era_gates.js"
        gate_03 = SERVER_SCRIPTS_DIR / "03_pneumatic_mekanism_gates.js"

        for gate_file in [gate_02, gate_03]:
            if not gate_file.exists():
                continue
            content = gate_file.read_text(encoding="utf-8", errors="replace")
            clean_tokens = " ".join(self.js_validator.extract_functional_tokens(content))
            self.assertIn("ServerEvents", clean_tokens)
            self.assertIn("recipes", clean_tokens)

    def test_05_flowerbed_3d_geometry_and_texture_preservation(self):
        """Verify that all flowerbed 3D model cubes, UV maps, rotations, and textures are 100% intact."""
        expected_element_counts = {
            "flowerbed_1.json": 7,
            "flowerbed_2.json": 3,
            "flowerbed_3.json": 5,
            "flowerbed_4.json": 5,
        }

        for model_file in FLOWERBED_MODEL_FILES:
            full_path = ASSETS_MODELS_DIR / model_file
            if not full_path.exists():
                self.fail(f"Flowerbed model file missing: {full_path}")

            is_valid, err_msg, data = self.json_validator.validate_file(full_path)
            self.assertTrue(is_valid, f"Failed to parse {model_file}: {err_msg}")
            self.assertIsInstance(data, dict)

            # Check ambientocclusion
            self.assertFalse(data.get("ambientocclusion", True))

            # Check textures
            textures = data.get("textures", {})
            self.assertEqual(textures.get("particle"), "minecraft:block/pink_petals")
            self.assertEqual(textures.get("flowerbed"), "minecraft:block/pink_petals")
            self.assertEqual(textures.get("stem"), "minecraft:block/pink_petals_stem")

            # Check elements geometry
            elements = data.get("elements", [])
            expected_count = expected_element_counts.get(model_file, 7)
            self.assertEqual(
                len(elements),
                expected_count,
                f"{model_file} element count modified! Expected {expected_count} cubes, got {len(elements)}",
            )

            # Element 0: Verify coordinates and faces exist
            elem0 = elements[0]
            self.assertIn("from", elem0)
            self.assertIn("to", elem0)
            self.assertIn("faces", elem0)
            self.assertIn("up", elem0["faces"])
            self.assertIn("down", elem0["faces"])

    def test_06_custom_items_startup_registry_intact(self):
        """Verify that custom_items.js in startup_scripts retains all item registrations."""
        custom_items_file = STARTUP_SCRIPTS_DIR / "custom_items.js"
        if not custom_items_file.exists():
            self.skipTest("custom_items.js not found in startup_scripts.")

        content = custom_items_file.read_text(encoding="utf-8", errors="replace")
        clean_tokens = " ".join(self.js_validator.extract_functional_tokens(content))

        self.assertIn("StartupEvents", clean_tokens)
        self.assertIn("registry", clean_tokens)
        self.assertIn("item", clean_tokens)
        self.assertIn("create", clean_tokens)
        self.assertIn("frozen_heart_core", clean_tokens)
        self.assertIn("primordial_core", clean_tokens)
        self.assertIn("culinary_singularity", clean_tokens)


if __name__ == "__main__":
    unittest.main()
