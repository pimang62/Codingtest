'''
1~3 숫자, n by n
상하좌우로 인접, 같은 숫자 같은 마을
[1, 2, 3] 부족의 사람 수?
'''
# bfs
from collections import deque

n = int(input())
graph = [ list(map(int, input().split())) for _ in range(n) ]

visited = [ [0]*n for _ in range(n) ]
people = [0, 0, 0]  # 1 2 3

dx = [0, 1, 0, -1]  # 동 남 서 북
dy = [1, 0, -1, 0]

def bfs(i, j, typ):
    
    q = deque([(i, j)])
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if not visited[nx][ny] and graph[nx][ny] == typ:
                visited[nx][ny] = 1
                q.append((nx, ny))

for i in range(n):
    for j in range(n):
        if not visited[i][j] :
            typ = graph[i][j]
            bfs(i, j, typ)
            people[typ-1] += 1

print(*people)
