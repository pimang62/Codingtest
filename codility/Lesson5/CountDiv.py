# three integers A, B and K
# returns the "number" of integers within the range [A..B] that are "divisible" by K : K로 나눠지는 [A, B] 사이의 수
# A ≤ i ≤ B, i mod K = 0

# 100% : O(1)
def solution(A, B, K):
    # A, B : [0..2,000,000,000]
    # K : [1..2,000,000,000]
    A = (A-1)//K
    B = B//K
    return B-A