# https://www.eolymp.com/en/contests/9060/problems/78602



def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def print_adjacent_vertices(graph, u):
    adjacent_vertices = graph[u]
    print(' '.join(map(str, adjacent_vertices)))

n = int(input())
k = int(input())

# Initialize the graph as an empty dictionary
graph = {v: [] for v in range(1, n+1)}

for _ in range(k):
    operation = input().split()
    op_type = int(operation[0])

    if op_type == 1:
        u, v = map(int, operation[1:])
        add_edge(graph, u, v)
    elif op_type == 2:
        u = int(operation[1])
        print_adjacent_vertices(graph, u)
