'''
[보급로]
복구 시간 가장 짧은 길로?
'''
from heapq import heappush, heappop

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input())

for i in range(1, t+1):
    n = int(input())
    graph = [[int(v) for v in input()] for _ in range(n)]
    
    def dijkstra():
        visited = [[1e9]*n for _ in range(n)]
        
        q = []
        heappush(q, (0, 0, 0))  # weight, 시작점
        visited[0][0] = 0
        
        while q:
            (w, x, y) = heappop(q)
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if visited[x][y] + graph[nx][ny] < visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + graph[nx][ny]
                    heappush(q, (graph[nx][ny], nx, ny))
        
        return visited[-1][-1]
    
    answer = dijkstra()
     
    print(f'#{i} '+ str(answer))