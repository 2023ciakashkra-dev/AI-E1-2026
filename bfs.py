from collections import deque

def bfs(tree, root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        visited.append(node)

        for child in tree[node]:
            queue.append(child)

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
print("BFS Traversal:", bfs(tree, 'A'))     

                