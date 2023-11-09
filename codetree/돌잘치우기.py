from collections import deque
# from itertools import combinations
from copy import deepcopy

n, k, m = map(int, input().split())

ones = []
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        if row[j] == 1:
            ones.append((i, j))
    graph.append(row)

starts = []
for _ in range(k):
    a, b = map(int, input().split())
    starts.append((a-1, b-1))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(board):
    q = deque(starts)
    visited = [[0]*n for _ in range(n)]

    answer = 1  # board max
    # if board[q[0][0]][q[0][1]] == 0:  # 시작 지점에 모두 돌임
    #     answer += 1
    
    visited[q[0][0]][q[0][1]] = 1  # 방문 처리!!
    
    while q:
        x, y = q.popleft()
        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = 1
                answer += 1
                q.append((nx, ny))

    return answer

result = 0  # 최종 max값
def dfs(cnt, idx):
    global result
    # 해줘야 하는 작업이 먼저 와야!
    if cnt == m:
        board = deepcopy(graph)
        result = max(result, bfs(board))
        return 
    # 종료 조건 넣어주기(idx not in range)
    if idx >= len(ones):
            return
    i, j = ones[idx]
    graph[i][j] = 0
    dfs(cnt+1, idx+1)
    graph[i][j] = 1
    dfs(cnt, idx+1)  # 첫 출발 idx를 계속 넘겨줌

dfs(0, 0)  # cnt, idx(뽑을 ones의 index)

print(result)