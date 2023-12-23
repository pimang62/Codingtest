# "non-empty" array A consisting of N
# integer P, 0 < P < N
# "difference" between the two parts : |(A[0] + A[1] + ... + A[P - 1]) - (A[P] + A[P + 1] + ... + A[N - 1])| = [0, p), [p, n)
# returns the "minimal" difference that can be achieved.

# 100% : O(N) maybe O(3N)
def solution(A):
    N = len(A)
    if N == 1:
        return 0

    front = [0]*(N+1)
    for i in range(1, N+1):
        front[i] = front[i-1] + A[i-1]

    back = [0]*(N+1)
    for j in range(N-1, -1, -1):
        back[j] = back[j+1] + A[j]
    
    # [0, 3, 4, 6, 10, 13]  # 1~N-1
    # [13, 10, 9, 7, 3, 0]
    # [0, 1] [1, 0]
    answer = 1e9
    for k in range(1, N):
        answer = min(answer, abs(front[k]-back[k]))
    
    return answer # if answer < 1e9 else 0