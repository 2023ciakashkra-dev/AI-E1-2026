from collections import deque

# Take number of edges
n = int(input("Enter number of edges: "))

graph = {}

print("Enter edges (node1 node2):")
for _ in range(n):
    u, v = input().split()
    
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
        
    graph[u].append(v)
    graph[v].append(u)   # remove this line if graph is directed

start = input("Enter starting node: ")

# BFS
visited = set()
queue = deque([start])

print("BFS Traversal:")

while queue:
    node = queue.popleft()
    
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)