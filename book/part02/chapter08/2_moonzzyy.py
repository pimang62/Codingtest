# 1로 만들기
# 정수 X를 1로 만들 때 연산 횟수의 최솟값
# dp 구현 bottom-up
# dp[i]: i번째 연산 횟수 최솟값
# i: 1은 0, X 까지 필요
# 같은 문제: https://www.acmicpc.net/problem/1463
# 유형: https://www.acmicpc.net/problem/12852

import sys
input = sys.stdin.readline

X = int(input())
dp = [0]*(X+1)
for i in range(2, X+1):
    dp[i] = dp[i-1]+1 # -1
    if i%5==0:
        dp[i] = min(dp[i//5]+1, dp[i])
    if i%3==0:
        dp[i] = min(dp[i//3]+1, dp[i])
    if i%2==0:
        dp[i] = min(dp[i//2]+1, dp[i])

print(dp[X])