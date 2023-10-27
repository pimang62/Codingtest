'''
[연구소]
바이러스의 확산을 막기 위해 벽을 세우려 함

n by m, 빈 칸 and 벽
일부 칸 바이러스, 상하좌우 퍼저나감
새로 세울 수 있는 벽은 3개, 꼭 3개
0: 빈 칸, 1: 벽, 2: 바이러스

바이러스가 퍼질 수 없는 곳을 안전 영역
안전 영역의 최댓값?
'''
from copy import deepcopy
from collections import deque

n, m = map(int, input().split())

graph = []  # 벽 세우기 전 그래프
virus = []  # 바이러스 좌표 : [(0, 0), (1, 5)]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            virus.append((i, j))
    graph.append(row)

dx = [0, 1, 0, -1]  # 동 남 서 북
dy = [1, 0, -1, 0]

def bfs(board):
    visited = [[0]*m for _ in range(n)]
    
    q = deque(virus)
    visited[virus[0][0]][virus[0][1]] = 1
    
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and board[nx][ny] == 0: 
                    visited[nx][ny] = 1
                    board[nx][ny] = 2  # 해줘야 함!
                    q.append((nx, ny))
    
    res = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                res += 1
    return res

cnt = 0
ans = 0
def backtrack(cnt):
    global ans
    if cnt == 3:
        board = deepcopy(graph)
        ans = max(ans, bfs(board))
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 :
                graph[i][j] = 1
                cnt += 1
                backtrack(cnt)
                graph[i][j] = 0
                cnt -= 1

backtrack(0)
print(ans)