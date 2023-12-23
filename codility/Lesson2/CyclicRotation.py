# "Rotation" of the array means that each element is shifted "right" by one index,
# rotate array A "K" times
# N & K ["0"..100]

from collections import deque

# 70% : ([], 1), 100% : or N == 0
def solution(A, K):
    q = deque(A)
    N = len(A)
    if K == N or N == 0:  # edge case
        return list(q) 
    for _ in range(K%N):  # do not divide zero
        q.rotate(+1)  # 오른쪽으로 밀기
    return list(q)