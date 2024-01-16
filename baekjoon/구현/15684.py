'''
[사다리 조작]
가로선을 추가해서, 사다리 게임의 결과를 조작하고자 함
i번 세로선의 결과가 i번 나오게
추가해야 하는 가로선 개수의 최솟값?
3보다 큰 정답 -1, 불가능 -1

  0 1 2 3 4 
0 - -
1     - - 
2   - -
3
4 - -   - -
5 

  0 1 2 3 4 5
0 - 
1     -
2   -
3
4 -     - 
5
'''
n, m, h = map(int, input().split())  # n개의 열, h개의 행

graph = [[0]*n for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())  # b, b+1열의 a번 행
    graph[a-1][b-1] = 1  # 0-indexed

def check():
    for j in range(n):
        y = j
        for x in range(h):
            if graph[x][y]:  # 지금 자리에 사다리가 있으면 오른쪽
                y += 1
            elif y > 0 and graph[x][y-1]:  # 왼쪽에 사다리가 있으면 왼쪽
                y -= 1
        if y != j:
            return False
    return True      

answer = 4  # depth min

def dfs(cnt, tx, ty):
    global answer
    if cnt > 3:
        return -1
    if check():
        answer = min(answer, cnt)
        return
    
    for i in range(tx, h):
        if i == tx:  # 현재 지점부터 채우기라면
            k = ty  # 해당 시작 지점에서부터 출발
        else:  # 첫 지점을 벗어나 행이 변경된 경우
            k = 0  # 0열부터 채우기
        for j in range(k, n-1):  # 1~n
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(cnt+1, i, j+2)  # 다음 사다리는 2칸 건너 뛰고부터 시작
                graph[i][j] = 0
    
dfs(0, 0, 0)
print(answer if answer < 4 else -1)

    

"""
from itertools import combinations
from copy import deepcopy

n, m, h = map(int, input().split())  # n개의 열, h개의 행

graph = [[0]+[0]*n+[0] for _ in range(h+2)]  # 동서로 padding
for _ in range(m):
    a, b = map(int, input().split())  # b, b+1열의 a번 행
    graph[a][b] = 1  # 1-indexed
    graph[a][b+1] = 1

dx = [0, 0]  # 동서
dy = [1, -1]

def in_range(i, j):
    if 0 <= i <= h+1 and 0 <= j <= n+1:
        return True
    return False

def check(board):
    flag = True
    for j in range(1, n+1):
        x, y = 0, j
        while True:
            if x >= h:
                if y != j:  # 한 번이라도 false면
                    flag = False
                break
            while x <= h and board[x][y] == 0:
                x += 1
            for d in range(2):
                nx, ny = x+dx[d], y+dy[d]
                if in_range(nx, ny) and board[nx][ny] == 1:
                    x, y = nx+1, ny
                    break
    
    return True if flag else False

def main():
    candidate = [(i, j) for i in range(1, h+1) for j in range(1, n+1)]
    for k in range(1, 4):  # 1~3
        for combi in combinations(candidate, k):
            board = deepcopy(graph)
            for (a, b) in combi:
                if board[a][b] or board[a][b+1]:  # 이미 옆이 1이면
                    break  # 다음 combi 넘어감
                board[a][b] = 1  # 1-indexed
                board[a][b+1] = 1
            if check(board):
                return k
    return -1

print(main())
"""

"""
[[0, 0, 0, 0, 0, 0, 0], 
 [0, 1, 1, 0, 0, 0, 0], 
 [0, 0, 0, 1, 1, 0, 0], 
 [0, 0, 1, 1, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0], 
 [0, 1, 1, 0, 1, 1, 0],
 [0, 0, 0, 0, 0, 0, 0]]
"""

