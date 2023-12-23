# non-empty array A
# "permutation" is a sequence containing each element from 1 to N once
# "check" whether array A is a permutation or not : 1 / 0

# 100% : O(N) or O(NlogN)
def solution(A):
    N = len(A)  # [1..100,000]
    d = {}
    for i in range(N):
        if A[i] not in d:
            d[A[i]] = 1
        else:
            d[A[i]] += 1
    
    for n in range(1, N+1):  # [1~N]
        if n not in d:
            return 0
    return 1
