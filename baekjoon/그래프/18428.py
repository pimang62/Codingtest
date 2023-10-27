'''
[감시 피하기]
n by n, 학생들은 감시에 들키지 않는 것이 목표
상하좌우 감시, 장애물이 있을 경우 못 봄
아무리 멀리 있더라도 계속 볼 수 있음

선생님: T, 학생: S, 장애물: O
3개의 장애물 설치해야 함!

감시를 피할 수 있다면 "YES", 아니면 "NO"
'''
from copy import deepcopy
from collections import deque

n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
graph = []
teacher = []
for i in range(n):
    row = list(map(str, input().split()))
    for j in range(n):
        if row[j] == 'T':
            teacher.append((i, j))
    graph.append(row)

ans = 0

def check(board):
    q = deque(teacher)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            while 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 'O':
                if board[nx][ny] == 'S':
                    return False
                nx += dx[k]
                ny += dy[k]
    
    return True

def backtracking(cnt):
    global ans
    if cnt == 3:
        board = deepcopy(graph)
        if check(board):
            ans += 1
        return
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                backtracking(cnt+1)
                graph[i][j] = 'X'

backtracking(0)  # cnt = 0
print("YES" if ans > 0 else "NO")