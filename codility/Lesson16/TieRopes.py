# N ropes numbered from 0 to N - 1, whose "lengths" are given in an array A : the length of rope I on the line is A[I].
# two ropes I and I + 1 are "adjacent" 인접한.
# the length of the tied rope is the "sum" of lengths of both ropes.
# tie the ropes, whose length is "greater than or equal to K" is "maximal".
# "three" ropes whose lengths are greater than or equal to K = 4

# 80% : (1, [2]) = 1, 100% : O(N)
def solution(K, A):
    N = len(A)
    # if N == 0 or N == 1 and sum(A) < K
    if N < 3 and sum(A) < K:
        return 0  # no adjacent rope
    
    prev = 0  # each element [1..1000000000].
    cnt = 0  # 인접한 rope 개수 세기 
    for i in range(N):
        prev += A[i]
        if prev >= K:
            cnt += 1
            prev = 0
    return cnt