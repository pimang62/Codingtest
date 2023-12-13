'''
[빙산] pypy3
일년마다 해당 칸에 동서남북으로 붙어있는 0의 개수만큼 줄어듦
단, 0보다 더 줄어들지는 않음

한 덩어리가 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)?
다 녹을 때까지 분리되지 않으면 0을 출력

def dfs() -> cnt:
- 아이스크림 덩어리 개수 확인해오기
- for문에서 받은 visited 배열로 갱신

def melting():
- 그래프 내 0이 아닌 모든 지점 탐색: q에 넣고
- 상하좌우 확인해서 graph 변형해야 함
- 전부 깎은 graph 반환

time = 0  # 시간
while True:
    if dfs() > 1:  # 두 덩어리로 나뉘면
        print(time)
        break
    if dfs() == 0:  # 덩어리 없으면
        print(0)
        break

'''
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]  # 동 남 서 북
dy = [1, 0, -1, 0]

def in_range(a, b):
    if 0 <= a < n and 0 <= b < m:
        return True
    return False

def check(candidate):
    visited = [[0]*m for _ in range(n)]
    
    def dfs(x, y):
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if not in_range(nx, ny):
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] != 0:
                visited[nx][ny] = 1
                dfs(nx, ny)
        return
    
    cnt = 0  # 덩어리 개수
    for (x, y) in candidate:
        if not visited[x][y]:
            visited[x][y] = 1
            dfs(x, y)
            cnt += 1

    return cnt

def melting(graph, candidate):
    tmp = candidate
    board = deepcopy(graph)
    q = deque(candidate)
    while q:
        x, y = q.popleft()
        zeros = 0  # 4방향 확인
        for k in range(4):
            tx, ty = x+dx[k], y+dy[k]
            if not in_range(tx, ty):
                continue
            if graph[tx][ty] == 0:
                zeros += 1
        if zeros > 0:
            if (graph[x][y] - zeros) > 0:
                board[x][y] -= zeros  # 갱신은 board에
            else:
                board[x][y] = 0
                tmp.remove((x, y))
    return board, tmp  # candidate

candidate = []  # initial
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            candidate.append((i, j))

time = 0  # 시간
while True:
    answer = check(candidate)  # 덩어리 개수
    if answer == 1:  # 한 덩어리면
        graph, candidate = melting(graph, candidate)
        time += 1
    else:
        break

if answer > 1:
    print(time)
else:
    print(0)
    