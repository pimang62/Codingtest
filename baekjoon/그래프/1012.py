'''
[유기농 배추]
어떤 배추에 흰 지렁이가 살고 있으면 인접한 배추들도 보호받는다.
서로 인접한 배추들이 몇 군데 퍼져있는지 조사하여 최소 흰 지렁이의 마리 수?

입력)
T = int(input())

for _ in range(T):

    m, n, k = map(int, input().split())

    graph = [ [0]*n for _ in range(m) ]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

'''
from collections import deque

def bfs(i, j, graph):

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque([(i, j)])
    
    # graph 초기화
    graph[i][j] = 0     

    while q:
        x, y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            
            if graph[nx][ny] == 1:
                # 큐에 넣기
                q.append((nx, ny))

                # graph 초기화
                graph[nx][ny] = 0

    return 1

T = int(input())

for _ in range(T):

    m, n, k = map(int, input().split())

    graph = [ [0]*n for _ in range(m) ]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    
    # 흰 지렁이 개수
    cnt = 0
    
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                # cnt += bfs(i, j, visited, graph)
                cnt += bfs(i, j, graph)
    print(cnt)
