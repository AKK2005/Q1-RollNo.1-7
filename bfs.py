from collections import deque, defaultdict
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}
def kahn_topological_sort(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    queue = deque(sorted([u for u in graph if in_degree[u] == 0]))
    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in sorted(graph[node]):  
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

        queue = deque(sorted(queue))
    return topo_order

def dfs_topological_sort(graph):
    visited = set()
    stack = []
    def dfs(node):
        visited.add(node)
        for neighbor in sorted(graph[node]):  
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)
    for node in sorted(graph):  
        if node not in visited:
            dfs(node)
    stack.reverse()
    return stack
kahn_result = kahn_topological_sort(graph)
dfs_result = dfs_topological_sort(graph)
print("Topological Sort using Kahn's Algorithm:")
print(" -> ".join(kahn_result))
print("\nTopological Sort using DFS:")
print(" -> ".join(dfs_result))
with open("topological_sort_results.txt", "w") as file:
    file.write("Topological Sorting Results\n")
    file.write("---------------------------\n")
    file.write("Kahn's Algorithm: " + " -> ".join(kahn_result) + "\n")
    file.write("DFS-Based Algorithm: " + " -> ".join(dfs_result) + "\n")
