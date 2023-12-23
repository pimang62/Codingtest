# get to the other side of a river.
# initially located on (position 0), get to the opposite bank (position X+1)
# A[K] represents the position where one leaf "falls" at time K
# find the "earliest" time when the frog can jump to the other side of the river.
# cross only when leaves appear at every position across the river from "1 to X" are "covered" by leaves
# leaves do not change their positions
# returns the "earliest" time when the frog can jump to the other side of the river.
# never able to jump, should return "-1"
# 1부터 X까지 모든 숫자가 한 번 이상 나타나는 최초의 시간 K(index)

# 100% : O(N)
def solution(X, A):
    N = len(A)  # [1..100,000]
    sets = set()
    for i in range(N):
        if A[i] not in sets:
            sets.add(A[i])
            if len(sets) == X:  # [1..X]
                return i
    # never able to jump, should return "-1"
    return -1