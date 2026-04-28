def dls(node, depth, limit, tree, levels):
    if node is None:
        return
    
    # Ensure list exists for this depth
    if depth not in levels:
        levels[depth] = []
    
    levels[depth].append(node)
    
    # Stop if depth limit reached
    if depth == limit:
        return
    
    for child in tree.get(node, []):
        dls(child, depth + 1, limit, tree, levels)


# Driver code
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7]
}

limit = 2
levels = {}

dls(1, 0, limit, tree, levels)

# Display output
for depth in range(limit + 1):
    print(f"Depth {depth}: Visited Nodes {levels.get(depth, [])}") 