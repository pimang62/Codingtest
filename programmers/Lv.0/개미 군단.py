hp = int(input())

# 업로드 -> 런타임 에러..
def solution(hp):
    dp = [0] * (hp+1)
    for i in range(1, hp+1):
        # 초기값 설정 중요 !
        dp[1], dp[3], dp[5] = 1, 1, 1
        dp[2], dp[4] = 2, 2
        # i가 2나 4일 때 인덱싱이 -값으로 주어져서 오류 !!
        dp[i] = min(dp[i-5], dp[i-3], dp[i-1]) + 1
    return dp[hp]

print(solution(hp))