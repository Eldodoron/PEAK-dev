"""
Regex Scanner Engine for AI Attributions, LLM Remnants, and Metadata.
Provides file scanning, text scanning, multiline scanning, and whitelist filtering.
"""
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Set
import os

from tests.helpers.config import BANNED_REGEX_RULES, WHITELIST_PATTERNS


@dataclass
class ScanViolation:
    file_path: Path
    line_number: int
    rule_id: str
    rule_name: str
    matched_text: str
    line_content: str
    description: str


DEFAULT_EXCLUDE_DIRS: Set[str] = {
    ".git", ".continue", ".agents", "libraries", "create.zip",
    "logs", "crash-reports", "saves", "cache", "downloads",
    "Distant_Horizons_server_data", "blueprints", "particular_cache",
    "tmp_irons", "tmp_cei", "create_jar_temp", "panoptic",
}

DEFAULT_EXCLUDE_FILES: Set[str] = {
    "ai_audit_report.md",
    "win_event1784950532001.txt",
}


class RegexScanner:
    def __init__(self, rules=None, whitelist=None, exclude_dirs=None, exclude_files=None):
        self.rules = rules or BANNED_REGEX_RULES
        self.whitelist = whitelist or WHITELIST_PATTERNS
        self.exclude_dirs = exclude_dirs or DEFAULT_EXCLUDE_DIRS
        self.exclude_files = exclude_files or DEFAULT_EXCLUDE_FILES
        self.scannable_extensions: Set[str] = {
            ".js", ".json", ".snbt", ".toml", ".txt", ".md", ".cfg",
            ".yaml", ".yml", ".properties", ".mcmeta", ".zs",
        }

    def is_whitelisted(self, text: str) -> bool:
        for wl_pattern in self.whitelist:
            if wl_pattern.search(text):
                return True
        return False

    def scan_text(self, text: str, file_path: Optional[Path] = None) -> List[ScanViolation]:
        violations: List[ScanViolation] = []
        path = file_path or Path("<in-memory>")
        lines = text.splitlines()

        for line_idx, line in enumerate(lines, 1):
            if self.is_whitelisted(line):
                continue

            for rule in self.rules:
                matches = rule["pattern"].finditer(line)
                for match in matches:
                    matched_str = match.group(0)
                    # Double-check match against whitelist in case whole line wasn't caught
                    if self.is_whitelisted(matched_str):
                        continue
                    violations.append(ScanViolation(
                        file_path=path,
                        line_number=line_idx,
                        rule_id=rule["id"],
                        rule_name=rule["name"],
                        matched_text=matched_str,
                        line_content=line.strip(),
                        description=rule["description"],
                    ))
        return violations

    def scan_file(self, file_path: Path) -> List[ScanViolation]:
        if not file_path.exists() or not file_path.is_file():
            return []

        if file_path.name in self.exclude_files:
            return []

        try:
            content = file_path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            try:
                content = file_path.read_text(encoding="cp1252", errors="replace")
            except Exception:
                return []

        return self.scan_text(content, file_path=file_path)

    def scan_directory(
        self,
        directory: Path,
        extensions: Optional[Set[str]] = None,
        exclude_dirs: Optional[Set[str]] = None,
    ) -> List[ScanViolation]:
        allowed_exts = extensions or self.scannable_extensions
        excluded = exclude_dirs or self.exclude_dirs
        all_violations: List[ScanViolation] = []

        if not directory.exists():
            return []

        for root, dirs, files in os.walk(directory):
            # Prune excluded directories in-place
            dirs[:] = [d for d in dirs if d not in excluded and not d.startswith(".")]

            for file_name in files:
                if file_name in self.exclude_files:
                    continue

                ext = Path(file_name).suffix.lower()
                if allowed_exts and ext not in allowed_exts:
                    continue

                full_path = Path(root) / file_name
                violations = self.scan_file(full_path)
                all_violations.extend(violations)

        return all_violations
