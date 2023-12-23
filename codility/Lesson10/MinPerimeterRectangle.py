# integer N is given, representing the area of some "rectangle"
# area of a rectangle whose sides are of length A and B is A * B, "perimeter" is 2 * (A + B)
# find the "minimal" perimeter of any rectangle
# 30 : 1 2 3 (5 6) 10 15 30
# returns the "minimal" perimeter of any rectangle whose "area" is exactly equal to "N" : 약수들 
# 4 : 1 (2) 4
# 36 : 1 2 3 4 (6) 9 
# 10 : 1 (2 5) 10
# 26 : 1 2 13 26

from math import sqrt

# 100% : O(sqrt(N))
def solution(N):
    # [1..1000000000]
    tmp = int(sqrt(N))  # 10 : 3, 4 : 2
    for i in range(tmp, 0, -1):  # tmp~1]
        if N % i == 0:
            return 2*(i + (N//i))