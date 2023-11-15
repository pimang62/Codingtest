'''
[Sum]
행, 열, 대각선의 합 최대!
'''
for _ in range(10):
    t = int(input())
    answer = 0  # max
    graph = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        answer = max(answer, sum(graph[i]))

    for j in range(100):
        each_col = 0
        for i in range(100):
            each_col += graph[i][j]
        answer = max(answer, each_col)

    for i in range(100):
        left_diagonal = 0
        for j in range(100):
            if i == j:
                left_diagonal += graph[i][j]
        answer = max(answer, left_diagonal)

    for i in range(99, -1, -1):
        right_diagonal = 0
        for j in range(99, -1, -1):
            if i == j:
                right_diagonal += graph[i][j]
        answer = max(answer, right_diagonal)

    print(f'#{t} ' + str(answer))