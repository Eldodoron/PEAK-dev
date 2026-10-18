import os
import sys

def parse_report():
    with open('scrapped_tools/log_analysis_report.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.split('\n')
    with open('scrapped_tools/detailed_breakdown.txt', 'w', encoding='utf-8') as out:
        current_mod = None
        for line in lines:
            if line.startswith('[') and ' - Total Errors:' in line:
                current_mod = line
                out.write('\n' + '='*80 + '\n')
                out.write(line + '\n')
                out.write('='*80 + '\n')
                continue
            if current_mod:
                # write all lines under this mod
                if line.startswith('[') and ' - Total Errors:' in line:
                    continue
                out.write(line + '\n')

    print("Detailed breakdown written to scrapped_tools/detailed_breakdown.txt")

if __name__ == '__main__':
    parse_report()
