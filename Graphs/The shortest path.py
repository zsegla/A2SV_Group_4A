# https://www.eolymp.com/en/contests/16924/problems/175327



from collections import deque

def shortest_path(n, m, a, b, edges):
   
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([a])
    
    visited = [False] * (n + 1)
    visited[a] = True

    parent = [-1] * (n + 1)
    parent[a] = -1

    distance = [-1] * (n + 1)
    distance[a] = 0

    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                parent[u] = v
                distance[u] = distance[v] + 1
                queue.append(u)
                if u == b:
                    break

    if not visited[b]:
        print(-1)
        return

    path = []
    while b != -1:
        path.append(b)
        b = parent[b]
    path.reverse()
    
    print(len(path) - 1)
    print(*path)

n, m = map(int, input().split())
a, b = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

shortest_path(n, m, a, b, edges)
