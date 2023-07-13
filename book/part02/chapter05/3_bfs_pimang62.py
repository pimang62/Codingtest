'''
[음료수 얼려 먹기]
n by m의 얼음 틀, 구멍이 뚫린 부분은 0, 칸막이가 존재하는 부분은 1
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결
얼음 틀 모양이 주어졌을 때 생성되는 총 아이스크림의 개수는?

입력)
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, *input())))

'''
from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


icecream = 0
def bfs(i, j):
    
    global graph, icecream

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque([(i, j)])
    graph[i][j] = 1     # 방문 처리
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 1
    
    # q가 다 빠지면
    icecream += 1
    return

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(i, j)

print(icecream)

'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
>>> 8
'''