'''
[N과 M (1)]
자연수 N과 M, 조건을 만족하는 길이 M 수열 모두 구하기
1부터 N까지 자연수 중 중복 없이 M개를 고른 수열

사전 순으로 증가하는 순서로 출력
'''
N, M = map(int, input().split())  # [4, 2]
A = [n for n in range(1, N+1)]  # [1, 2, 3, 4]

def dfs(cnt, arr: list):
    if cnt == M:
        print(*arr)
        return
    for i in range(N):
        if A[i] not in arr:
            arr.append(A[i])
            dfs(cnt+1, arr)
            arr.pop()
    return


dfs(0, [])  # depth, array