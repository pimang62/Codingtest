'''
[차이를 최대로]
N개의 정수, 배열 A
정수의 순서를 적절히 바꿈

|A[0]-A[1]| + |A[1]-A[2]| + ... 최댓값?

3 <= N <= 8
'''
from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

answer = 0  # 최댓값
for perm in permutations(A, N):
    cnt = 0
    for i in range(0, N-1):
        cnt += abs(perm[i] - perm[i+1])
    answer = max(answer, cnt)

print(answer)