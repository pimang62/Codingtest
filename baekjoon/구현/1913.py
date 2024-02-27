'''
[달팽이]
홀수인 자연수 n

9 2 3
8 1 4
7 6 5

  n//2
3 (1, 1) 
-> 북 1 (0, 1) 
-> 동 1 (0, 2) 
-> 남 2 (1, 2), (2, 2)
-> 서 2 (2, 1), (2, 0)
-> 북 2

25 10 11 12 13
24  9  2  3 14
23  8  1  4 15
22  7  6  5 16
21 20 19 18 17

5 (2, 2)
북1 동1 남2 서2
북3 동3 남4 서4
북4

7 (3, 3)
...
북5
북6

'''
n = int(input())
target = int(input())

graph = [[0]*n for _ in range(n)]
graph[n//2][n//2] = 1  # initialize

# # target과 같을 때
# answer = [n//2, n//2]  # initialize 1!!

# def check(x, y):
#     global answer
#     if graph[x][y] == target:
#         answer = [x+1, y+1]
#     return

dx = [-1, 0, 1, 0]  # 북 동 남 서
dy = [0, 1, 0, -1]

cnt = 2  # 반복 횟수 2배씩
num = 1  # start value
x, y = n//2, n//2  # (좌표)
while True:
    if cnt > n:
        for _ in range(cnt-2):
            num += 1
            x, y = x+dx[0], y+dy[0]
            graph[x][y] = num
            # check(x, y)
        break
            
    for _ in range(cnt-1):
        num += 1
        x, y = x+dx[0], y+dy[0]
        graph[x][y] = num
        # check(x, y)
    
    for _ in range(cnt-1):
        num += 1
        x, y = x+dx[1], y+dy[1]
        graph[x][y] = num
        # check(x, y)
    
    for _ in range(cnt):
        num += 1
        x, y = x+dx[2], y+dy[2]
        graph[x][y] = num
        # check(x, y)
    
    for _ in range(cnt):
        num += 1
        x, y = x+dx[3], y+dy[3]
        graph[x][y] = num
        # check(x, y)
    
    cnt += 2

answer = [n//2, n//2]  # initialize 1!
for i in range(n):
    for j in range(n):
        if graph[i][j] == target:
            answer = i+1, j+1
    print(*graph[i])

print(*answer)
