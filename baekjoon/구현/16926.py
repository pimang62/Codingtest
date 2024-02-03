'''
[배열 돌리기 1]
배열과 정수 R이 주어짐
배열을 반시계 방향으로 R번 돌린 결과?

(0, 0) (0, 1) (0, 2) (0, 3)
(1, 0) (1, 1) (1, 2) (1, 3)
(2, 0) (2, 1) (2, 2) (2, 3)
(3, 0) (3, 1) (3, 2) (3, 3)

(n-1)*2 + (m-1)*2번씩 반복

'''
from collections import deque

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
board = [[0]*m for _ in range(n)]  # new graph

# r %= (n-1)*2 + (m-1)*2

visited = [[0]*m for _ in range(n)]
for i in range(n):
    
    q = deque()
    if visited[i][i]:
        break
    
    # 각 껍질을 저장하는 부분
    for x in range(i, n-i):
        if not visited[x][i]:
            visited[x][i] = 1
            q.append(graph[x][i])
    
    for y in range(i, m-i):
        if not visited[n-i-1][y]:
            visited[n-i-1][y] = 1
            q.append(graph[n-1-i][y])
    
    for x in range(n-i-1, i-1, -1):
        if not visited[x][m-i-1]:
            visited[x][m-i-1] = 1
            q.append(graph[x][m-i-1])
    
    for y in range(m-i-1, i-1, -1):
        if not visited[i][y]:
            visited[i][y] = 1
            q.append(graph[i][y])
    
    # 얼마나 돌릴지 저장
    k = r % ((n-i*2-1)*2 + (m-i*2-1)*2)  # 최적화
    q.rotate(k)
    
    # 각 자리에 다시 배정
    for x in range(i, n-i):
        if not board[x][i]:
            board[x][i] = q.popleft()
    
    for y in range(i, m-i):
        if not board[n-1-i][y]:
            board[n-1-i][y] = q.popleft()
    
    for x in range(n-i-1, i-1, -1):
        if not board[x][m-i-1]:
            board[x][m-i-1] = q.popleft()
    
    for y in range(m-i-1, i-1, -1):
        if not board[i][y]:
            board[i][y] = q.popleft()

for i in range(n):
    print(*board[i])