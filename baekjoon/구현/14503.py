'''
[로봇 청소기]
n by m, 0-indexed
1. 아직 청소되지 않은 경우, 현재 칸 청소
2. 주변 4칸 중 빈칸이 없는 경우
    1. 바라보는 방향 유지 한칸 후진, 1번 돌아감
    2. 바라보는 방향의 뒤쪽 칸이 벽이면 멈춤
3. 주변 4칸 중 청소되지 않은 빈칸이 있는 경우
    1. 반시계 방향 90도: 북동남서 -1
    2. 바라보는 방향 앞쪽 칸이 청소되지 않은 경우 한칸 전진
    3. 1번으로 돌아감

청소하는 칸의 개수?

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 9 9 0 0 0 1 0 1
1 0 9 9 0 9 1 1 0 1
1 0 0 9 9 9 1 1 0 1
1 0 0 9 9 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''
n, m = map(int, input().split())
r, c, d = map(int, input().split())  # (r, c), 바라보는 방향

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]  # 북동남서
dy = [0, 1, 0, -1]

answer = 0  # 청소한 칸의 개수

def in_range(tx, ty):
    if 0 <= tx < n and 0 <= ty < m:
        return True
    return False

def check(x, y):
    for k in range(4):
        tx, ty = x+dx[k], y+dy[k]
        if in_range(tx, ty) and graph[tx][ty] == 0:
            return True
    return False

while True:
    if graph[r][c] == 0:
        graph[r][c] = 9  # 청소 기록
        answer += 1
    if not check(r, c):  # 주변에 빈칸이 없는 경우
        nx, ny = r - dx[d], c - dy[d]
        if not in_range(nx, ny) or graph[nx][ny] == 1:  # != 0은 안됨!
            break
        else:
            r, c = nx, ny  # 뒤로 후진
    else:  # 주변에 빈칸이 있는 경우
        d = (d-1) if d-1 >= 0 else 3   # 음수면 3
        nx, ny = r + dx[d], c + dy[d]
        if in_range(nx, ny) and graph[nx][ny] == 0:
            r, c = nx, ny  # 앞으로 전진

print(answer) 