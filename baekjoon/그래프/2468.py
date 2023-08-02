'''
[안전 영역]
높이 정보, 안전한 영역이 최대 몇 개?
일정 높이 이하의 모든 지점은 물에 잠김

물에 잠기지 않는 안전한 영역의 최대 개수?
높이는 1 이상 100 이하의 정수

입력)
n = int(input())    # 2 <= n <= 100
graph = []
maximum = 0
for _ in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[i] > maximum:
            maximum = row[i]
    graph.append(row)

'''
from collections import deque

def bfs(i, j, h):

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] > h:
                visited[nx][ny] = 1
                q.append((nx, ny))


n = int(input())    # 2 <= n <= 100
graph = []
maximum = 0
for _ in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] > maximum:
            maximum = row[j]
    graph.append(row)

result = 0
for h in range(maximum):
    cnt = 0
    visited = [ [0]*n for _ in range(n) ]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] > h:
                bfs(i, j, h)
                cnt += 1
    
    result = max(cnt, result)

print(result)