'''
[봄버맨]
크기가 r by c, 비어있거나 폭탄
폭탄은 3초 후 폭발 -> 인접한 네 칸까지 빈칸(폭탄 있어도)

1. 폭탄 설치
2. 1초 동안은 아무것도 하지 않음
3. 1초 뒤 모든 칸에 폭탄 설치
4. 3초 전에 설치된 폭탄 모두 폭발
    - 3, 4 반복

6 7 3
.......
...O...
....O..
.......
OO.....
OO.....

OOO.OOO
OO...OO
OOO...O
..OO.OO
...OOOO
...OOOO
'''
from collections import deque
from copy import deepcopy

r, c, n = map(int, input().split())
graph = [list(input()) for _ in range(r)]

dx = [0, 1, 0, -1]  # 동남서북
dy = [1, 0, -1, 0]

def in_range(a, b):
    return 0 <= a < r and 0 <= b < c

def bomb(board, graph):
    q = deque()
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                q.append((i, j))

    while q:
        x, y = q.popleft()
        graph[x][y] = '.'
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if in_range(nx, ny):
                graph[nx][ny] = '.'

    return graph

def check(time):
    return time < n

time = 0
def main():
    global time, graph

    time += 1  # 첫 1초
    if not check(time):
        return graph

    board = deepcopy(graph)
    while True: 
        for i in range(r):
            for j in range(c):
                graph[i][j] = 'O'
        time += 1
        if not check(time):
            return graph
        
        graph = bomb(board, graph)
        time += 1
        if not check(time):
            return graph
        
        board = deepcopy(graph)  # 이전 graph 저장

for row in main():
    print(''.join(row))