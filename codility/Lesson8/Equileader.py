# "non-empty" array A consisting of N
# "leader" of this array is the value that occurs in "more than half" of the elements of A.
# index S, 0 ≤ S < N - 1, 
# A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] have "leaders" of the "same" value.
# returns the "number" of equi leaders.
from collections import Counter

# 80% : Timeout always find key, 100% : O(N)
def solution(A):
    N = len(A)  # [1..100,000]
    if N == 1:
        return 0  # "number"

    # leader of this array is the value that occurs in more than half of the elements of "A".
    d2 = Counter(A)  # total부터 시작
    key = 0  # leader 찾아 놓기
    max_val = 0
    for k, v in d2.items():
        if v > max_val:
            max_val = v
            key = k

    cnt = 0 
    d1 = Counter()
    for i in range(0, N-1):  # d1 리스트 길이 i+1
        d1[A[i]] += 1
        d2[A[i]] -= 1
        if 2*d1[key] > (i+1) and 2*d2[key] > (N-(i+1)):
            cnt += 1
    
    return cnt