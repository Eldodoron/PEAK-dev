"""
Tier 1: Feature Coverage Test Suite.
Verifies core acceptance criteria:
- No .py files in minecraft/
- All 24 .py maintenance tools archived in scrapped_tools/
- Zero AI regex matches across all text files in minecraft/
- All .js files in kubejs/ parse cleanly with zero syntax errors
- All .json files in minecraft/ parse cleanly
- Blockbench flowerbed 3D model credits cleaned
"""
from pathlib import Path
from typing import List
import os
import unittest

from tests.helpers.config import (
    ASSETS_MODELS_DIR,
    EXPECTED_PY_FILES,
    FLOWERBED_MODEL_FILES,
    KUBEJS_DIR,
    MINECRAFT_DIR,
    ORIGINAL_PY_REL_PATHS,
    SCRAPPED_TOOLS_DIR,
)
from tests.helpers.js_validator import JSValidator
from tests.helpers.json_validator import JSONValidator
from tests.helpers.model_validator import BlockbenchModelValidator
from tests.helpers.regex_scanner import RegexScanner


class TestTier1FeatureCoverage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scanner = RegexScanner()
        cls.js_validator = JSValidator()
        cls.json_validator = JSONValidator()
        cls.model_validator = BlockbenchModelValidator()

    def test_01_no_python_files_remain_in_minecraft(self):
        """Verify that zero .py files remain anywhere inside the minecraft/ directory tree."""
        py_files: List[Path] = []
        if MINECRAFT_DIR.exists():
            for root, _, files in os.walk(MINECRAFT_DIR):
                for f in files:
                    if f.lower().endswith(".py"):
                        py_files.append(Path(root) / f)

        msg = (
            f"Found {len(py_files)} lingering .py file(s) in {MINECRAFT_DIR}:\n"
            + "\n".join(f" - {p.relative_to(MINECRAFT_DIR)}" for p in py_files)
        )
        self.assertEqual(len(py_files), 0, msg)

    def test_02_all_python_scripts_archived_in_scrapped_tools(self):
        """Verify that all 24 maintenance Python utility scripts exist in scrapped_tools/."""
        self.assertTrue(
            SCRAPPED_TOOLS_DIR.exists(),
            f"Archive directory {SCRAPPED_TOOLS_DIR} does not exist.",
        )

        # Collect all .py files currently in scrapped_tools/
        archived_files = set()
        for root, _, files in os.walk(SCRAPPED_TOOLS_DIR):
            for f in files:
                if f.lower().endswith(".py"):
                    archived_files.add(f.lower())

        missing = []
        for expected in EXPECTED_PY_FILES:
            if expected.lower() not in archived_files:
                missing.append(expected)

        msg = (
            f"Missing {len(missing)} expected Python tool(s) in {SCRAPPED_TOOLS_DIR}:\n"
            + "\n".join(f" - {m}" for m in missing)
        )
        self.assertEqual(len(missing), 0, msg)
        self.assertGreaterEqual(
            len(archived_files),
            len(EXPECTED_PY_FILES),
            f"Expected at least {len(EXPECTED_PY_FILES)} archived scripts, found {len(archived_files)}",
        )

    def test_03_zero_banned_ai_signatures_in_minecraft(self):
        """Verify that an exhaustive scan across all readable files in minecraft/ finds zero AI signatures."""
        violations = self.scanner.scan_directory(MINECRAFT_DIR)
        
        if violations:
            details = [
                f"[{v.rule_name}] {v.file_path.relative_to(MINECRAFT_DIR)}:{v.line_number}: '{v.matched_text}' -> Line: {v.line_content}"
                for v in violations
            ]
            msg = f"Found {len(violations)} banned AI signature violation(s) in minecraft/:\n" + "\n".join(details)
            self.assertEqual(len(violations), 0, msg)

    def test_04_all_kubejs_javascript_files_parse_cleanly(self):
        """Verify that 100% of .js scripts in kubejs/ parse cleanly with zero syntax errors."""
        self.assertTrue(KUBEJS_DIR.exists(), f"KubeJS directory {KUBEJS_DIR} not found.")

        js_files = list(KUBEJS_DIR.rglob("*.js"))
        self.assertGreaterEqual(len(js_files), 60, f"Expected at least 60 JS scripts, found {len(js_files)}")

        syntax_errors = []
        for js_file in js_files:
            valid, err = self.js_validator.check_syntax_node(js_file)
            if not valid:
                rel_path = js_file.relative_to(MINECRAFT_DIR)
                syntax_errors.append(f"{rel_path}: {err}")

        msg = f"Syntax errors detected in {len(syntax_errors)} JS script(s):\n" + "\n".join(syntax_errors)
        self.assertEqual(len(syntax_errors), 0, msg)

    def test_05_all_minecraft_json_files_parse_cleanly(self):
        """Verify that all .json files in minecraft/ (assets, worldgen, configs, models) parse without syntax errors."""
        from tests.helpers.regex_scanner import DEFAULT_EXCLUDE_DIRS
        json_files = []
        for root, dirs, files in os.walk(MINECRAFT_DIR):
            dirs[:] = [d for d in dirs if d not in DEFAULT_EXCLUDE_DIRS and not d.startswith(".")]
            for f in files:
                if f.lower().endswith(".json"):
                    json_files.append(Path(root) / f)

        self.assertGreater(len(json_files), 50, f"Expected at least 50 JSON files, found {len(json_files)}")

        json_errors = []
        for j_file in json_files:
            valid, err, _ = self.json_validator.validate_file(j_file)
            if not valid:
                rel_path = j_file.relative_to(MINECRAFT_DIR)
                json_errors.append(f"{rel_path}: {err}")

        msg = f"JSON parse errors in {len(json_errors)} file(s):\n" + "\n".join(json_errors)
        self.assertEqual(len(json_errors), 0, msg)

    def test_06_blockbench_flowerbed_model_credits_cleaned(self):
        """Verify that all flowerbed 3D models retain standard Blockbench credits without AI attribution."""
        passed, results = self.model_validator.validate_all_flowerbeds()
        errors = []
        for model_name, errs in results.items():
            for err in errs:
                errors.append(f"{model_name}: {err}")

        msg = f"Flowerbed model validation failed with {len(errors)} error(s):\n" + "\n".join(errors)
        self.assertTrue(passed, msg)


if __name__ == "__main__":
    unittest.main()
