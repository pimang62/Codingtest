'''
[구슬 탈출 2]
빨간 구슬을 구멍을 통해 빼내는 게임
n by m, 중력 이용, 보드에는 구멍이 하나
파란 구슬이 구멍에 들어가면 안됨!
'.' 빈칸, '#' 벽, 'O' 구멍 'R' 빨간 'B' 파란

최소 몇 번?, 10번 이하로 움직일 수 없으면 -1!
좌우로 움직이다가 아래 방향으로 갈 수 있다면 떨어짐

'O'에서 시작 cnt마다 distance배열 만들기
'''
from collections import deque

n, m = map(int, input().split())
graph = [[s for s in input()] for _ in range(n)]

# os, oe = 0, 0  # 'O' 좌표 기록 : 필요 없을듯
rs, re = 0, 0  # 'R' 좌표 기록
bs, be = 0, 0  # 'B' 좌표 기록
for i in range(n):
    for j in range(m):
        # if graph[i][j] == 'O':
        #     os, oe = i, j
        if graph[i][j] == 'R':
            rs, re = i, j
        elif graph[i][j] == 'B':
            bs, be = i, j
            
# def in_range(a, b):
#     if 0 <= a < n and 0 <= b < m:
#         return True
#     return False

dx = [0, 1, 0, -1]  # 동남서북
dy = [1, 0, -1, 0]

def bfs():
    q = deque([(rs, re, bs, be, 0)])
    visited = []  # or set
    visited.append((rs, re, bs, be))
    
    flag = False  # 가능한지 여부
    cnt = 0  # 몇 번 이동?
    while q:
        rx, ry, bx, by, cnt = q.popleft()  # cnt: 총 시행 횟수
        if cnt > 10:
            break  # return -1
        if graph[rx][ry] == 'O':
            flag = True
            break  # return cnt
        for k in range(4):
            nrx, nry = rx, ry
            while True:
                nrx += dx[k]  # 일단 움직여봐야!
                nry += dy[k]
                # if not in_range(nrx, nry):  # 범퍼 있으니 '#' 확인하면 의미 없을듯
                #     continue
                if graph[nrx][nry] == '#':
                    nrx -= dx[k]  # 한 칸 back
                    nry -= dy[k] 
                    break
                if graph[nrx][nry] == 'O':
                    break

            nbx, nby = bx, by  # 독립 시행
            while True:
                nbx += dx[k]
                nby += dy[k]
                if graph[nbx][nby] == '#':
                    nbx -= dx[k]  # 한 칸 back
                    nby -= dy[k] 
                    break
                if graph[nbx][nby] == 'O':
                    break
            
            if graph[nbx][nby] == 'O':
                continue  # 이 방향으로 이동하는 경우의 수 무시
            if (nrx, nry) == (nbx, nby):  # 같아지면
                if (abs(nrx - rx) + abs(nry - ry)) > (abs (nbx - bx) + abs(nby - by)):  # A 이동거리가 B보다 멀면
                    nrx -= dx[k]  # A가 뒤에 있었음
                    nry -= dy[k]
                else:
                    nbx -= dx[k]
                    nby -= dy[k]
            if (nrx, nry, nbx, nby) not in visited:  # 방문하지 않아야
                q.append((nrx, nry, nbx, nby, cnt+1))
                visited.append((nrx, nry, nbx, nby))  # visited는 cnt 들어가면 안 됨

    return cnt if flag else -1

print(bfs())

 
'''
def bfs():
    q = deque([(1, os, oe)])  # time, os, oe
    dist = [[-1]*m for _ in range(n)]
    dist[os][oe] = 0  # initialize
    
    cnt = 1  # 기록
    while q:
        if cnt > 10:
            return -1
        cnt, x, y = q.popleft()
        for k in range(4):
            flag = False  # 맨 마지막 지점
            tx, ty = x+dx[k], y+dy[k]
            while in_range(tx, ty) and dist[tx][ty] == -1 and graph[tx][ty] != '#':
                flag = True
                if graph[tx][ty] == 'R':
                    return cnt
                dist[tx][ty] = cnt
                
                nx, ny = tx, ty  # 그 다음 못갈 경우방지!
                if in_range(nx+dx[-1], ny+dy[-1]) and graph[nx+dx[-1]][ny+dy[-1]] == '.':
                    q.append((cnt+1, nx, ny))
                
                tx += dx[k]
                ty += dy[k]
            
            if flag:
                q.append((cnt+1, nx, ny))

answer = bfs()
print(answer if answer != None else -1)
'''

"""
5 4
####
#RB#
####
#O.#
####
-----------
10 10
##########
#RB....#.#
#..#.....#
#........#
#.O......#
#...#....#
#........#
#........#
#.......##
##########
ans: 10
"""