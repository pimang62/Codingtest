'''
[배열 돌리기 4]
n by m, 배열 A의 값은 행의 합 중 최솟값
(r, c, s) -> (r-s, c-s) ~ (r+s, c+s)

정사학형을 시계 방향으로 한 칸씩 돌림
연산 수행 순서에 따라 배열 다름
'''
from itertools import permutations
from copy import deepcopy

n, m, k = map(int, input().split())

A = [
    list(map(int, input().split())) \
    for _ in range(n)
]

candidate = []  # 1-indexed
for _ in range(k):
    r, c, s = map(int, input().split())
    candidate.append((r, c, s))

answer = 1e9
def rotate(O, x, y, s):
    for l in range(1, s+1):  # 2
        prev = O[x-l][y-l]
        # 왼쪽: y 고정, x+1~
        for i in range(x-l, x+l):
            O[i][y-l] = O[i+1][y-l] 
        # 아래쪽 : x+interval-1 고정, y+1~
        for j in range(y-l, y+l):
            O[x+l][j] = O[x+l][j+1]
        # 오른쪽 : y+interval-1 고정, ~x+interval-2
        for i in range(x+l, x-l, -1):
            O[i][y+l] = O[i-1][y+l]
        # 위쪽 : x 고정, ~y+interval-1
        for j in range(y+l, y-l, -1):
            O[x-l][j] = O[x-l][j-1]
        
        O[x-l][y-l+1] = prev

for cand in permutations(candidate):
    O = deepcopy(A)  # original
    
    for (r, c, s) in cand:
        rotate(O, r-1, c-1, s)

    for k in range(n):
        answer = min(answer, sum(O[k]))

print(answer)

"""
from itertools import permutations
import copy

def rotate(x, y, s):
    for layer in range(1, s+1):
        top_left = A[x-layer][y-layer]
        
        # Left side
        for i in range(x-layer, x+layer):
            A[i][y-layer] = A[i+1][y-layer]
        
        # Bottom side
        for j in range(y-layer, y+layer):
            A[x+layer][j] = A[x+layer][j+1]
        
        # Right side
        for i in range(x+layer, x-layer, -1):
            A[i][y+layer] = A[i-1][y+layer]
        
        # Top side
        for j in range(y+layer, y-layer, -1):
            A[x-layer][j] = A[x-layer][j-1]
        
        A[x-layer][y-layer+1] = top_left

# 입력 처리
n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
operations = [tuple(map(int, input().split())) for _ in range(k)]

# 최소값 초기화
min_value = float('inf')

# 모든 연산 순서를 확인
for perm in permutations(operations):
    # 원본 배열을 복사
    original = copy.deepcopy(A)
    
    for op in perm:
        r, c, s = op
        r, c = r-1, c-1
        rotate(r, c, s)
    
    # 회전 결과에서 행의 합의 최솟값 계산
    for row in A:
        min_value = min(min_value, sum(row))
    
    # 배열 원본 복구
    A = copy.deepcopy(original)

print(min_value)
"""