'''
[드래곤 커브]
k세대 드래곤 커브는 k-1세대 커브를
끝 점 기준 90도 시계 방향 회전한 뒤 붙임

1 by 1 정사각형 네 꼭짓점이 
모두 드래곤 커브인 개수?

0 <= x, y <= 100 만 유효한 좌표
격자 밖으로 벗어나지 않고, 겹칠 수 있다.

x축은 동쪽, y축은 남쪽(?;)
-> x가 열 방향, y가 행 방향 (y, x)
0: 동[0] -> 북
1: 북[3] -> 서
2: 서[2] -> 남
3: 남[1] -> 동

1 <= n <= 20
0 <= g <= 10

3
3 3 0 1
4 2 1 3
4 2 2 1
>>> 4

ex1. (3, 3, 0) -> (3, 4, 0).
     (2, 4, 1) <- (3, 4, 0) (3, 3, 0)
     (2, 4, 1) -> ()

sol. 1 -> 2 -> 3 2 -> 3 0 3 2 

4
3 3 0 1
4 2 1 3
4 2 2 1
2 7 3 4
>>> 11

sol. 3 -> 0 -> 1 0 -> 1 2 1 0 -> 1 2 3 2 1 2 1 0
'''
n = int(input())  # 드래곤 커브 정보 개수
graph = [[0]*101 for _ in range(101)]  # 0~100

def in_range(a, b):
    if 0 <= a < 101 and 0 <= b < 101:
        return True
    return False

def check():
    cnt = 0  # 1 by 1 개수
    for i in range(101):
        for j in range(101):
            if not in_range(i+1, j+1):
                continue
            if graph[i][j] and graph[i][j+1] and graph[i+1][j] and graph[i+1][j+1]:  # == 1
                cnt += 1
    return cnt

# y가 행!! x가 열!!
dy = [0, -1, 0, 1]  # 동0 북1 서2 남3
dx = [1, 0, -1, 0]
    
for _ in range(n):
    x, y, d, g = map(int, input().split())
    
    stack = [d]  # 첫 방향
    graph[y][x] = 1  # initialize
    
    # 0세대 드래곤 커브
    y, x = y+dy[d], x+dx[d]  # 한 번 움직임
    if in_range(y, x):  # 갈 수 있는지 체크
        graph[y][x] = 1
    
    for _ in range(g):  # 3이면 (0) 1 2 3
        # stack <- 역순 탐색
        for i in range(len(stack)-1, -1, -1):
            dd = (stack[i]+1) % 4   # next direction
            y, x = y+dy[dd], x+dx[dd]
            if in_range(y, x):  # 갈 수 있는지 체크
                graph[y][x] = 1
            stack.append(dd)  # 새로 추가: stack 도는 동안은 고려 안함

# 모두 움직이고 난 다음 -> cnt
print(check())