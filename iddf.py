def dls(node, depth, limit, tree, visited):
    if node is None:
        return
    
    visited.append(node)
    
    if depth == limit:
        return
    
    for child in tree.get(node, []):
        dls(child, depth + 1, limit, tree, visited)



def iddfs(tree, root, max_depth):
    for limit in range(1, max_depth + 1):
        visited = []
        dls(root, 0, limit, tree, visited)
        print(f"Depth Limit {limit}: Visited Nodes {visited}")



tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7]
}


iddfs(tree, 1, 2)