'''
k번 반복한 이후의 위치?

1. x보다 작은 곳으로 이동 가능
2. 도달할 수 있는 칸의 최댓값 이동
3. (행 번호, 열 번호) 우선순위 정렬

k번을 반복하지 않았더라도 더이상 갈 곳이 없으면 종료!
result r, c : 1-indexed

- k번 반복하면서 좌표를 추가 : rep, cnt
- 해당 좌표의 작은 값들 중 가장 큰 값 고름 : q -> sort

res = []
while rep(r-1, c-1):
    if cnt >= k:
        break
    i, j = rep.popleft()
    res.append(bfs(i, j))  # 현재 좌표
    cnt += 1

if cnt == k:
    rr, rc = res[-1]
    print(*[rr+1, rc+1])
'''
import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())  # 1-indexed

rep = deque([(r-1, c-1)])  # 첫 좌표

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(i, j, value):
    visited = [[0]*n for _ in range(n)]
    
    q = deque([(i, j)])
    visited[i][j] = 1

    possible = []  # 조건에 맞게 갈 수 있는 값

    while q:
        x, y = q.popleft()
        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if not visited[nx][ny] and graph[nx][ny] < value:
                visited[nx][ny] = 1
                possible.append((graph[nx][ny], nx, ny))
                q.append((nx, ny))
    
    if possible:
        possible.sort(key=lambda x: (-x[0], x[1], x[2]))
    else:
        return None

    return possible[0]

cnt = 0  # 반복 횟수
result = [(r-1, c-1)]  # 반복 시 추가된 좌표들
while rep:
    if cnt >= k:
        break
    i, j = rep.popleft()
    if bfs(i, j, graph[i][j]) is not None:  # 현재 좌표
        val, ni, nj = bfs(i, j, graph[i][j])
        rep.append((ni, nj))
        result.append((ni, nj))
    else:
        break
    cnt += 1

rr, cc = result.pop()
print(*[rr+1, cc+1])