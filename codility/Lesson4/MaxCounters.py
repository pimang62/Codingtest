# given N counters, initially set to 0
# increase(X) : X+=1, max counter : all counters are set to the maximum
# A[K] = X, 1 ≤ X ≤ N : increase(X)
# A[K] = N + 1 : K is max counter
# calculate the value of every counter after all operations.
# return [3, 2, 2, 4, 2]

# 60% : d[A[i]] += max_val, 100% : O(N+M)
def solution(N, A):
    # N, M : [1, 100000]
    # A[i] : [1, N + 1]
    d = [0]*(N+1)  # 0~6]
    max_val = 0  # update max값
    tmp = 0  # 매 구간 max값
    for i in range(len(A)):
        if A[i] == N+1:  # 6
            max_val = max(max_val, tmp)
            continue
        if d[A[i]] < max_val:
            d[A[i]] = max_val
        d[A[i]] += 1
        tmp = max(tmp, d[A[i]])

    # 마무리 더해주기
    for i in range(1, N+1):
        if d[i] < max_val:
            d[i] = max_val
    return d[1:]