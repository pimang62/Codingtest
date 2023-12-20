# The discs are numbered from 0 to N - 1
# An array A of N non-negative integers 'radiuses' of the discs
# center at (J, 0) and radius A[J]
# returns 11 the "number" of (unordered) pairs of "intersecting" discs.
# return -1 if the number of intersecting pairs exceeds 10,000,000.

def solution(A):
    candi = []
    for i in range(len(A)):  # 6
        candi.append((i-A[i], +1, i))
        candi.append((i+A[i], -1, i))
    # [(-4, 1, 1), (-1, 1, 0), (0, 1, 2), (0, 1, 4), (1, -1, 0), (2, 1, 3), (4, -1, 2), (4, -1, 3), {(5, +1, 5), (5, -1, 5)}, (6, -1, 1), (8, -1, 4)]
    candi.sort(key=lambda x: (x[0], -x[1]))  # +1 -1
    
    answer = 0  # intersect 개수
    lines = set()
    cnt = 0
    for i in range(len(A)*2):
        v, k, l = candi[i] # value, key, line
        if k == +1:
            lines.add(l)
            cnt += 1
            if cnt > 1:
                answer += (cnt-1)  # 2 -> 1, 3 -> 2
        else:  # k == -1
            # if l in lines:
            lines.discard(l)
            cnt -= 1
    
    if answer > 1e7:  # break condition
        return -1
    return answer