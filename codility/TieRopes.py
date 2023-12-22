# N ropes numbered from 0 to N - 1
# I (0 ≤ I < N), the length of rope I on the line is A[I].
# two ropes I and I + 1 are "adjacent" : 인접한
# the length of the tied rope is the "sum" of lengths of both ropes
# greater than or equal to K is maximal. >= K
# "3" ropes whose lengths are greater than or "equal" to K = 4
# returns the "maximum" number of ropes of "length" greater than or equal to "K"

def solution(K, A):
    N = len(A)
    summ = 0  # 구간합
    cnt = 0  # 최종 개수
    for i in range(N):
        summ += A[i]
        if summ >= K:
            cnt += 1
            summ = 0  # reset
    return cnt