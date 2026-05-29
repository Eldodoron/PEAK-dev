import json
import sys
import os

path = os.environ.get('TEMP') + '/spark_full.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def get_node_name(node):
    class_name = node.get('className', '')
    method_name = node.get('methodName', '')
    return f"{class_name}.{method_name}" if class_name or method_name else "Unknown"

def get_total_time(node):
    return sum(node.get('times', []))

def process_node(node_idx, all_nodes, depth, thread_total_time, out_lines):
    if node_idx >= len(all_nodes): return
    node = all_nodes[node_idx]
    
    node_time = get_total_time(node)
    percent = (node_time / thread_total_time) * 100 if thread_total_time > 0 else 0
    if percent < 1.0: # threshold 1%
        return
    
    name = get_node_name(node)
    out_lines.append("  " * depth + f"{name} - {percent:.1f}%")
    
    refs = node.get('childrenRefs', [])
    child_nodes = [(ref, all_nodes[ref]) for ref in refs if ref < len(all_nodes)]
    child_nodes.sort(key=lambda x: get_total_time(x[1]), reverse=True)
    
    for ref, child in child_nodes:
        process_node(ref, all_nodes, depth + 1, thread_total_time, out_lines)

out_lines = []
for thread in data.get('threads', []):
    thread_name = thread.get('name')
    if "Server thread" not in thread_name:
        continue
    out_lines.append(f"Thread: {thread_name}")
    
    thread_total_time = get_total_time(thread)
    all_nodes = thread.get('children', [])
    
    root_refs = thread.get('childrenRefs', [])
    root_nodes = [(ref, all_nodes[ref]) for ref in root_refs if ref < len(all_nodes)]
    root_nodes.sort(key=lambda x: get_total_time(x[1]), reverse=True)
    
    for ref, root in root_nodes:
        process_node(ref, all_nodes, 1, thread_total_time, out_lines)

with open(os.environ.get('TEMP') + '/spark_hotspots.txt', 'w') as f:
    f.write("\n".join(out_lines))
print("Hotspots written to spark_hotspots.txt")
