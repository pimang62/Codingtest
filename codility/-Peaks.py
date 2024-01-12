# index P, 0 < P < N - 1, A[P - 1] < A[P] and A[P] > A[P + 1].
# "maximum" number of blocks that array A can be divided
# "cannot" be divided into some number of blocks, the function should return 0.
# blocks containing the "same" number of elements

def solution(A):
    if len(A) < 3:  # 최소 조건
        return 0

    peak = []   # [3, 5, 10]
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] > A[i+1]:
            peak.append(i)   # index

    if len(peak) == 0:
        return 0
    if len(peak) == 1:
        return 1

    N = len(A)
    for k in range(len(peak), 0, -1):  # 3, 2, 1
        if N % k == 0:
            cnt = 0  # 매번 최대 깃발 개수 확인
            block = N // k  # 블럭 size : 4, 6, 12
            d = [0]*k  # 블럭 넘버 : 1번, 2번, 3번 상자
            for j in range(len(peak)):  # peak[0] = index 3
                idx = peak[j] // block  # 3//4(size)
                if d[idx] == 0:  # 해당 상자에 들어갈 수 있는지
                    d[idx] = 1  # d[0] = 1
                    cnt += 1
            if cnt == k:   # 다 채울 수 있다면
                return cnt