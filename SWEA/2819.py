'''
[격자판의 숫자 이어 붙이기]
4 by 4, 0-9 숫자
인접한 격자로 총 6번 이동
만들 수 있는 서로 다른 일곱자리 수?
'''
T = int(input())
for t in range(1, T+1):
    graph = [list(map(str, input().split())) for _ in range(4)]  # str

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def dfs(cnt, x, y, s):
        global answer
        if cnt > 6:
            return
        if cnt == 6:
            if s not in answer:
                answer.add(s)
                return
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                continue
            dfs(cnt+1, nx, ny, s+graph[nx][ny])

    answer = set()
    for i in range(4):
        for j in range(4):
            x, y = i, j
            dfs(0, x, y, graph[i][j])

    print(f'#{t} ' + str(len(answer)))

    #print(f'#{t} ' + )
