'''
[미로 탐색]
n by m 크기의 미로가 있다.
(1, 1)에서 출발하여 (n, m)의 위치로 이동할 때 최소의 칸 수!
시작 위치와 도착 위치를 포함한다.

입력)
n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(n):
    row = input()
    graph[n].append([int(r) for r in row])

print(graph)
'''
from collections import deque 

n, m = map(int, input().split())

graph = []
for _ in range(n):
    row = input()
    graph.append([int(r) for r in row])

# 0-indexed
x, y = 0, 0

#     e, s, w,  n
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


visited = [ [0]*m for _ in range(n) ]

q = deque([(x, y)])

def bfs(x, y):
    
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m :
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1 # 방문 처리
                    graph[nx][ny] += graph[x][y]

    return graph[n-1][m-1]

print(bfs(x, y))

    
    