# line are N segments, 0 to N - 1
# whose positions are given in arrays A and B
# segment I is from A[I] to B[I]
# "sorted" by their ends, B[K] ≤ B[K + 1], 0 ≤ K < N - 1.
# I ≠ J, "overlapping" if they share at least one common point
# when A[I] ≤ A[J](end) ≤ B[I] or A[J] ≤ A[I](start) ≤ B[J].
# "non-overlapping" if it contains no two overlapping segments
# find the "size" of a non-overlapping set containing the "maximal" number of segments.
# returns the "size"({}, 3) of a non-overlapping set containing a "maximal"(4) number of segments.
# non-overlapping한 line set 개수가 가장 많을 때의 set size!

# 80% : prev = 0, 100% : O(N)
def solution(A, B):
    N = len(A)  # same as len(B) : [0..30,000]
    # if N == 1:
    #     return 1

    line = []
    for a, b in zip(A, B):
        line.append((a, b))
    # [(1, 5), (3, 6), (7, 8), (9, 9), (9, 10)]
    line.sort(key=lambda x: (x[1], x[0]))

    cnt = 0  # 붙일 수 있는 최대 개수
    prev = -1  # 이전 회의 끝난 시간
    for a, b in line:  # elements are [0, 1e9]
        # could start 0, end 0!
        if prev < a:  # 이전보다 내 시작 시간이 더 커야!
            cnt += 1
            prev = b
    return cnt