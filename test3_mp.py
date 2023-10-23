import collections as c

graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1],
    3: [0],
    4: [2]
}

def bfs(graph, root):
    visited = set()
    queue = c.deque([root])

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)

    return visited

result = bfs(graph, 0)
print(result)
