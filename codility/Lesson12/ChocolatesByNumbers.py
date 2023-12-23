# Two positive integers N and M are given
# N represents the number of chocolates arranged in a circle, 0 to N - 1
# After eating a chocolate you leave only a "wrapper".
# begin with 0, omit the next M - 1, eat the following one : M
# X, next eat the chocolate with number (X + M)
# "stop" eating when you encounter an "empty" wrapper.
# count the "number" of chocolates that you will "eat", following the above rules. : return 5
# from math import gcd

# 100% : O(log(N+M))
def GCD(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def solution(N, M):
    tmp = GCD(N, M)
    return N//tmp