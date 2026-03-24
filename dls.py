def dls(graph, node, goal, depth, visited):
    if node == goal:
        print(f"\n✅ Goal node {goal} found")
        return True
    
    if depth <= 0:
        return False

    visited.add(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if dls(graph, neighbor, goal, depth - 1, visited):
                return True

    return False


# Input section (same style as your code)
n = int(input("Enter number of nodes: "))

graph = {}

print("Enter adjacency list (space-separated neighbors):")
for i in range(n):
    neighbors = list(map(int, input(f"Node {i}: ").split()))
    graph[i] = neighbors

start = int(input("Enter start node: "))
goal = int(input("Enter goal node: "))
depth_limit = int(input("Enter depth limit: "))

visited = set()

print(f"\nSearching with depth limit {depth_limit}...")

if not dls(graph, start, goal, depth_limit, visited):
    print("\n❌ Goal node not found within depth limit")