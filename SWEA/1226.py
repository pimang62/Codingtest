'''
[미로1]
0 길, 1 벽, 2 출발, 3 도착
도달 가능 여부: 1 ok, 0 no
16 by 16
'''
from collections import deque

T = 10
for _ in range(T):
    t = int(input())  # 테케 번호
    graph = []
    sx, sy = -1, -1
    ex, ey = -1, -1
    for i in range(16):
        row = [r for r in input()]  # str
        for j in range(16):
            if row[j] == '2':
                sx, sy = i, j
            elif row[j] == '3':
                ex, ey = i, j
        graph.append(row)

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def bfs():
        visited = [[0]*16 for _ in range(16)]

        q = deque([(sx, sy)])
        visited[sx][sy] = 1

        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if nx < 0 or ny < 0 or nx >= 16 or ny >= 16:
                    continue
                if (nx, ny) == (ex, ey):
                    return '1'
                if not visited[nx][ny] and graph[nx][ny] == '0':
                    visited[nx][ny] = 1
                    q.append((nx, ny))

        return '0'

    print(f'#{t} ' + bfs())