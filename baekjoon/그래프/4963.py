'''
[섬의 개수]
섬(1)과 바다(0) 지도
섬의 개수?

입력)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1e9)

w, h = map(int, input().split())
while (a and b) != 0:
    print('a')

'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [0, 1, 0, -1, -1, -1, 1, 1]
dy = [1, 0, -1, 0, -1, 1, -1, 1]

def dfs(i, j):
    
    for k in range(8):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        if visited[nx][ny] == 0 and graph[nx][ny] == 1:
            visited[nx][ny] = 1
            dfs(nx, ny)
    return 

result = []

while True:
    graph = []  # graph
    visited = []
    data = []   # 1
    w, h = map(int, input().split())
    if (w and h) == 0:
        break
    for i in range(h):
        row = list(map(int, input().split()))
        for j in range(w):
            if row[j] == 1:
                data.append((i, j))
        graph.append(row)
        visited.append([0]*w)
    
    cnt = 0 
    for d in data:
        i, j = d
        if visited[i][j] == 0:
            dfs(i, j)
            cnt += 1

    print(cnt)