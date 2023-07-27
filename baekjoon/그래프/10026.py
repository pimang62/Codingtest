'''
[적록색약]
적록색약인 사람 / 아닌 사람 구역의 수?

'''
from collections import deque

n = int(input())

graph = []
for _ in range(n):
    graph.append([s for s in input()])

yes_visited = [ [0]*len(graph[0]) for _ in range(n) ]
not_visited = [ [0]*len(graph[0]) for _ in range(n) ]

def yes_bfs(i, j, visited,  rgb):

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    visited[i][j] = 1
    q = deque([(i, j)])    
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= len(graph[0]) or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] == rgb:
                visited[nx][ny] = 1 # 방문 처리만 해주고 나옴
                q.append((nx, ny))
    return 1

def not_bfs(i, j, visited,  rgb):

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    visited[i][j] = 1
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= len(graph[0]) or ny < 0 or ny >= n:
                continue
            if rgb == 'R' or rgb == 'G' :
                if visited[nx][ny] == 0 and (graph[nx][ny] == 'R' or graph[nx][ny] == 'G') :
                    visited[nx][ny] = 1 # 방문 처리만 해주고 나옴
                    q.append((nx, ny))
            else:
                if visited[nx][ny] == 0 and graph[nx][ny] == rgb:
                    visited[nx][ny] = 1 # 방문 처리만 해주고 나옴
                    q.append((nx, ny))
    return 1

yes_cnt, not_cnt = 0, 0

for i in range(n):
    for j in range(len(graph[0])):
        # 방문하지 않았다면 움직임
        if yes_visited[i][j] == 0:
            rgb = graph[i][j]
            yes_cnt += yes_bfs(i, j, yes_visited, rgb)
        if not_visited[i][j] == 0:
            rgb = graph[i][j]
            not_cnt += not_bfs(i, j, not_visited, rgb)
    
print(yes_cnt, not_cnt)
