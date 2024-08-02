from collections import deque

N, M, V = map(int, input().split())
graph = {}

# Build graph
for v in range(1, N + 1):
    graph[v] = []
for _ in range(M):
    start_v, end_v = map(int, input().split())
    graph[start_v].append(end_v)
    graph[end_v].append(start_v)

def dfs(graph, visited, start_v):
    curr_v = start_v
    if curr_v not in visited:
        visited.append(curr_v)

        for v in sorted(graph[curr_v]):
            dfs(graph, visited, v)

def bfs(graph, start_v):
    visited = []
    queue = deque([start_v])

    while queue:
        curr_v = queue.popleft()
        if curr_v not in visited:
            visited.append(curr_v)
            for v in sorted(graph[curr_v]):
                queue.append(v)

    return visited

# dfs
visited = []
dfs(graph, visited, V)
print(" ".join(map(str, visited)))

# bfs
visited = bfs(graph, V)
print(" ".join(map(str, visited)))
