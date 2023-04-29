import queue

def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    q = queue.Queue()
    for node in graph:
        if in_degree[node] == 0:
            q.put(node)
    
    result = []
    while not q.empty():
        node = q.get()
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.put(neighbor)
    
    return result

graph = {
    'A': ['B'],
    'B': ['D', 'E'],
    'C': ['E'],
    'D': [],
    'E': []
}

print(topological_sort(graph))
