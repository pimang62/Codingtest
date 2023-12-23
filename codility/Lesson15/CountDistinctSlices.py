# integer M and a non-empty array A consisting of N "non-negative" integers are given.
# All integers in array A are less than or equal to M. : A[i] <= M
# (P, Q), 0 ≤ P ≤ Q < N, slice of array A, A[P], A[P + 1], ..., A[Q] : [P, Q]
# distinct slice is a slice consisting of "only unique numbers".
# calculate the number of distinct slices, return 9
# if greater than 1,000,000,000, the function should return 1,000,000,000.

# 80% : not if greater than, 100% : O(N)
def solution(M, A):
    N = len(A)  # [1..100000]
    front = 0
    cnt = 0  # 부분 집합 개수 기록 
    sets = set()
    for back in range(N):
        while front < N and A[front] not in sets:
            sets.add(A[front])
            cnt += (front-back) + 1
            front += 1
        sets.remove(A[back])
    # if greater than 1,000,000,000, the function should return 1,000,000,000.
    if cnt > 1000000000:
        return 1000000000
    return cnt