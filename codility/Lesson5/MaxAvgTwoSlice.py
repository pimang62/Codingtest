# non-empty array A consisting of N integers is given
# (P, Q), 0 ≤ P < Q < N, slice contains at least two elements
# average of a slice (P, Q) = A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice
# (A[P] + A[P + 1] + ... + A[Q]) / (Q - P + 1).
# find the "starting position" of a slice whose "average is minimal".
# divide 2 or 3

# 90% : return sum(A)/2, 100% : O(N)
def solution(A):
    N = len(A)  # [2, 100000]
    if N == 2:
        return 0  # index!!

    answer = 1e9  # minimal
    pos = 0  # idx
    for i in range(N-1):
        if answer > (A[i]+A[i+1])/2:
            answer = (A[i]+A[i+1])/2
            pos = i
    for i in range(N-2):
        if answer > (A[i]+A[i+1]+A[i+2])/3:
            answer = (A[i]+A[i+1]+A[i+2])/3
            pos = i
    return pos