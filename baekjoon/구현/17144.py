'''
[미세먼지 안녕!]
공기청정기는 항상 1번 열, 크기는 두 행

1초동안
1. 미세먼지 확산, 미세먼지 있는 칸에서 동시에
    - (r-1, c-1)에 있는 인접한 상하좌우 네 방향
    - 인접 방향에 공기청청기가 있거나, 칸이 없으면 확산x
    - 양은 A_rc//5
    - (r-1, c-1)에 남은 양은 A_rc - A_rc//5*확산 '방향' 개수
    - 0 30 7  6  15  11  독립적으로 //, 갈수있는 횟수, 더하기
      0 10 0  -  10   7  
      0 0 20      6  12 
2. 공기청정기 작동
    - 바람이 나옴
    - 위쪽 바람은 반시계, 아래쪽 바람은 시계
    - 바람 방향대로 미세먼지 한 칸씩 이동
    - 공기청정기로 들어간 미세먼지는 모두 정화
'''
from collections import deque
from copy import deepcopy

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

cleaner = []  # up(반시계), down(시계)
for i in range(r):
    if graph[i][0] == -1:
        cleaner.append((i, 0))

dx = [0, 1, 0, -1]  # 동남서북
dy = [1, 0, -1, 0]

# 공기청청기
upx, upy = cleaner[0]
dwx, dwy = cleaner[1]

def in_range(a, b):
    if 0 <= a < r and 0 <= b < c:
        return True
    return False

