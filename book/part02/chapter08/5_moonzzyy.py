# 효율적인 화폐 구성 (어려움)
# M원을 만들기 위한 최소한의 화폐 개수
# dp[i]: i 금액의 최소 화폐 개수

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
dp = [1e9]*(M+1)
dp[0]=0
for n in arr: # 화폐 종류마다 반복
    for i in range(n, M+1):
        if dp[i-n]!=1e9: # 방법 존재
            dp[i] = min(dp[i], dp[i-n]+1)

print(dp[M] if dp[M]!=1e9 else -1)