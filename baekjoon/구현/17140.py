'''
[이차원 배열과 연산]
R 연산: 행 >= 열
C 연산: 행 < 열

수의 등장 횟수는 오름차순
여러가지면 수의 오름차순

[3, 1, 1] 3: 1, 1: 2
[3, 1, 1, 2] 3: 1, 1: 2, 2: 1
[2, 1, 3, 1, 1, 2]

가장 큰 열을 기준으로 padding
[3, 2, 0, 0] -> [3, 2]
'''
from collections import Counter
from copy import deepcopy

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

def in_range(N, M):  # 더 큰지 봐야함
    return r <= N and c <= M

def check(board):
    N, M = len(board), len(board[0])
    if in_range(N, M) and A[r-1][c-1] == k: # 1-indexed
        return True
    return False

def trans(sample):
    l = []
    for (k, v) in sample:
        l += [k, v]
    return l

cnt = 0  # 100 넘어가는지 check
while True:
    if cnt > 100:
        print(-1)
        break
    
    if check(A):
        print(cnt)
        break
    
    n, m = len(A), len(A[0])
    new_A = []
    if n >= m:
        max_length = 0
        for i in range(n):
            clean_Ai = [x for x in A[i] if x != 0]
            di = sorted(Counter(clean_Ai).items(), \
                key=lambda x: (x[1], x[0]))
            dilist = trans(di)
            new_A.append(dilist)
            max_length = max(max_length, len(dilist))
        for i in range(n):
            new_A[i] += [0]*(max_length-len(new_A[i]))
        A = deepcopy(new_A)
    else:   
        max_length = 0
        for j in range(m):
            clean_Aj = [A[i][j] for i in range(n) if A[i][j] != 0]
            dj = sorted(Counter(clean_Aj).items(), \
                key=lambda x: (x[1], x[0]))
            djlist = trans(dj)
            new_A.append(djlist)
            max_length = max(max_length, len(djlist))
        new_A = [x + [0]*(max_length-len(x)) for x in new_A]
        A = [list(tmp) for tmp in zip(*new_A)]  # Transpose!
    
    cnt += 1
