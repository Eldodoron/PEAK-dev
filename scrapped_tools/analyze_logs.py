import re
import os
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def analyze_log(log_path):
    if not os.path.exists(log_path):
        print(f"Log file not found: {log_path}")
        return

    print(f"Analyzing {log_path} (size: {os.path.getsize(log_path):,} bytes)...")

    # Regular expressions for log lines
    # e.g. [01:30:14] [Server thread/ERROR] [apotheosis/]: ...
    # or [01:30:14] [Render thread/WARN] [something]: ...
    log_pattern = re.compile(r"^\[(?P<time>[^\]]+)\] \[(?P<thread>[^/]+)/(?P<level>[A-Z]+)\] \[(?P<mod>[^\]]+)\]: (?P<msg>.*)$")

    errors_by_mod = defaultdict(lambda: defaultdict(list))
    warns_by_mod = defaultdict(lambda: defaultdict(list))
    other_errors = []

    current_error = None

    with open(log_path, "r", encoding="utf-8", errors="replace") as f:
        for line_num, line in enumerate(f, start=1):
            line_str = line.rstrip()
            match = log_pattern.match(line_str)
            if match:
                level = match.group("level")
                mod = match.group("mod").strip("/")
                msg = match.group("msg")

                if level == "ERROR":
                    # Normalize message for grouping (strip numbers, variable IDs)
                    norm_msg = re.sub(r"0x[0-9a-fA-F]+", "<hex>", msg)
                    errors_by_mod[mod][norm_msg].append((line_num, line_str))
                    current_error = (mod, norm_msg)
                elif level == "WARN":
                    norm_msg = re.sub(r"0x[0-9a-fA-F]+", "<hex>", msg)
                    warns_by_mod[mod][norm_msg].append((line_num, line_str))
                    current_error = None
                else:
                    current_error = None
            else:
                if current_error and line_str.startswith("\tat "):
                    # Stack trace continuation
                    pass

    report_path = "scrapped_tools/log_analysis_report.txt"
    with open(report_path, "w", encoding="utf-8") as out:
        out.write("="*80 + "\n")
        out.write("LOG ERROR SUMMARY (by Mod / Category)\n")
        out.write("="*80 + "\n")

        total_error_count = 0
        for mod in sorted(errors_by_mod.keys()):
            mod_errors = errors_by_mod[mod]
            mod_total = sum(len(samples) for samples in mod_errors.values())
            total_error_count += mod_total
            out.write(f"\n[{mod}] - Total Errors: {mod_total}\n")
            for norm_msg, samples in sorted(mod_errors.items(), key=lambda x: len(x[1]), reverse=True):
                out.write(f"  ({len(samples)}x) Line {samples[0][0]}: {samples[0][1]}\n")

        out.write(f"\nTotal Errors Found: {total_error_count}\n")

        out.write("\n" + "="*80 + "\n")
        out.write("TOP WARNING SUMMARY (by Mod / Category)\n")
        out.write("="*80 + "\n")
        for mod in sorted(warns_by_mod.keys(), key=lambda m: sum(len(s) for s in warns_by_mod[m].values()), reverse=True):
            mod_warns = warns_by_mod[mod]
            mod_total = sum(len(samples) for samples in mod_warns.values())
            out.write(f"\n[{mod}] - Total Warnings: {mod_total}\n")
            for norm_msg, samples in sorted(mod_warns.items(), key=lambda x: len(x[1]), reverse=True)[:10]:
                out.write(f"  ({len(samples)}x) Line {samples[0][0]}: {samples[0][1]}\n")

    print(f"\nAnalysis complete. Full report written to {report_path}.")
    print(f"Total Errors Found: {total_error_count}")

if __name__ == "__main__":
    analyze_log("minecraft/logs/latest.log")