def diffuse(q: deque, board: list):
    d = [[0]*c for _ in range(r)]
    while q:
        x, y = q.popleft()
        orig = board[x][y]  # 원래 값
        cnt = 0  # 가능한 칸의 개수
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if not in_range(nx, ny):
                continue
            if board[nx][ny] == -1:
                continue
            else:
                d[nx][ny] += (orig//5)
                cnt += 1
        d[x][y] += orig - (orig//5)*cnt
    
    d[upx][upy] = -1
    d[dwx][dwy] = -1
    
    return d

def rotate(board: list):
    d = [[0]*c for _ in range(r)]
    
    # 반시계
    puz1 = board[0][0]
    # 0행 왼쪽: 0열 제외
    for j in range(1, c):
        d[0][j-1] = board[0][j]
    # c-1열 위로
    for i in range(1, upx+1):
        d[i-1][-1] = board[i][-1]
    # upx행 오른쪽: upy 제외
    for j in range(1, c-1):  # 1 ~ c-2 
        d[upx][j+1] = board[upx][j]
    # upy열 아래로: 
    for i in range(1, upx-1):  # 1 ~ upx-2
        d[i+1][0] = board[i][0]
    # 마무리
    d[1][0] = puz1
    d[upx][upy] = -1  
    
    # 시계  
    puz2 = board[-1][-1]
    # -1열 아래로
    for i in range(dwx, r-1):  # dwx ~ r-2
        d[i+1][-1] = board[i][-1]
    # -1행 왼쪽: -1행 제외
    for j in range(1, c-1):
        d[-1][j-1] = board[-1][j]
    # 0열 위로
    for i in range(dwx+2, r):  # dwx+2 ~ r-1
        d[i-1][0] = board[i][0]
    # dwx행 오른쪽
    for j in range(1, c-1):  # 1 ~ c-2
        d[dwx][j+1] = board[dwx][j]
    # 마무리
    d[-1][c-2] = puz2
    d[dwx][dwy] = -1
    
    # 내부 채우기
    for i in range(1, upx):
        for j in range(1, c-1):
            d[i][j] = board[i][j]
    
    for i in range(dwx+1, r-1):
        for j in range(1, c-1):
            d[i][j] = board[i][j]
    
    return d
    
board = deepcopy(graph)  # initialize
# q = deque()  # 좌표 담기
# for i in range(r):
#     for j in range(c):
#         if graph[i][j] > 0:
#             q.append((i, j))
            
for _ in range(t):
    q = deque()  # 좌표 담기
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                q.append((i, j))
    
    board = diffuse(q, board)
    board = rotate(board)
    print(board)

print(sum(map(sum, board))+2)  # -1*2개

'''
[[0, 0, 0, 0, 0, 0, 1, 8], 
 [0, 0, 1, 0, 3, 0, 5, 6], 
 [0, 2, 1, 1, 0, 4, 6, 5], 
 [0, 5, 2, 0, 0, 2, 12, 0], 
 [0, 1, 1, 0, 5, 10, 13, 8], 
 [0, 1, 9, 4, 3, 5, 12, 0], 
 [0, 8, 17, 8, 3, 4, 8, 4]]
 
[[0, 0, 0, 0, 0, 1, 8, 6], 
 [0, 0, 0, 0, 0, 0, 0, 5], 
 [-1, 0, 2, 1, 1, 0, 4, 6], 
 [-1, 0, 5, 2, 0, 0, 2, 12], 
 [0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 8], 
 [8, 17, 8, 3, 4, 8, 4, 0]]
 
[[0, 0, 0, 0, 0, 1, 8, 6], 
 [0, 0, 1, 0, 3, 0, 5, 5], 
 [-1, 0, 2, 1, 1, 0, 4, 6], 
 [-1, 0, 5, 2, 0, 0, 2, 12], 
 [0, 1, 1, 0, 5, 10, 13, 0], 
 [0, 1, 9, 4, 3, 5, 12, 8], 
 [8, 17, 8, 3, 4, 8, 4, 0]]

8 8 2
3 0 0 0 0 0 0 0
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
>>> 191

[[3, 0, 0, 0, 0, 0, 0, 1], 
 [0, 0, 0, 0, 0, 0, 1, 7], 
 [0, 0, 1, 0, 3, 0, 5, 6], 
 [-1, 2, 1, 1, 0, 4, 6, 5], 
 [-1, 5, 2, 0, 0, 2, 12, 0], 
 [0, 1, 1, 0, 5, 10, 13, 8], 
 [0, 1, 9, 4, 3, 5, 12, 0], 
 [0, 8, 17, 8, 3, 4, 8, 4]]
 
[[0, 0, 0, 0, 0, 0, 1, 7], 
 [3, 0, 0, 0, 0, 0, 1, 6], 
 [0, 0, 1, 0, 3, 0, 5, 5], 
 [-1, 0, 2, 1, 1, 0, 4, 6], 
 [-1, 0, 5, 2, 0, 0, 2, 12], 
 [0, 1, 1, 0, 5, 10, 13, 0], 
 [0, 1, 9, 4, 3, 5, 12, 8], 
 [8, 17, 8, 3, 4, 8, 4, 0]]
 
[[0, 0, 0, 0, 0, 0, 2, 6], 
 [3, 0, 0, 0, 0, 0, 3, 5], 
 [0, 0, 1, 0, 3, 1, 2, 5], 
 [-1, 0, 3, 1, 1, 0, 6, 6], 
 [-1, 1, 1, 3, 1, 2, 6, 7], 
 [0, 1, 3, 1, 3, 6, 9, 5], 
 [1, 5, 6, 5, 5, 6, 8, 7], 
 [9, 10, 9, 4, 5, 6, 7, 1]]
 
[[0, 0, 0, 0, 0, 2, 6, 5], 
 [0, 0, 0, 0, 0, 0, 3, 5], 
 [-(bug!), 0, 1, 0, 3, 1, 2, 6], 
 [-1, 0, 0, 3, 1, 1, 0, 6], 
 [-1, 0, 1, 1, 3, 1, 2, 6], 
 [1, 1, 3, 1, 3, 6, 9, 7], 
 [9, 5, 6, 5, 5, 6, 8, 5], 
 [10, 9, 4, 5, 6, 7, 1, 7]]
 
 d를 board로 변경..
'''