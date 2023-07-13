'''
[설탕 배달]
n킬로그램 배달, 3kg & 5kg 봉지
최대한 적은 봉지!!

'''

n = int(input())

dp = [1e9] * (n+3)  # 3 <= n
dp[3] = dp[5] = 1   # 초기화

for i in range(6, n+1):     # index 에러 방지
    dp[i] = 1 + min(dp[i-3], dp[i-5])

if dp[n] < 1e9:
    print(dp[n])
else:   # 1e9 이상
    print(-1)
