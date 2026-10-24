"""
Canonical CLI entrypoint for the PEAK Modpack Export & Verification Engine.
Supports PEAK (Dev), PEAK Lite, and PEAK Dedicated Server Pack.
"""
import runpy
import os

if __name__ == "__main__":
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_export_alpha2.py")
    runpy.run_path(script_path, run_name="__main__")
