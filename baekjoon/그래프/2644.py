'''
[촌수계산]
부모 자식들간의 관계가 주어짐
촌수를 계산?

나-아버지 1촌 아버지(아버지 형제들)-할아버지 1촌
나-할아버지 2촌 나-아버지 형제들 3촌
아버지-아버지 형제들 2촌

'''

n = int(input())  # 사람들 1~n
a, b = map(int, input().split())

m = int(input())  # 부모 자식들 관계 개수
# [[], 1:[2, 3], 2:[1, 7, 8, 9], 3:[1], 4:[5, 6], 5:[4], 6:[4], 7:[2], 8:[2], 9:[2]]
relations = [ [] for _ in range(n+1) ]
for _ in range(m):
    x, y = map(int, input().split())  # x가 y의 부모
    relations[x].append(y)
    relations[y].append(x)

visited = [0] * (n+1)

def dfs(now, cnt):
    global result
    if now == b:  # target
        result = max(result, cnt)
        return
    visited[now] = 1
    for nxt in relations[now]:
        if not visited[nxt]:
            visited[nxt] = 1
            dfs(nxt, cnt+1)

result = 0  # 촌수 계산
dfs(a, 0)  # cnt = 0
print(result if result > 0 else -1)