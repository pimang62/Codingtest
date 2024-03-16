'''
[스도쿠]
9 by 9 board
각 행, 열, 3 by 3에 1~9
'''
import sys
from copy import deepcopy

input = sys.stdin.readline

graph = []
zeros = []
for i in range(9):
    row = list(map(int, input().rstrip()))
    for j in range(9):
        if row[j] == 0:
            zeros.append((i, j))
    graph.append(row)

def check(n, x, y):
    # 행 check
    for j in range(9):
        if graph[x][j] == n:  # 중복값이 있다면
            return False
    # 열 check
    for i in range(9):
        if graph[i][y] == n:  # 중복값이 있다면
            return False
    # 3 by 3 check: 0 1 2 | 3 4 5 | 6 7 8
    start_x = (x // 3) * 3
    start_y = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if graph[start_x+i][start_y+j] == n:  # 중복값이 있다면
                return False
    return True

# answer = None  # global
def dfs(idx):  # zeros의 index
    # global answer
    if idx == len(zeros):
        for i in range(9):
            print(''.join(map(str, graph[i])))  # or list(map)
        exit()  # 시간 초과 해결!
        # if answer == None:
        #     answer = deepcopy(graph)  # deepcopy!, [:] X
        # print(graph)

    x, y = zeros[idx]  # idx번째의 x, y
    for n in range(1, 10):  # 1~9
        if check(n, x, y):
            graph[x][y] = n
            dfs(idx+1)
            graph[x][y] = 0
    return 

dfs(0)  # zeros[0] 에서 시작
# for i in range(9):
#     print(*answer[i])