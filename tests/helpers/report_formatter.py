"""
Test Result Formatter and Terminal Reporter for E2E Test Suite.
Provides ANSI colored console outputs, test summary tables, and JSON report generation.
"""
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
import json
import sys


# ANSI Escape Codes for Rich Terminal Output
class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"


@dataclass
class SingleTestResult:
    test_id: str
    tier: str
    name: str
    status: str  # "PASS", "FAIL", "SKIP", "ERROR"
    duration_ms: float
    message: Optional[str] = None
    details: Optional[Dict[str, Any]] = None


@dataclass
class SuiteReport:
    timestamp: str
    total_tests: int = 0
    passed_tests: int = 0
    failed_tests: int = 0
    skipped_tests: int = 0
    error_tests: int = 0
    duration_seconds: float = 0.0
    overall_status: str = "PENDING"
    tier_results: Dict[str, List[SingleTestResult]] = field(default_factory=dict)
    summary_by_tier: Dict[str, Dict[str, int]] = field(default_factory=dict)


class TestReporter:
    def __init__(self, use_colors: bool = True):
        self.use_colors = use_colors and sys.stdout.isatty()
        self.report = SuiteReport(
            timestamp=datetime.now(timezone.utc).isoformat(),
            tier_results={"Tier 1": [], "Tier 2": [], "Tier 3": [], "Tier 4": []},
            summary_by_tier={
                "Tier 1": {"passed": 0, "failed": 0, "skipped": 0, "errors": 0},
                "Tier 2": {"passed": 0, "failed": 0, "skipped": 0, "errors": 0},
                "Tier 3": {"passed": 0, "failed": 0, "skipped": 0, "errors": 0},
                "Tier 4": {"passed": 0, "failed": 0, "skipped": 0, "errors": 0},
            },
        )

    def colorize(self, text: str, color: str) -> str:
        if not self.use_colors:
            return text
        return f"{color}{text}{Colors.RESET}"

    def print_banner(self, title: str):
        bar = "=" * 78
        print(self.colorize(bar, Colors.CYAN))
        print(self.colorize(f"  {title}", Colors.BOLD + Colors.CYAN))
        print(self.colorize(bar, Colors.CYAN))

    def print_tier_header(self, tier_name: str, tier_desc: str):
        print("\n" + self.colorize(f"--- {tier_name.upper()}: {tier_desc} ---", Colors.BOLD + Colors.BLUE))

    def record_result(self, result: SingleTestResult):
        tier_key = result.tier
        if tier_key not in self.report.tier_results:
            self.report.tier_results[tier_key] = []
            self.report.summary_by_tier[tier_key] = {"passed": 0, "failed": 0, "skipped": 0, "errors": 0}

        self.report.tier_results[tier_key].append(result)
        self.report.total_tests += 1

        if result.status == "PASS":
            self.report.passed_tests += 1
            self.report.summary_by_tier[tier_key]["passed"] += 1
            status_str = self.colorize("PASS", Colors.GREEN)
        elif result.status == "FAIL":
            self.report.failed_tests += 1
            self.report.summary_by_tier[tier_key]["failed"] += 1
            status_str = self.colorize("FAIL", Colors.RED)
        elif result.status == "SKIP":
            self.report.skipped_tests += 1
            self.report.summary_by_tier[tier_key]["skipped"] += 1
            status_str = self.colorize("SKIP", Colors.YELLOW)
        else:
            self.report.error_tests += 1
            self.report.summary_by_tier[tier_key]["errors"] += 1
            status_str = self.colorize("ERROR", Colors.RED + Colors.BOLD)

        duration_str = f"{result.duration_ms:.1f}ms"
        print(f"  [{status_str}] {result.name:<58} ({duration_str})")
        if result.message and result.status in ("FAIL", "ERROR"):
            for line in result.message.strip().splitlines():
                print(self.colorize(f"         > {line}", Colors.RED))

    def finalize(self, total_duration: float) -> bool:
        self.report.duration_seconds = total_duration
        if self.report.failed_tests == 0 and self.report.error_tests == 0:
            self.report.overall_status = "PASSED"
            success = True
        else:
            self.report.overall_status = "FAILED"
            success = False

        self.print_summary()
        return success

    def print_summary(self):
        bar = "=" * 78
        print("\n" + self.colorize(bar, Colors.CYAN))
        print(self.colorize("  E2E TEST SUITE EXECUTION SUMMARY", Colors.BOLD))
        print(self.colorize(bar, Colors.CYAN))

        for tier, counts in self.report.summary_by_tier.items():
            t_pass = counts["passed"]
            t_fail = counts["failed"]
            t_err = counts["errors"]
            t_skip = counts["skipped"]
            t_total = t_pass + t_fail + t_err + t_skip
            status = self.colorize("PASS", Colors.GREEN) if (t_fail == 0 and t_err == 0 and t_total > 0) else self.colorize("FAIL", Colors.RED)
            print(f"  {tier:<10} : {status} | Passed: {t_pass:>2} | Failed: {t_fail:>2} | Errors: {t_err:>2} | Total: {t_total:>2}")

        print(self.colorize("-" * 78, Colors.DIM))
        overall_color = Colors.GREEN if self.report.overall_status == "PASSED" else Colors.RED
        print(f"  Total Duration : {self.report.duration_seconds:.2f}s")
        print(f"  Total Tests    : {self.report.total_tests}")
        print(f"  Passed         : {self.colorize(str(self.report.passed_tests), Colors.GREEN)}")
        print(f"  Failed         : {self.colorize(str(self.report.failed_tests), Colors.RED if self.report.failed_tests else Colors.GREEN)}")
        print(f"  Errors         : {self.colorize(str(self.report.error_tests), Colors.RED if self.report.error_tests else Colors.GREEN)}")
        print(f"  Overall Status : {self.colorize(self.report.overall_status, Colors.BOLD + overall_color)}")
        print(self.colorize(bar, Colors.CYAN) + "\n")

    def save_json_report(self, output_path: Path):
        output_path.parent.mkdir(parents=True, exist_ok=True)
        # Convert to serializable dict
        data = {
            "timestamp": self.report.timestamp,
            "overall_status": self.report.overall_status,
            "duration_seconds": self.report.duration_seconds,
            "total_tests": self.report.total_tests,
            "passed_tests": self.report.passed_tests,
            "failed_tests": self.report.failed_tests,
            "skipped_tests": self.report.skipped_tests,
            "error_tests": self.report.error_tests,
            "summary_by_tier": self.report.summary_by_tier,
            "tier_results": {
                tier: [asdict(r) for r in results]
                for tier, results in self.report.tier_results.items()
            },
        }
        output_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
