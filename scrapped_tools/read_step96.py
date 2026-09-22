import json

with open(r'C:\Users\chris\.gemini\antigravity\brain\4621470a-fbef-4973-848e-5f18970291b3\.system_generated\logs\chunks\transcript_full\00000001.jsonl', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        try:
            d = json.loads(line)
            if d.get('step_index') == 96:
                cmd = d['tool_calls'][0]['args']['CommandLine']
                print(cmd)
                break
        except Exception as e:
            pass
