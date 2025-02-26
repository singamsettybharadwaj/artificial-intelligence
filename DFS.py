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
# Implementing DFS
stack = [(root, 0)]
while stack:
    node, level = stack.pop()
    print("  " * level + node["value"])  # Print node with indentation based on level
    for child in reversed(node["children"]):  # Reverse to maintain order
        stack.append((child, level + 1))
