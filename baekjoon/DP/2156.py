'''
[포도주 시식]
포도주 잔이 일렬로 놓임
1. 선택하면 모두 마시고, 원래 위치로
2. 연속으로 놓인 3잔은 모두 마실 수 없음

많은 양의 포도주를 맛보고 싶음
1~n개, 각 잔에 들어있는 포도주의 양

가장 많은 양의 포도주를 먹으려면?
1 <= N <= 10000

[6, 10, 13, 9, 8, 1]
'''
N = int(input())

A = []
for _ in range(N):
    A.append(int(input()))

# answer = 0  # 최대로 마실 수 있는 양

# def dfs(i, cnt, total):
#     global answer
#     if i >= N:
#         return
#     if cnt == 3:
#         return

#     answer = max(answer, total)

#     for j in range(i+1, N):
#         dfs(j, cnt+1 if j == i+1 else 1, total+A[j])

# for i in range(N):
#     dfs(i, 1, A[i])

# print(answer)

# -------------------

if N <= 2:
    print(sum(A))
    exit()

dp = [0]*N
dp[0], dp[1] = A[0], A[0]+A[1]
dp[2] = max(A[0]+A[1], A[0]+A[2], A[1]+A[2])

for i in range(3, N):
    # x o o, o x o, o o x
    dp[i] = max(dp[i-3] + A[i-1] + A[i], \
                dp[i-2] + A[i], \
                dp[i-1])  # 이전 두 개를 마신 최댓값

print(dp[N-1])