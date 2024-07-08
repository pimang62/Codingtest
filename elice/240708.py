"""
내일 풀 문제의 개수: 오늘 푼 문제 개수와 숫자 구성 같으면서 더 큰 수 중 가장 작은 수

1 <= N <= 999999

364 -> 436
353 -> 533
"""
N = int(input())
nlist = [n_str for n_str in str(N)]
visited = [0]*(len(nlist))

nlist.sort()

def dfs(cnt, stack: list):
    if cnt == len(nlist):
        if int(''.join(stack)) > N:
            print(int(''.join(stack)))
            exit()
        return

    for i in range(len(nlist)):
        if not visited[i]:
            stack.append(nlist[i])
            visited[i] = 1
            dfs(cnt+1, stack)
            stack.pop()
            visited[i] = 0

dfs(0, [])

