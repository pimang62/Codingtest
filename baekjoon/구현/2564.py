'''
[경비원]
블록 중간을 가로지를 수 없음
경계에 무인 경비를 의뢰한 상점
상점은 숫자, 동근이 x

각 상점 사이의 최단 거리 합?
단, 모서리에는 존재하지 않음
                    <- 열 추가?
- - - - 0 - - - - - - (1, 4) 행 index
- - - - - - - - - - - 
0 - - - - - - - - - - (3, 2) 열 index
- - - - - - - - - - - 
- - - - - - - - - - - <- 한 행 추가?
- - - x - - - - 0 - - (2, 3) (2, 8)

1 동(0) 2 서(2) 3 북(3) 4 남(1) 먼저!
'''
m, n = map(int, input().split())  # 가로, 세로
k = int(input())  # 상점 개수

x, y = 0, 0
d = 0  # 처음 방향
graph = [[0]*(m+1) for _ in range(n+1)]
islast = 1
# 1 북 2 남 (행 index) 3 서 4 동 (열 index)
for c in range(k+1):
    if c == k:
        islast = 2
    DIR, idx = map(int, input().split())
    if DIR == 1: # 북
        graph[0][idx] = islast
        if islast == 2:
            x, y = 0, idx
            d = 0  # 동
    elif DIR == 2:  # 남
        graph[-1][idx] = islast
        if islast == 2:
            x, y = n, idx
            d = 2  # 서
    elif DIR == 3:  # 서
        graph[idx][0] = islast
        if islast == 2:
            x, y = idx, 0
            d = 3  # 북
    else:  # == 4  # 동
        graph[idx][-1] = islast
        if islast == 2:
            x, y = idx, m
            d = 1  # 남

def in_range(a, b):
    return 0 <= a <= n and 0 <= b <= m

dx = [0, 1, 0, -1]  # 동남서북
dy = [1, 0, -1, 0]

answer = 0  # 최단거리 합
cnt = 0
while True:
    
    while cnt < 2*(n+m) and in_range(x+dx[d], y+dy[d]):
        cnt += 1
        x += dx[d]
        y += dy[d]
        
        if graph[x][y] == 1:
            answer += min(cnt, 2*(n+m)-cnt)
    
    if cnt >= 2*(n+m):
        break
    
    d = (d+1) % 4  # 방향 전환

print(answer)

'''
[[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0]]
'''

# 다른 사람의 풀이
## https://otu165.tistory.com/2

import sys
read = sys.stdin.readline

def get_distance(x, y):
    if x == 1:  # 북
        return y
    if x == 2:  # 남
        return w + h + w - y
    if x == 3:  # 서
        return w + h + w + h - y
    if x == 4:  # 동
        return w + y

# 입력
w, h = map(int, read().split())
n = int(read())

# 풀이
course = []
for _ in range(n + 1):  # (0, 0) 에서 상점까지의 거리
    x, y = map(int, input().split())
    course.append(get_distance(x, y))

answer = 0

for i in range(n):  # 동근이와 상점 사이의 최단거리
    in_course = abs(course[-1] - course[i])
    out_course = 2 * (w + h) - in_course
    answer += min(in_course, out_course)

# 출력
print(answer)