'''
[나이트의 이동]
나이트가 이동할 수 있는 칸
몇 번 움직이면 이 칸으로 이동할 수 있나?

각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지?

'''
import sys
input = sys.stdin.readline

from collections import deque

t = int(input())

for _ in range(t):
    
    result = 0

    l = int(input())
    graph = [ [-1]*l for _ in range(l) ]
    visited = [ [0]*l for _ in range(l) ]

    # start
    a, b = map(int, input().split())
    graph[a][b] = 0
    # end
    c, d = map(int, input().split())
    graph[c][d] = 1

    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]

    q = deque([(a, b)])
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue

            if visited[nx][ny] == 0 and graph[nx][ny] == 1:    # end point
                visited[nx][ny] = 1
                result = graph[x][y] + 1
                break

            if visited[nx][ny] == 0 and graph[nx][ny] == -1:
                visited[nx][ny] = 1
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    
    print(result)

        

