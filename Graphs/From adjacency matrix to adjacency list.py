# https://www.eolymp.com/en/contests/9060/problems/78603



n = int(input())

adjacency_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    adjacency_matrix.append(row)

adjacency_list = []
for i in range(n):
    edges = []
    for j in range(n):
        if adjacency_matrix[i][j] == 1:
            edges.append(j + 1)  
    adjacency_list.append(edges)


for edges in adjacency_list:
    print(len(edges), *edges)
