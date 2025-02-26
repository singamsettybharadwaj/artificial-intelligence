# Defining the tree structure
root = {"value": "A", "children": []}
b = {"value": "B", "children": []}
c = {"value": "C", "children": []}
d = {"value": "D", "children": []}
e = {"value": "E", "children": []}
f = {"value": "F", "children": []}

# Building the tree structure
root["children"].append(b)
root["children"].append(c)
b["children"].append(d)
b["children"].append(e)
c["children"].append(f)
# Implementing BFS
queue = [(root, 0)]
while queue:
    node, level = queue.pop(0)
    print("  " * level + node["value"])  # Print node with indentation based on level
    for child in node["children"]:  
        queue.append((child, level + 1))
