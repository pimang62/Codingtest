'''
[오목]
1~19행, 1~19열
검은색이 이겼는지, 흰색이 이겼는지, 승부가 안났는지

검은 1, 흰 2, 아직 0 출력
누군가 이겼을 경우 가장 왼쪽 가로줄 번호, 세로줄 번호 출력
'''
graph = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]  # 동, 동남, 북동, 남
dy = [1, 1, 0, 1]

def dfs(x, y, d, t, cnt):
    global graph
    if cnt == 5:
        nx, ny = x+dx[d], y+dy[d]
        if in_range(nx, ny) and graph[nx][ny] == t:
            return False  # 6개 이상이라면!
        return True
    nx, ny = x+dx[d], y+dy[d]
    if in_range(nx, ny) and graph[nx][ny] == t:
        return dfs(nx, ny, d, t, cnt+1)
    else:
        return False

def in_range(a, b):
    return 0 <= a < 19 and 0 <= b < 19

def check_back(x, y, d):
    # Check the opposite direction
    bx, by = x-dx[d], y-dy[d]
    if in_range(bx, by) and graph[bx][by] == graph[x][y]:
        return False
    return True

def main():
    for i in range(19):
        for j in range(19):  # 행 기준으로 우선 탐색
            if graph[i][j] in [1, 2]:
                for k in range(4):
                    if check_back(i, j, k):
                        if dfs(i, j, k, graph[i][j], 1):
                            return graph[i][j], (i+1, j+1)           
    return 0

answer = main()
if answer != 0:
    print(answer[0])
    print(*answer[1])
else:
    print(answer)