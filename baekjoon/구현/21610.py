'''
[마법사 상어와 비바라기]
https://www.acmicpc.net/problem/21610

비바라기 -> 하늘에 비구름, N by N
1번 행 N번 행 연결, 1번 열 N번 열 연결

비구름: (N, 1), (N, 2), (N-1, 1), (N-1, 2)
구름 이동 M번 명령, 8개의 방향

1. 모든 구름 d_i 방향, s_i칸 이동
2. 구름이 있는 칸 물의 양 +1
3. 구름 사라짐
4. 물복사버그: 대각선 방향으로 거리 1 바구니 수만큼 +
  - 경계 넘어가면 거리 1 아님
5. 물이 2 이상인 모든 칸에 구름 생김, 물 양 -2
  - 구름이 생기는 칸은 3에서 사라진 칸 아님

M번의 이동 모두 끝난 후 바구니에 들어있는 물의 양 합?

해야할 일 
  - 첫 initial cloud: (N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)
  - def in_range: 물복사 시 쓰임
  - def make_cloud: 2이상인 칸 체크, -2도 해주어야
  - def pad_cor: 범위 벗어나면 안으로 오게끔
    - >= N: N이면 0, N+1이면 1, ... 좌표 -N
    - < 0: -1이면 N-1, -2이면 N-2, ... 좌표 +N
'''
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 8개 방향, 대각선: [2, 4, 6, 8]
dirs = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1),
        5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}

def in_range(a, b):
    return 0 <= a < N and 0 <= b < N

def make_cloud(moved_cloud):
    new_cloud = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and (i, j) not in moved_cloud:
                new_cloud.append((i, j))
                graph[i][j] -= 2
    
    return new_cloud

def pad_cor(c):  # 좌표 하나
    if c >= N:
        return c - N
    elif c < 0:
        return c + N
    return c

def main(cloud, d, s):
    dx0, dy0 = dirs[d]  # 1. 이동 방향
    moved_cloud = []
    for (x0, y0) in cloud:
        nx0, ny0 = pad_cor((x0 + dx0*s)%N), pad_cor((y0 + dy0*s)%N)
        graph[nx0][ny0] += 1
        moved_cloud.append((nx0, ny0))
    
    for (x1, y1) in moved_cloud:
        cnt = 0  # 대각선 몇 개
        for k in range(2, 9, 2):
            dx1, dy1 = dirs[k]
            nx1, ny1 = x1+dx1, y1+dy1
            if in_range(nx1, ny1) and graph[nx1][ny1]:
                cnt += 1
        graph[x1][y1] += cnt
    
    return make_cloud(moved_cloud)


# initialize
cloud = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]  

for _ in range(M):
    d, s = map(int, input().split())
    cloud = main(cloud, d, s)

answer = 0  # 전체 물의 양의 합
for i in range(N):
    for j in range(N):
        answer += graph[i][j]

print(answer)
