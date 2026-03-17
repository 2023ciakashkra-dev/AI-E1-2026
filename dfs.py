def dfs(node, visited, graph):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs(neighbor, visited, graph)


# Input same as before
n = int(input("Enter number of edges: "))
graph = {}

print("Enter edges (node1 node2):")
for _ in range(n):
    u, v = input().split()
    
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

start = input("Enter starting node: ")

visited = set()

print("DFS Traversal:")
dfs(start, visited, graph)