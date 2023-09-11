import sys
sys.setrecursionlimit(10000)  # 런타임 에러!!

from collections import deque

n, m = map(int, input().split())

graph = []
max_val = -1    
for _ in range(n):
    row = list(map(int, input().split()))
    if max(row) > max_val:
        max_val = max(row)  # 7
    graph.append(row)


def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        x, y = q.popleft()
        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] > k:
                visited[nx][ny] = 1
                q.append((nx, ny))
            
    return 1

"""
def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return 0
    if visited[i][j] == 0 and graph[i][j] > k:
        visited[i][j] = 1
        dfs(i, j+1)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i-1, j)
        return 1
    return 0
"""

shelter = 0
k_val = max_val
for k in range(1, max_val):  # 7 제외
    visited = [[0]*m for _ in range(n)]
    icecream = 0     # icecream 덩어리
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and graph[i][j] > k:
                icecream += bfs(i, j)
    
    if shelter < icecream:
        shelter = icecream
        k_val = k

print(k_val, shelter, end = ' ')