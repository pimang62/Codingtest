# "non-empty" array A consisting of N integers
# contains an odd number of elements
# paired with another element that has the same value,
# "except for one element" that is left "unpaired."
# returns the value of the "unpaired" element.

# 100% : O(N) or O(NlogN)
def solution(A):
    d = {}  # dictionary
    for i in range(len(A)):
        if A[i] not in d:
            d[A[i]] = 1
        else:  # if in d
            d[A[i]] -= 1  # eliminated
            if d[A[i]] == 0:
                del d[A[i]]
    
    return list(d.keys())[0]