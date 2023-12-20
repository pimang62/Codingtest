# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # 누적합
    d = [0]*(len(A)+1)  # 0~7
    # [0, 4, 6, 8, 13, 14, 19, 27]
    for i in range(1, len(A)+1):
        d[i] += d[i-1] + A[i-1]

    idx = 0
    min_avg = 1e9  # 최소 average
    for k in range(2, 4):  # 2, 3만 봐주면 됨!
        for j in range(0, len(d)-k):
            avg = (d[j+k]-d[j])/k
            if min_avg > avg:
                min_avg = avg
                idx = j
    return idx