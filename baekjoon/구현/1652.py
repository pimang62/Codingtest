'''
[누울 자리를 찾아라]
n by n, 가로 세로 연속 2개 이상: +1
'''
from copy import deepcopy
n = int(input())

graph = []
for _ in range(n):
    row = [0 if s == '.'  else 1 for s in input()]
    graph.append(row)

# 행 탐색
cnt1 = 0  # 누울 자리
board = deepcopy(graph)
for i in range(n):
    stack = []
    for j in range(n):
        while j < n and board[i][j] == 0:
            stack.append(0)
            board[i][j] = 1
            j += 1
        if j < n and board[i][j] == 1:
            if len(stack) >= 2:
                cnt1 += 1
            stack = []

# 열 탐색
cnt2 = 0  # 누울 자리
board = deepcopy(graph)
for j in range(n):
    stack = []
    for i in range(n):
        while i < n and board[i][j] == 0:
            stack.append(0)
            board[i][j] = 1
            i += 1
        if i < n and board[i][j] == 1:
            if len(stack) >= 2:
                cnt2 += 1
            stack = []

print(cnt1, cnt2)

# 다른 사람의 풀이
import sys
input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]
arr_h = [''.join(i) for i in zip(*arr)]
h,v = 0,0
for i in range(n):
    
    for j in arr[i].split('X'):
        if '..' in j:
            h += 1
    
    for j in arr_h[i].split('X'):
        if '..' in j:
            v += 1

print(h,v)