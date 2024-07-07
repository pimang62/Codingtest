'''
[설탕 배달]
N킬로그램 배달해야
3kg, 5kg 봉지 있음

최대한 "적은" 봉지
정확히 N킬로그램 만들 수 없으면 -1

배달하는 봉지의 최소 개수?

3 <= N <= 5000
'''
N = int(input())

dp = [1e9] * (N+3)  # if N == 3, 5 존재해야
dp[3], dp[5] = 1, 1

for i in range(6, N+1):  # N까지만
    dp[i] = min(dp[i-3], dp[i-5]) + 1

# not dp[N] != 1e9, < 1e9! (ex. 1e9+1)
print(dp[N] if dp[N] < 1e9 else -1)