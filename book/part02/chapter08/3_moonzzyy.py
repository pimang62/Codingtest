# 개미 전사
# 식량창고 N개 중 얻을 수 있는 식량의 최대
# dp 구현 bottom-up
# dp[i]: i번째까지 식량의 최대값

import sys
input = sys.stdin.readline

N = int(input())
dp = list(map(int, input().split()))
for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2]+dp[i])

print(dp[-1])