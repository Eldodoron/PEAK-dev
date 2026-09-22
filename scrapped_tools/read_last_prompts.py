import json

transcript_path = r"C:\Users\chris\.gemini\antigravity\brain\e6ce4756-c251-406e-afaa-90894d34048e\.system_generated\logs\transcript.jsonl"
prompts = []
with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get("type") == "USER_INPUT":
                prompts.append(data.get("content", ""))
        except Exception:
            pass

print("Total user prompts:", len(prompts))
if prompts:
    print("=== Last prompt ===")
    print(prompts[-1])
