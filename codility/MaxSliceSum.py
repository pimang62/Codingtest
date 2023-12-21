# (P, Q), such that 0 ≤ P ≤ Q < N, slice of array A
# [P, Q] is the total of A[P] + A[P+1] + ... + A[Q].
# returns the "maximum" sum of any slice of A.
import sys

def solution(A):
    # [3, 2, -6, 4, 0]
    max_ending = 0
    max_slice = -sys.maxsize   # 최댓값
    for i in range(len(A)):
        # 자기 자신을 선택할 수 있음!
        # 양수만 뽑고 싶다면 max(0, val)
        max_ending = max(max_ending + A[i], A[i])
        max_slice = max(max_ending, max_slice)
    return max_slice