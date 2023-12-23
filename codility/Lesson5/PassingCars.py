# "non-empty" array A consisting of N
# 0 east, 1 west
# count passing cars, (P, Q), where 0 ≤ P < Q < N
# P is traveling to the east and Q is traveling to the west.
# returns the "number" of pairs of passing cars. return 5
# return "-1" if the number of pairs of passing cars "exceeds" 1,000,000,000.

# 70% : if cnt <= 1000000000, 100% : O(N)
def solution(A):
    N = len(A)  # [1..100,000]
    # [3, 3, 2, 2, 1, 0]
    d = [0]*(N+1)  # [0, N]
    for i in range(N-1, -1, -1):
        d[i] = d[i+1] + A[i]  # 0 or 1
    
    cnt = 0  # 내가 0일 때 뒤의 1 개수
    for i in range(N):
        if A[i] == 0:
            cnt += d[i+1]
    
    return cnt if cnt <= 1000000000 else -1