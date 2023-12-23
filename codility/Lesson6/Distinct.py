# A consisting of N integers
# returns the "number" of "distinct" values in array A.
# return 3, "distinct" values appearing in array A
# namely 1, 2 and 3 !!

from collections import Counter

# 100% : O(NlogN) or O(N)
def solution(A):
    N = len(A)  # ["0"..100,000]
    d = Counter(A)
    return len(d)