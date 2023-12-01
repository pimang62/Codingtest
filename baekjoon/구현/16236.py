'''
[아기 상어]
n by n 물고기 m, 아기 상어 1
가장 처음 아기 상어 크기 2
자신보다 크기가 "작은" 물고기만 먹음

- 더 이상 먹을 공간이 없다면 엄마 상어에게
- 먹을 수 있는 물고기가 1마리면 그걸 먹음
- 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운
  - 거리는 지나야 하는 칸의 개수의 최솟값
  - 가까운 물고기가 많다면 가장 위, 왼쪽 순으로

이동은 1초, 먹는데 걸리는 시간은 없음
물고기를 먹으면, 그 칸은 빈칸이 됨

자신의 크기와 "같은 수의 물고기"를 먹을 때마다 크기가 1 증가
몇 초동안 잡아먹을 수 있는지?

4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4

- 참고: https://hae-sooo97.tistory.com/53
'''
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

sx, sy = 0, 0  # shark i, j: 2, 2
size = 2  # 초기 shark 사이즈
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            sx, sy = i, j

def in_range(a, b):
    if 0 <= a < n and 0 <= b < n:
        return True
    return False

dx = [-1, 0, 1, 0]  # 북서남동
dy = [0, -1, 0, 1]

def bfs(x, y):  # 상어의 현 지점으로부터 거리 기록
    q = deque([(x, y)])
    visited = [[-1]*n for _ in range(n)]
    visited[x][y] = 0
    
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not in_range(nx, ny):
                continue
            if visited[nx][ny] == -1 and graph[nx][ny] <= size:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    # [[3, 2, 3], 
    #  [2, 1, 2], 
    #  [1, 0, 1]]
    return visited

def find(visited):  # 0 < graph[i][j] < size인 곳 찾기
    x, y = 0, 0
    mini = 1e9  # 가장 최단 거리 찾기
    for i in range(n):
        for j in range(n):
            if visited[i][j] != -1 and 0 < graph[i][j] < size:  # 작은 물고기만 먹음!
                if visited[i][j] < mini:
                    x, y = i, j  # 이동할 좌표 기록
                    mini = visited[i][j]
                    #break : 모든 물고기 확인해야 함!
    if mini < 1e9:
        return x, y, mini
    return None  # if mini == 1e9

answer = 0  # 시간 기록
cnt = 0  # 먹은 물고기 수
while True:
    check = find(bfs(sx, sy))
    if check == None:  # 엄마 상어!
        break  # print(answer)
    else:
        nx, ny, dist = check
        answer += dist
        graph[nx][ny] = 0  # 먹음
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0  # 다시 초기화!!
        sx, sy = nx, ny
        
print(answer)

        
    
    