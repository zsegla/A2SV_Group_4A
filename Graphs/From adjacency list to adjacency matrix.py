# https://www.eolymp.com/en/contests/9060/problems/78604



n = int(input())

adjacency_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    edges = list(map(int, input().split()))[1:]
    for vertex in edges:
        adjacency_matrix[i][vertex - 1] = 1  

for row in adjacency_matrix:
    print(*row)
