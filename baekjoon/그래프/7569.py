'''
[토마토]
익은 토마토의 인접한 곳에 있는 익지 않은 토마토들은 익음
며칠이 지나면 다 익게 되는지? 최소 일수!
일부 칸에는 토마토가 들어있지 않을 수 있다

입력)
m, n, h = map(int, input().split())
graph = [ [ [] for _ in range(n) ] for _ in range(h) ]
visited = [ [ [] for _ in range(n) ] for _ in range(h) ]
for k in range(h):
    for j in range(n):
        graph[k][j] = list(map(int, input().split()))
        visited[k][j] = [0]*len(graph[k][j])

'''
from collections import deque
import sys

input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [ [ [] for _ in range(n) ] for _ in range(h) ]
visited = [ [ [] for _ in range(n) ] for _ in range(h) ]

data = []
for k in range(h):
    for i in range(n):
        graph[k][i] = list(map(int, input().split()))
        visited[k][i] = [0]*len(graph[k][i])
        for j in range(m):
            if graph[k][i][j] == 1:
                data.append((k, i, j))

'''
def bfs(data, visited, graph):

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dz = [-1, 1]

    q = deque(data)
    a, b, c = q[0]
    visited[a][b][c] = 1
    while q :
        z, x, y = q.popleft()
        for l in range(2):
            nz = z + dz[l]
            if nz < 0 or nz >= h:
                continue
            if visited[nz][x][y] == 0 and graph[nz][x][y] == 0:
                visited[nz][x][y] = 1
                graph[nz][x][y] = graph[z][x][y] + 1
                q.append((nz, x, y))
            
        for o in range(4):
            nx = x + dx[o]
            ny = y + dy[o]
            if nx < 0 or ny < 0 or ny >= n or nx >= m:
                continue
            if visited[z][nx][ny] == 0 and graph[z][nx][ny] == 0:
                visited[z][nx][ny] = 1
                graph[z][nx][ny] = graph[z][x][y] + 1
                q.append((z, nx, ny))
                
    return graph

print(bfs(data, visited, graph))
'''

def bfs(data, visited, graph):
    
    direction = [(1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0)]

    q = deque(data)
    while q :
        z, x, y = q.popleft() 
        visited[z][x][y] = 1
        for d in direction:
            nz = z + d[0]
            nx = x + d[1]
            ny = y + d[2]
            if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
                continue
            if visited[nz][nx][ny] == 0 and graph[nz][nx][ny] == 0:
                visited[nz][nx][ny] = 1
                graph[nz][nx][ny] = graph[z][x][y] + 1
                q.append((nz, nx, ny))
                
    return graph

result = bfs(data, visited, graph)
answer = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if result[k][i][j] == 0:
                print(-1)
                exit(0)
            else:
                answer = max(answer, result[k][i][j])

print(answer-1)
