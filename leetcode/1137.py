'''
[N-th Tribonacci Number]
Tn+3 = Tn + Tn+1 + Tn+2 
Given n, return the value of Tn.

0 <= n <= 37
answer <= 2^31 - 1
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return 0 if n == 0 else 1  # n==1

        d = [0]*(n+1)
        d[0], d[1], d[2] = 0, 1, 1

        if n == 2:
            return d[n]
        
        for i in range(3, n+1):
            d[i] = d[i-3] + d[i-2] + d[i-1]

        return d[n]
