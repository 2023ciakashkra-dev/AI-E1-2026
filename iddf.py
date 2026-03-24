def dls(graph, node, goal, depth, visited):
    if node == goal:
        return True
    
    if depth <= 0:
        return False

    visited.add(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if dls(graph, neighbor, goal, depth - 1, visited):
                return True

    return False


def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        print(f"Searching at depth {depth}...")

        if dls(graph, start, goal, depth, visited):
            print(f"\n✅ Goal node {goal} found at depth {depth}")
            return

    print("\n Goal node not found")



n = int(input("Enter number of nodes: "))

graph = {}

print("Enter adjacency list (space-separated neighbors):")
for i in range(n):
    neighbors = list(map(int, input(f"Node {i}: ").split()))
    graph[i] = neighbors

start = int(input("Enter start node: "))
goal = int(input("Enter goal node: "))
max_depth = int(input("Enter maximum depth limit: "))

iddfs(graph, start, goal, max_depth)