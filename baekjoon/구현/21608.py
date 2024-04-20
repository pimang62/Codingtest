'''
[상어 초등학교]
n by n, n^2명 자리를 정할 것
학생의 순서와 각 학생이 좋아하는 학생 4명 조사
맨해튼 거리 1이면 == 인접하다

1. 비어있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많게
2. 1이 여러 개면 비어있는 칸이 가장 많은 칸으로
3. 행의 번호가 가장 작은, 열이 번호가 가장 작은
(like cnt, none cnt, row, col)

3
4 2 5 1 7
3 1 9 4 5
9 8 1 2 3
8 1 9 3 4
7 2 3 4 8
1 9 2 5 7
6 5 2 3 4
5 1 9 2 8
2 9 3 1 4

0 0 0
0 0 0
0 0 0
'''
from heapq import heappush, heappop

n = int(input())

like = {}
for _ in range(n**2):
    who, *four = map(int, input().split())
    like[who] = four

graph = [[0]*n for _ in range(n)]

dx = [0, 1, 0, -1]  # 동남서북
dy = [1, 0, -1, 0]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < n

def check(four) -> tuple:
    q = []
    for i in range(n):
        for j in range(n):
            how_many, blank = 0, 0
            if graph[i][j] != 0:
                continue
            for l in range(4):
                nx, ny = i+dx[l], j+dy[l]
                if not in_range(nx, ny):
                    continue
                if graph[nx][ny] in four:
                    how_many += 1
                elif graph[nx][ny] == 0:
                    blank += 1
            heappush(q, (-how_many, -blank, i, j))
    return heappop(q)

def satisfy():
    answer = 0
    for i in range(n):
        for j in range(n):
            who = graph[i][j]
            cnt = 0
            for l in range(4):
                nx, ny = i+dx[l], j+dy[l]
                if not in_range(nx, ny):
                    continue
                if graph[nx][ny] in like[who]:
                    cnt += 1
            answer += 10**(cnt-1) if cnt > 0 else 0
    return answer
    
def solution():
    global graph
    for who in like.keys():  # 4, 3, 9, ...
        _, _, x, y = check(like[who])
        graph[x][y] = who
    result = satisfy()
    return result

print(solution())