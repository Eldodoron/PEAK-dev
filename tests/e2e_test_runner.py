#!/usr/bin/env python3
"""
E2E Automated Test Suite Runner for PEAK Modpack AI Sanitization & Tool Archiving.
Supports tiered execution, detailed terminal reporting, JSON export, and automated exit codes.

Usage:
  python tests/e2e_test_runner.py [--tier {1,2,3,4,all}] [--json-report PATH] [--no-color] [-v]
"""
import argparse
from pathlib import Path
import sys
import time
import unittest

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Ensure UTF-8 output on Windows terminals if possible
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from tests.helpers.report_formatter import SingleTestResult, TestReporter
from tests.test_tier1_feature_coverage import TestTier1FeatureCoverage
from tests.test_tier2_boundary_cases import TestTier2BoundaryCases
from tests.test_tier3_functional_preservation import TestTier3FunctionalPreservation
from tests.test_tier4_workload_scenarios import TestTier4WorkloadScenarios


class CustomTestResult(unittest.TestResult):
    """Custom TestResult that streams formatted test progress to TestReporter."""

    def __init__(self, reporter: TestReporter, tier_name: str, verbose: bool = False):
        super().__init__()
        self.reporter = reporter
        self.tier_name = tier_name
        self.verbose = verbose
        self._start_time = 0.0

    def startTest(self, test):
        super().startTest(test)
        self._start_time = time.perf_counter()

    def addSuccess(self, test):
        super().addSuccess(test)
        duration_ms = (time.perf_counter() - self._start_time) * 1000
        doc = test.shortDescription() or test._testMethodName
        self.reporter.record_result(SingleTestResult(
            test_id=test.id(),
            tier=self.tier_name,
            name=doc,
            status="PASS",
            duration_ms=duration_ms,
        ))

    def addFailure(self, test, err):
        super().addFailure(test, err)
        duration_ms = (time.perf_counter() - self._start_time) * 1000
        doc = test.shortDescription() or test._testMethodName
        err_msg = str(err[1])
        self.reporter.record_result(SingleTestResult(
            test_id=test.id(),
            tier=self.tier_name,
            name=doc,
            status="FAIL",
            duration_ms=duration_ms,
            message=err_msg,
        ))

    def addError(self, test, err):
        super().addError(test, err)
        duration_ms = (time.perf_counter() - self._start_time) * 1000
        doc = test.shortDescription() or test._testMethodName
        err_msg = str(err[1])
        self.reporter.record_result(SingleTestResult(
            test_id=test.id(),
            tier=self.tier_name,
            name=doc,
            status="ERROR",
            duration_ms=duration_ms,
            message=err_msg,
        ))

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        duration_ms = (time.perf_counter() - self._start_time) * 1000
        doc = test.shortDescription() or test._testMethodName
        self.reporter.record_result(SingleTestResult(
            test_id=test.id(),
            tier=self.tier_name,
            name=doc,
            status="SKIP",
            duration_ms=duration_ms,
            message=reason,
        ))


def run_tier(suite_cls, tier_name: str, tier_desc: str, reporter: TestReporter, verbose: bool):
    reporter.print_tier_header(tier_name, tier_desc)
    suite = unittest.TestLoader().loadTestsFromTestCase(suite_cls)
    custom_result = CustomTestResult(reporter, tier_name=tier_name, verbose=verbose)
    suite.run(custom_result)
    return custom_result


def main():
    parser = argparse.ArgumentParser(
        description="E2E Test Runner for PEAK Modpack AI Sanitization & Archiving"
    )
    parser.add_argument(
        "--tier",
        choices=["1", "2", "3", "4", "all"],
        default="all",
        help="Select which tier of tests to execute (default: all)",
    )
    parser.add_argument(
        "--json-report",
        type=Path,
        default=PROJECT_ROOT / "tests" / "test_report.json",
        help="Path to save execution JSON report (default: tests/test_report.json)",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored ANSI terminal output",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )

    args = parser.parse_args()

    reporter = TestReporter(use_colors=not args.no_color)
    reporter.print_banner("PEAK MODPACK — E2E TEST SUITE RUNNER")

    start_total_time = time.perf_counter()

    tier_map = {
        "1": (TestTier1FeatureCoverage, "Tier 1", "Feature Coverage (Archiving, AI Regex, JS/JSON Parse, Credits)"),
        "2": (TestTier2BoundaryCases, "Tier 2", "Boundary & Corner Cases (Regex Variations, Comments, Mojibake)"),
        "3": (TestTier3FunctionalPreservation, "Tier 3", "Cross-Feature & Functional Preservation (Logic, Geometry, Tags)"),
        "4": (TestTier4WorkloadScenarios, "Tier 4", "Real-World Workload Scenarios (Deep AST, Modpack Assets, SNBT)"),
    }

    if args.tier == "all":
        tiers_to_run = ["1", "2", "3", "4"]
    else:
        tiers_to_run = [args.tier]

    for tier_key in tiers_to_run:
        cls, t_name, t_desc = tier_map[tier_key]
        run_tier(cls, t_name, t_desc, reporter, args.verbose)

    total_duration = time.perf_counter() - start_total_time
    success = reporter.finalize(total_duration)

    if args.json_report:
        reporter.save_json_report(args.json_report)
        print(f"Detailed JSON execution report saved to: {args.json_report}")

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
