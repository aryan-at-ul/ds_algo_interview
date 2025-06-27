
from collections import deque

def bfs(graph, start_node):

    if start_node not in graph:
        return []
        
    visited = set()        
    queue = deque([start_node])
    traversal_order = []  

    visited.add(start_node)

    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node)


        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_order


def dfs_recursive(graph, start_node, visited=None, traversal_order=None):

    if visited is None:
        visited = set()
    if traversal_order is None:
        traversal_order = []

    if start_node not in graph or start_node in visited:
        return traversal_order

    visited.add(start_node)
    traversal_order.append(start_node)

    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, traversal_order)
            
    return traversal_order



graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


print("BFS Traversal starting from node 'A':")
print(bfs(graph, 'A'))


print("\nDFS Traversal starting from node 'A':")
print(dfs_recursive(graph, 'A'))




