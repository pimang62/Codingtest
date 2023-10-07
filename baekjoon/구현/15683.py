'''
[감시]
n by m, k개의 CCTV, 5종류
감시할 수 있는 방향의 칸 전체를 감시
벽은 통과할 수 없음 : 사각지대
회전은 90도 방향으로!

0: 빈칸, 6: 벽, 1~5: CCTV
사각지대의 최소 크기?

동:0 남:1 서:2 북:2
{
    1: [0, 1, 2, 3]
    2: [(0, 2), (1, 3)]
    3: [(0, 1), (1, 2), (2, 3), (3, 0)]
    4: [(0, 1, 3), (0, 1, 2), (1, 2, 3), (2, 3, 0)]
    5: [(0, 1, 2, 3)]
    }

1. cctv 번호 리스트 : [2, 3, 5, ...] 재귀 idx+1 사용
2. for k in k_dict[cctv[idx][0]] : 방향키 k
3. k 넘겨 받아 fill #

'''
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

cctv = []  # [(2, (1, 1)), (2, (3, 4)), ...]
for i in range(n):
    for j in range(m):
        if 0 < graph[i][j] < 6:  # 12345
            cctv.append((graph[i][j], (i, j)))  # 1, (2, 2)

k_list = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 3], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
    5: [[0, 1, 2, 3]]
}

#     동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

res = 1e9  # 최솟값 결과

def fill(k_tmp, x, y, board):
    for k in k_tmp:
        nx = x  # 각 k마다 업데이트이므로 초기화 필요!
        ny = y 
        while True:
            nx += dx[k]
            ny += dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            if board[nx][ny] == 6:
                break  # 다음 k로
            if board[nx][ny] == 0:
                board[nx][ny] = '#'

def dfs(idx, graph_tmp):  # 0
    global res
    if idx == len(cctv):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if graph_tmp[i][j] == 0:
                    cnt += 1
        res = min(res, cnt)
        return

    board = deepcopy(graph_tmp)
    num, (x, y) = cctv[idx]  # 1, (2, 2)
    for k_tmp in k_list[num]:  # 1: [0, 2] ...
        fill(k_tmp, x, y, board)
        dfs(idx+1, board)
        board = deepcopy(graph_tmp)  # 다시 처음 board로 초기화
    
dfs(0, graph)
print(res)