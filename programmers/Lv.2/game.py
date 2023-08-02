from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [ [0]*m for _ in range(n) ]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    q = deque([(0, 0)])
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                visited[nx][ny] = 1
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))

    return maps

print(solution(maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
