# 바닥 공사
# 가로가 N일때 바닥을 채우는 모든 경우의 수
# dp 구현 bottom-up
# dp[i]: 가로가 i일 때 경우의 수
# i=1,2 까지 초기값 필요
# 같은 문제: https://www.acmicpc.net/problem/11727
# 유형: https://www.acmicpc.net/problem/11726

import sys
input = sys.stdin.readline

N = int(input())
dp = [0, 1, 3]
for i in range(3, N+1):
    dp.append((dp[i-1]+dp[i-2]*2)%796796)

print(dp[N])