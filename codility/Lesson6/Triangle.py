# triplet (P, Q, R) is "triangular" if 0 ≤ P < Q < R < N
# A[P] + A[Q] > A[R]
# returns 1 if there "exists" a triangular or 0

# 100% : O(NlogN)
def solution(A):
    N = len(A)
    # [1, 2, 5, 8, 10, 20]
    A.sort()

    for i in range(N-2, 0, -1):  # [N-2~1]
        if (A[i-1] + A[i]) > A[i+1]:
            return 1
    return 0