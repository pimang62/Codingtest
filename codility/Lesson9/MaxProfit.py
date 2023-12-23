# A consisting of N integers
# daily "prices" of a stock share for a period of N consecutive days
# bought on day P and sold on day Q, 0 ≤ P ≤ Q < N
# "profit" of such transaction is equal to A[Q] - A[P], A[Q] ≥ A[P]
# loss of A[P] - A[Q].
# Maximum possible profit was 356, bought on day 1 and sold on day 5.
# returns the maximum possible profit
# return 0 if it was impossible to gain any profit.

# 100% : O(N)
def solution(A):
    N = len(A)  # [0..400,000]
    # return 0 if it was impossible to gain any profit.
    if N < 2:  # 0 or 1
        return 0

    d = [1e9]*N  # 최솟값 기록
    answer = 0  # 최대 profit
    for i in range(N):
        d[i] = min(d[i-1], A[i]) # : [0..200,000]
        answer = max(answer, A[i] - d[i])  # or (0, )
    return answer