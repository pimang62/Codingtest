from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [ list(map(int,input().strip())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<N and 0<=ny<M: # 범위 안에 있으면
                if board[nx][ny]!=0 and board[nx][ny]==1: # 괴물이 아니고 방문하지 않았으면
                    board[nx][ny] = board[x][y]+1
                    queue.append((nx,ny))

    return board[-1][-1]

print(BFS(0,0))