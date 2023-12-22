# integer M, non-empty array A, N non-negative integers
# All integers in array A are "less than or equal" to M. <= M
# (P, Q), 0 ≤ P ≤ Q < N, slice A[P], A[P + 1], ..., A[Q]
# "distinct" slice is a slice consisting of only "unique" numbers
# return 9, "calculate" the number of distinct slices
# If the number of distinct slices is greater than 1,000,000,000, 
# the function should return "1,000,000,000."

# 효율성 70% 정확성 100% : O(N*(N+M))
def solution(M, A):
    N = len(A)
    front, dist = 0, set()
    cnt = 0  # 경우의 수 계산
    for back in range(N):
        front = back
        while front < N and (A[front] not in dist):
            dist.add(A[front])
            front += 1
            cnt += 1  # 가능한 경우의 수
        dist = set()  # reset
    return cnt

# 100%
from collections import defaultdict

def solution(M, A):
    # d = [0] * (M+1)  # 0~M]
    d = defaultdict(int)  # 대체해보기
    N = len(A)

    # [3, 4, 5, 5, 2]
    front, cnt = 0, 0
    for back in range(N):
        while front < N and d[A[front]] == 0:
            d[A[front]] += 1
            cnt += (front - back) + 1
            front += 1
        d[A[back]] -= 1
        if cnt > 1000000000:
            return 1000000000
    return cnt
