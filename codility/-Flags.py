# "peak" is an array element which is "larger" than its neighbours.
# index P, 0 < P < N - 1, A[P - 1] < A[P] > A[P + 1].
# if you take "K" flags, distance between indices P and Q is the absolute value |P - Q|.
# return 3, "maximum" number of flags
# Solution: https://codility.com/media/train/solution-flags.pdf

def create_peaks(A):
    N = len(A)
    peaks = [False] * N 
    for i in range(1, N-1): 
        if A[i] > max(A[i-1], A[i+1]): 
            peaks[i] = True 
    return peaks

def next_peak(A):
    N = len(A)
    peaks = create_peaks(A)
    nxt = [0]*N
    nxt[N-1] = -1
    for i in range(N-2, -1, -1): 
        if peaks[i]:
            nxt[i] = i 
        else:
            nxt[i] = nxt[i+1]
    return nxt

# def next_peak(A):
#     # [1, 1, 3, 3, 5, 5, 10, 10, 10, 10, 10, -1]
#     nxt = [0]*len(A)
#     nxt[-1] = -1   # initialize
#     for i in range(len(A)-2, 0, -1):  # [1, N-1]
#         if A[i] > max(A[i-1], A[i+1]):    
#             nxt[i] = i
#         else:
#             nxt[i] = nxt[i+1]
#     if len(nxt) > 1:  # index 에러 방지!!
#         nxt[0] = nxt[1] # [0] = [1]
#     return nxt

def solution(A):
    N = len(A)
    nxt = next_peak(A)
    i = 1
    result = 0
    while (i - 1) * i <= N:
        pos = 0
        num = 0
        while pos < N and num < i:
            pos = nxt[pos]
            if pos == -1:
                break
            num += 1
            pos += i
        result = max(result, num)
        i += 1
    return result