"""
Tier 4: Real-World Workload Scenarios Test Suite.
Simulates real-world modpack execution and asset verification:
- Full modpack asset and script verification across 170+ files
- Deep AST parsing of all KubeJS scripts
- FTB Quest SNBT parsing, structural validation, and zero-AI check across 3,310+ lines
"""
from pathlib import Path
from typing import Dict, List
import unittest

from tests.helpers.config import (
    CONFIG_DIR,
    FTBQUESTS_LANG_FILE,
    KUBEJS_DIR,
    MINECRAFT_DIR,
)
from tests.helpers.js_validator import JSValidator
from tests.helpers.json_validator import JSONValidator
from tests.helpers.regex_scanner import RegexScanner
from tests.helpers.snbt_parser import SNBTParser


class TestTier4WorkloadScenarios(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scanner = RegexScanner()
        cls.js_validator = JSValidator()
        cls.json_validator = JSONValidator()
        cls.snbt_parser = SNBTParser()

    def test_01_full_kubejs_subsystem_verification(self):
        """Simulates full KubeJS subsystem load: scans all 170+ files for integrity and clean syntax."""
        self.assertTrue(KUBEJS_DIR.exists(), f"KubeJS directory {KUBEJS_DIR} not found.")

        all_files = list(KUBEJS_DIR.rglob("*"))
        file_count = len([f for f in all_files if f.is_file()])
        self.assertGreaterEqual(file_count, 100, f"Expected at least 100 files in kubejs/, found {file_count}")

        # Scan all files for banned AI patterns
        violations = self.scanner.scan_directory(KUBEJS_DIR)
        msg = f"KubeJS subsystem contains {len(violations)} AI violations:\n" + "\n".join(
            f" - {v.file_path.name}:{v.line_number}: {v.matched_text}" for v in violations
        )
        self.assertEqual(len(violations), 0, msg)

    def test_02_deep_ast_parsing_and_syntax_of_all_js_scripts(self):
        """Performs deep AST parsing on all 64 JS scripts to ensure zero syntax or bracket errors."""
        js_files = list(KUBEJS_DIR.rglob("*.js"))
        self.assertGreaterEqual(len(js_files), 60)

        for js_file in js_files:
            valid, err = self.js_validator.check_syntax_node(js_file)
            self.assertTrue(
                valid,
                f"Deep AST parse failed on {js_file.relative_to(MINECRAFT_DIR)}: {err}",
            )

    def test_03_ftbquests_snbt_localization_and_zero_ai_check(self):
        """Parses the entire 3,310+ line FTB Quests localization file, validating all 680+ quests and clean text."""
        self.assertTrue(
            FTBQUESTS_LANG_FILE.exists(),
            f"FTB Quests lang file not found: {FTBQUESTS_LANG_FILE}",
        )

        # 1. Parse SNBT file
        parsed_ok, parse_err, data = self.snbt_parser.parse_file(FTBQUESTS_LANG_FILE)
        self.assertTrue(parsed_ok, f"Failed to parse en_us.snbt: {parse_err}")
        self.assertGreater(len(data), 1500, f"Expected >1500 SNBT keys, found {len(data)}")

        # 2. Extract Quests
        quests = self.snbt_parser.extract_quests(data)
        self.assertGreaterEqual(
            len(quests),
            600,
            f"Expected at least 600 quest entries, found {len(quests)}",
        )

        # 3. Check for banned AI signatures in SNBT content
        violations = self.scanner.scan_file(FTBQUESTS_LANG_FILE)
        msg = f"FTB Quests lang file contains {len(violations)} AI violations:\n" + "\n".join(
            f" - Line {v.line_number}: '{v.matched_text}' -> {v.line_content}" for v in violations
        )
        self.assertEqual(len(violations), 0, msg)

    def test_04_mod_configs_integrity_and_cleanliness(self):
        """Verifies that all mod configuration files in config/ and defaultconfigs/ remain valid and clean."""
        self.assertTrue(CONFIG_DIR.exists(), f"Config directory {CONFIG_DIR} not found.")

        config_files = list(CONFIG_DIR.rglob("*"))
        readable_configs = [
            f for f in config_files
            if f.is_file() and f.suffix.lower() in {".json", ".toml", ".cfg", ".yaml", ".json5"}
        ]
        self.assertGreaterEqual(len(readable_configs), 50)

        violations = []
        for cfg in readable_configs:
            v_list = self.scanner.scan_file(cfg)
            violations.extend(v_list)

        msg = f"Config files contain {len(violations)} AI violations:\n" + "\n".join(
            f" - {v.file_path.name}:{v.line_number}: {v.matched_text}" for v in violations
        )
        self.assertEqual(len(violations), 0, msg)


if __name__ == "__main__":
    unittest.main()
