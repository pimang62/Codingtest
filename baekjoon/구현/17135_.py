from itertools import combinations

n, m, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

def move(graph):
    new_graph = [[0]*m for _ in range(n)]
    for j in range(m):
        if graph[-1][j] == 1:
            for i in range(n):
                new_graph[i][j] = graph[i][j]
        else:  # == 0
            for i in range(n-1):
                new_graph[i+1][j] = graph[i][j]
    return new_graph

answer = 0
for _ in range(n):
    for combi in combinations(range(n), 3):
        for idx in combi:
            
                
        graph = move(graph)
    