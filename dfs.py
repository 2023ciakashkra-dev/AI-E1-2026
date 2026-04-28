def dfs(tree, node, visited=None):
    if visited is None:
        visited = []

    visited.append(node)

    for child in tree[node]:
        if child not in visited:
            dfs(tree, child, visited)

    return visited


# Example tree
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Execution
print("DFS Traversal:", dfs(tree, 'A'))
from collections import deque