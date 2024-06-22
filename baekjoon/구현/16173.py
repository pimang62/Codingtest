'''
[점프왕 쩰리(Small)]
https://www.acmicpc.net/problem/16173

1. 정사각형 구역 내부에서만 움직임
2. 출발점은 항상 가장 왼쪽 가장 위
3. 이동 방향은 '오른쪽'과 '아래'
4. 가장 오른쪽 아래에 도달하면 승리
5. 한 번에 이동하는 칸 수는 밟고 있는 칸에 적힌 수

이길 수 있는지를 알려달라!
이기면 "HaruHaru", 아니면 "Hing"

2 <= N <= 3
'''
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

x, y = 0, 0  # initialize

dx = [0, 1]  # 동 남
dy = [1, 0]

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

flag = False

def dfs(x, y):
    if graph[x][y] == -1:
        print("HaruHaru")
        exit()
    
    dist = graph[x][y]
    for k in range(2):
        nx, ny = x+dx[k]*dist, y+dy[k]*dist
        if not in_range(nx, ny) or visited[nx][ny]:
            continue
        else:
            visited[nx][ny] = 1
            dfs(nx, ny)
    
    return

dfs(x, y)

print("Hing")