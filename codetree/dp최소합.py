n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n-1, -1, -1):
        if i == 0 and j == n-1:
            continue
        from_above = graph[i-1][j] if i-1 >= 0 else 1e9
        from_right = graph[i][j+1] if j+1 < n else 1e9
        graph[i][j] += min(from_above, from_right)

print(graph[n-1][0])