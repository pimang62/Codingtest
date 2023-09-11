from collections import deque

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(i, j, num):
    global visited
    q = deque([(i, j)])
    visited[i][j] = 1

    dx = [0, 1, 0, -1]
    dy = [1, 0 , -1, 0]
    
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] == num:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1

    return cnt

visited = [[0]*n for _ in range(n)]

block, maxval = 0, 0
for i in range(n):
    for j in range(n):       
        if visited[i][j] == 0:
            num = graph[i][j]   # 1
            cnt = bfs(i, j, num)
            if cnt >= 4:
                block += 1  # 전체 블럭 개수
            maxval = max(maxval, cnt)

print(block, maxval, end=' ')