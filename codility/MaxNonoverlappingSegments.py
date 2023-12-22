# N segments, numbered from 0 to N - 1
# 0 ≤ I < N, A[I] to B[I] (inclusive)
# segments are sorted by their ends B[K] ≤ B[K + 1], 0 ≤ K < N - 1
# "overlapping" if they "share at least one common point."
# I ≠ J, A[I] ≤ A[J] ≤ B[I] or A[J] ≤ A[I] ≤ B[J].
# find the size of a "non-overlapping", "maximal" number of segments.
# returns the size of a non-overlapping set, containing a "maximal" number of segments.
# just 회의실 문제..

def solution(A, B):
    # [0..30,000]
    N = len(A)  # same as len(B)
    if N == 0:
        return 0
    # if N == 1:
    #     return 1  # 뒤에 cnt로 커버 가능

    lines = []
    for i in range(N):
        lines.append((A[i], B[i]))  # (start, end)

    # [(1, 5), (3, 6), (7, 8), (9, 9), (9, 10)]
    lines.sort(key=lambda x: (x[1], x[0]))  # 끝점 기준 정렬
    
    prev_ending = lines[0][1]  # first ending
    cnt = 1  # 최대 개수
    for i in range(1, N):
        if lines[i][0] <= prev_ending:  # 아직 끝나지 않았다면면
            continue
        else:  # prev_ending < lines[0] 
            cnt += 1
            prev_ending = lines[i][1]
    return cnt
