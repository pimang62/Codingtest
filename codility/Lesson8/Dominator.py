# A consisting of N
# "dominator" of array A is the value that occurs in "more than half" of the elements of A.
# returns "index" of "any" element of array A in which the dominator of A occurs.
# return -1 if array A does not have a dominator.
from collections import Counter

# 100% : O(NlogN) or O(N)
def solution(A):
    N = len(A)  # [0..100,000]
    if N == 0:
        return -1
    
    d = Counter(A)
    max_val = max(d.values())  # 5
    
    # return -1 if array A does not have a dominator.
    if max_val*2 <= N:  # not max_val*2 > N
        return -1
    for k, v in d.items():  # {3: 5}
        if d[k] == max_val:
            return A.index(k)
    
    #return -1
