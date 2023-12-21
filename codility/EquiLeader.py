# "leader" of this array is the value that occurs in more than half of the elements of A.
# "equi leader" is an index S
# count the number of equi leaders.
from collections import Counter

def solution(A):
    bro = Counter(A)  # total count

    key, max_val = 0, 0  # 4, _
    for k, v in bro.items():
        if v > max_val:
            max_val = v
            key = k

    N = len(A)
    cnt = 0  # 가능한 경우의 수

    chi = Counter()
    for i in range(len(A)-1):
        chi[A[i]] += 1
        bro[A[i]] -= 1
        # (i+1): 1~ 리스트 길이! 
        if 2*chi[key] > (i+1) and 2*bro[key] > (N-1-i):
            cnt += 1
        # print(chi, bro)
    
    return cnt
