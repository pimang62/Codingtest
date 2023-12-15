'''
[2차원 배열의 합]
시간 복잡도: 1e5*3e6
'''
'''
# PyPy3로 제출
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0  # 최종 합
k = int(input())
for _ in range(k):
    summ = 0  # 각 시도 별 합
    i, j, x, y = map(int, input().split())
    for a in range(i-1, x):  # 좌표는 -1씩
        for b in range(j-1, y):  # j-1 ~ y-1
            summ += graph[a][b]
    print(summ)
'''
# 누적합으로 풀기
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 누적합 배열 만들기
d = [[0]*(m+1) for _ in range(n+1)]  # 1칸씩 더 있음
for i in range(1, n+1):
    for j in range(1, m+1):
        # (0, 0) ~ 원래 (i, j) 합 : (0, 0)~(i-1, j) 합 + (0, 0)~(i, j-1) 합 + 자기 자신 - (0, 0)~(i-1, j-1) 합
        d[i][j] = d[i-1][j] + d[i][j-1] + graph[i-1][j-1] - d[i-1][j-1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    answer = d[x][y] - d[i-1][y] - d[x][j-1] + d[i-1][j-1]
    print(answer)

"""
[[0, 0, 0, 0, 0], 
 [0, 1, 3, 6, 10], 
 [0, 3, 8, 15, 24], 
 [0, 6, 15, 27, 42], 
 [0, 10, 24, 42, 64]]
"""