import json
import sys
import os

path = os.environ.get('TEMP') + '/spark_full.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

thread = data['threads'][0]
print("Thread 0 name:", thread.get('name'))
print("Thread 0 time:", thread.get('time'))
print("Thread 0 children length:", len(thread.get('children', [])))
if thread.get('children'):
    print("Thread 0 first child:", thread['children'][0])
    
print("MethodSources keys example:", list(data['methodSources'].keys())[:5])
print("MethodSources values example:", [data['methodSources'][k] for k in list(data['methodSources'].keys())[:5]])

print("ClassSources keys example:", list(data['classSources'].keys())[:5])
print("ClassSources values example:", [data['classSources'][k] for k in list(data['classSources'].keys())[:5]])

