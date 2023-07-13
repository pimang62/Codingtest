'''
[단지번호붙이기]
n by n의 그래프
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
이 지도를 가지고 연결된 집의 모임인 단지를 정의한다.
각 단지에 속하는 집의 수를 오름차순으로 정렬!

입력)
n = int(input())

visited = [ [0]*n for _ in range(n) ]

graph = []
for _ in range(n):
    graph.append([i for i in input()])
'''

n = int(input())

visited = [ [0]*n for _ in range(n) ]

graph = []
for _ in range(n):
    graph.append([int(i) for i in input()])

cnt = 0     # 단지 개수
house = []

def move(visited, graph):
    for i in range(n):
        for j in range(n):
            '''
            if graph[n-1][n-1] == 1:
                return
            '''
            if visited[i][j] == 0 and graph[i][j] == 1:
                house.append(count(i, j, graph, visited))
                global cnt
                cnt += 1
            
            # *모든 집 방문
            visited[i][j] = 1
                    
from collections import deque

def count(i, j, graph, visited):
    
    visited[i][j] = 1   # 방문처리!!

    q = deque([(i, j)])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    h = 1      # *집 개수(집이 한 가구밖에 없을 때를 고려!)
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n :
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    h += 1
                    q.append((nx, ny))
                
                # *모든 집 방문
                visited[nx][ny] = 1
    
    return h

move(visited, graph)

# *오름차순!!
house.sort()

print(cnt)
for h in house:
    print(h)