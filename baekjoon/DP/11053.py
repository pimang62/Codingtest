'''
[가장 긴 증가하는 부분 수열]
a = [10, 20, 10, 30, 20, 50] 
10 20 30 50 : 4

입력)
import sys
input = sys.stdin.readline

n = int(input())
table = list(map(int, input().split()))
'''
import sys
input = sys.stdin.readline

n = int(input())
table = list(map(int, input().split()))

d = [1]*n

for i in range(n):
    value = table[i]
    for j in range(i):
        if table[j] < value:
            d[i] = max(d[i], d[j]+1)

print(max(d))
        
# 다른 사람의 풀이
n = int(input())
a = list(map(int, input().split()))
dp = [1 for _ in range(n)]

# dp[i] = dp[0]~dp[i-1] 중 a의 값은 a[i]보다 작으면서 dp의 값은 가장 큰 값 + 1

for i in range(1, n):
    curr = a[i]
    for j in range(i-1, -1, -1):
        if curr > a[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(max(d))
