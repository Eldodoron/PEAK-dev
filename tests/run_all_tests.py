#!/usr/bin/env python3
"""
Convenience entry point to execute the complete E2E test suite.
"""
from pathlib import Path
import subprocess
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RUNNER = PROJECT_ROOT / "tests" / "e2e_test_runner.py"

if __name__ == "__main__":
    cmd = [sys.executable, str(RUNNER)] + sys.argv[1:]
    proc = subprocess.run(cmd)
    sys.exit(proc.returncode)
