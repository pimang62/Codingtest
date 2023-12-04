from copy import deepcopy

n, h = map(int, input().split())  # 격자 크기, 최소한의 간식
graph = [list(map(int, input().split())) for _ in range(n)]

sx, sy = n//2, n//2

dx = [-1, 0, 1, 0]  # 북동남서
dy = [0, 1, 0, -1]

def in_range(i, j):
    if 0 <= i < n and 0 <= j < n:
        return True
    return False

def twice(i, j, board):
    x, y = i, j
    board[x][y] *= 2
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if in_range(nx, ny):
            board[nx][ny] *= 2
    return board

def move(board):
    x, y = sx, sy
    cnt = 0  # 들린 부스의 수
    snack = 0  # 먹은 과자의 양
    for d in range(1, n-1, 2):  # 1, 3, 5, ... n-2
        for k in range(4):
            if k < 2:  # 0, 1: 북, 동
                for _ in range(d):
                    nx, ny = x+dx[k], y+dy[k]
                    snack += board[nx][ny]
                    cnt += 1
                    if snack >= h:
                        return cnt  # not break!!
                    x, y = nx, ny

            elif k >= 2:  # 2, 3: 남, 서
                for _ in range(d+1):
                    nx, ny = x+dx[k], y+dy[k]
                    snack += board[nx][ny]
                    cnt += 1
                    if snack >= h:
                        return cnt
                    x, y = nx, ny

    for _ in range(n-1):
        nx, ny = x+dx[0], y+dy[0]
        snack += board[nx][ny]
        cnt += 1
        if snack >= h:
            return cnt
        x, y = nx, ny
    
    return None

ans = 1e9  # 최솟값
for i in range(n):
    for j in range(n):
        board = deepcopy(graph)
        board = twice(i, j, board)
        if move(board) != None:
            ans = min(ans, move(board))

print(ans if ans < 1e9 else "HUNGRY")