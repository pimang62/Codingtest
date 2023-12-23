# positive integer D, "factor" of positive integer N, N = D * M. if there exists an integer M
# returns the "number" of its factors.
from math import sqrt

# 100% : O(sqrt(N))
def solution(N):
    cnt = 0  # 약수 개수
    for i in range(1, int(sqrt(N))+1):  # if N = 4, 
        if N % i == 0:
            cnt += 2
    if N % sqrt(N) == 0: # 2 두번 더해짐
        cnt -= 1
    return cnt