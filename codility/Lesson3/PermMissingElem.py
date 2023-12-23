# array contains integers in the range [1..(N + 1)]
# find that "missing" element. return 4

# 100% : O(N) or O(NlogN)
def solution(A):
    N = len(A)
    if N == 0:
        return 1
    
    d = [0]*(N+2)
    d[0] = 1
    for i in range(N):
        d[A[i]] = 1

    return d.index(0)