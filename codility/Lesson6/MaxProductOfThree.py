# "non-empty" array A consisting of N
# product of "triplet" (P, Q, R)
# A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).
# find the "maximal" product of any triplet.
# return 60, (2, 4, 5) is maximal.
# (-, -), (+, +) +
# (- ) (+, +, +)
# (-, -, ) (+)

# 100% : O(NlogN)
def solution(A):
    A.sort()
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])