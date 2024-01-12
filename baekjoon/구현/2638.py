'''
[치즈]
각 정사각형의 4변 중 2변 이상이 공기와 닿으면 사라짐
주어진 치즈가 모두 녹아 없어지는데 걸리는 시간?
'''
from collections import deque

n, m = map(int, input().split())
graph =[list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]  # 동남서북
dy = [1, 0, -1, 0]

def in_range(a, b):
    if 0 <= a < n and 0 <= b < m:
        return True
    return False

def bfs():
    global graph
    q = deque([(0, 0)])  # 시작점 (0, 0)
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1  # initialize
    
    cnt = 0  # 녹을 치즈 개수
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if not in_range(nx, ny):
                continue
            if graph[nx][ny] == 1:
                visited[nx][ny] += 1
                if visited[nx][ny] >= 2:  # 2개 이상 체크
                    cnt += 1
                    graph[nx][ny] = 0  # 녹은 상태 기록
            # not visited : 무한 루프 방지!
            if not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))
    return cnt

time = 0  # 모두 녹을 때까지 걸린 시간
while True:
    melt = bfs()
    if melt == 0:
        break
    time += 1

print(time)

'''
[[0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 2, 2, 0, 0, 0, 0], 
 [0, 0, 0, 1, 1, 0, 2, 2, 0], 
 [0, 0, 2, 1, 1, 1, 1, 2, 0], 
 [0, 0, 1, 1, 1, 1, 1, 0, 0], 
 [0, 0, 2, 2, 0, 2, 2, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
'''