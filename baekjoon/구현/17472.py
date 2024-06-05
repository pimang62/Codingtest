'''
[다리 만들기 2]
n by m, 땅(1)/바다(0)

다리는 바다에만 건설, 가로/세로
다리 길이는 차지하는 칸 수

다리를 연결해서 모든 섬을 연결
교차하는 경우에도 다리 길이 포함

[[0, 0, 0, 0, 0, 0, 1, 1], 
 [2, 2, 0, 0, 0, 0, 1, 1], 
 [2, 2, 0, 0, 0, 0, 0, 0], 
 [2, 2, 0, 0, 0, 3, 3, 0], 
 [0, 0, 0, 0, 0, 3, 3, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0], 
 [4, 4, 4, 4, 4, 4, 4, 4]]
'''
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < m

def dfs(x, y, cnt):
    global visited
    graph[x][y] = cnt
    for l in range(4):
        nx, ny = x+dx[l], y+dy[l]
        if not in_range(nx, ny) or visited[nx][ny]:
            continue
        if graph[nx][ny] == 1:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt)

    return

k = 1
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            dfs(i, j, k)
            k += 1

edge = set()

def distance(x, y):
    now = graph[x][y]
    for l in range(4):
        nx, ny = x+dx[l], y+dy[l]
        while in_range(nx, ny):




for i in range(n):



for j in range(m):
