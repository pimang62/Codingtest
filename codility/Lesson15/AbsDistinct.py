# "non-empty" array A consisting of N is given
# sorted in non-decreasing order. : 오름차순
# "absolute distinct" count of this array is the "number" of distinct absolute values among the elements of the array.
# return 5

# 0% : del & list(d.keys())[0], 100% just len(d) : O(N) or O(NlogN)
def solution(A):
    N = len(A)  # [1..100000]
    d = {}
    for i in range(N):
        tmp = abs(A[i])
        if tmp not in d:
            d[tmp] = 1  # just 1
    
    return len(d)