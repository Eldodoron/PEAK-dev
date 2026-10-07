import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scrapped_tools")))
import sync_to_lite as stl

class TestSyncToLiteSafety(unittest.TestCase):

    def test_directory_invariants(self):
        """Ensures source is PEAK-dev and target is PEAK-Lite, never the same folder."""
        self.assertNotEqual(
            os.path.realpath(stl.BASE_DEV),
            os.path.realpath(stl.BASE_LITE),
            "Source and target must be distinct directories."
        )
        self.assertEqual(os.path.basename(os.path.realpath(stl.BASE_DEV)), "PEAK-dev")
        self.assertEqual(os.path.basename(os.path.realpath(stl.BASE_LITE)), "PEAK-Lite")

    def test_refuse_write_outside_lite(self):
        """Guarantees that assert_safe_target_path aborts if targeting outside PEAK-Lite."""
        # Attempting to target Dev
        with self.assertRaises(RuntimeError):
            stl.assert_safe_target_path(os.path.join(stl.BASE_DEV, "minecraft", "mods", "test.jar"))

        # Attempting to target C:\ Windows or system dirs
        with self.assertRaises(RuntimeError):
            stl.assert_safe_target_path(r"C:\Windows\System32\cmd.exe")

    def test_refuse_write_to_protected_directories(self):
        """Guarantees that saves, logs, screenshots, crash-reports can never be touched."""
        protected_targets = [
            os.path.join(stl.LITE_MC, "saves", "New World"),
            os.path.join(stl.LITE_MC, "saves", "test_world", "level.dat"),
            os.path.join(stl.LITE_MC, "screenshots", "2026-10-04.png"),
            os.path.join(stl.LITE_MC, "logs", "latest.log"),
            os.path.join(stl.LITE_MC, "crash-reports", "crash.txt"),
            os.path.join(stl.LITE_MC, "usercache.json"),
            os.path.join(stl.LITE_MC, "usernamecache.json")
        ]
        for pt in protected_targets:
            with self.assertRaises(RuntimeError, msg=f"Should have protected: {pt}"):
                stl.assert_safe_target_path(pt)

    def test_exclusions_absent_in_lite(self):
        """Verifies that none of the 30 excluded components exist in PEAK-Lite."""
        exclusions = stl.load_exclusions()
        self.assertGreaterEqual(len(exclusions), 20, "Exclusions file must be populated.")

        # Check mods in Lite
        lite_mods_dir = os.path.join(stl.LITE_MC, "mods")
        if os.path.exists(lite_mods_dir):
            for m in os.listdir(lite_mods_dir):
                self.assertNotIn(m.lower(), exclusions, f"Excluded mod found in Lite: {m}")

        # Check resource packs in Lite
        lite_rp_dir = os.path.join(stl.LITE_MC, "config", "paxi", "resourcepacks")
        if os.path.exists(lite_rp_dir):
            for rp in os.listdir(lite_rp_dir):
                self.assertNotIn(rp.lower(), exclusions, f"Excluded pack found in Lite: {rp}")

    def test_lite_instance_identity_preserved(self):
        """Ensures that PEAK-Lite retains its unique name and independent UUID."""
        lite_cfg = os.path.join(stl.BASE_LITE, "instance.cfg")
        self.assertTrue(os.path.exists(lite_cfg))

        with open(lite_cfg, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("name=PEAK Lite", content)
        self.assertIn("ExportName=PEAK-Lite", content)
        self.assertIn("uuid=", content)

if __name__ == "__main__":
    unittest.main()
