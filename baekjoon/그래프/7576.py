'''
[토마토]
n by m 상자
보관 후 하루가 지나면 익은 토마토 인접한 곳들이 익게 된다.
토마토들이 며칠이 지나면 다 익게 되는지 최소 일수를 알고 싶다!
1은 익은 토마토, 0은 익지 않은 토마토, -1은 토마토가 없음

- 토마토가 *모두 익을 때까지의 최소 날짜
- 처음부터 모든 토마토가 익어있으면 0
- 토마토가 모두 익지 못하면 -1

입력)
m, n = map(int, input().split())

tomato = []

graph = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1: tomato.append((i, j))

참고)
https://jae04099.tistory.com/entry/%EB%B0%B1%EC%A4%80-7576-%ED%86%A0%EB%A7%88%ED%86%A0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EC%84%A4%ED%8F%AC%ED%95%A8       

'''

from collections import deque

m, n = map(int, input().split())

tomato = []

graph = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1: tomato.append((i, j))
    graph.append(row)


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cnt = 0

q = deque(tomato)

while q:
    x, y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny] += graph[x][y] + 1  # 최단 거리로 기록!
            q.append((nx, ny))

for row in graph:
    for j in row:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(row))   

print(cnt-1)
