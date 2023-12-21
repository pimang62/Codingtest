# *"dominator" of array A is the value that occurs in "more than half" of the elements of A.
# returns "index" of any element of array A in which the "dominator" of A occurs.
# The function should return -1 if array A "does not have" a dominator.
# dominator of array A is the value that occurs in "more than" half of the elements of A.
from collections import Counter

def solution(A):
    # Counter({3: 5, 4: 1, 2: 1, -1: 1})
    total = Counter(A)

    key, max_val = 0, 0  # 3
    for k, v in total.items():  # 정렬: NlogN > N!!
        if v > max_val:
            key = k
            max_val = v
    
    if 2*max_val > len(A):  # max_val == len(A)/2
        return A.index(key)  # 찾기 but 앞에서 끊기: less than N
    else:
        return -1


    



