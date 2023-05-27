# https://www.eolymp.com/en/contests/9060/problems/78613



n, m = map(int, input().split()) 
edges = [list(map(int, input().split())) for _ in range(m)]  

degree = {v: 0 for v in range(1, n+1)}

for u, v in edges:
    degree[u] += 1
    degree[v] += 1
is_regular = all(deg == degree[1] for deg in degree.values())

if is_regular:
    print("YES")
else:
    print("NO")
