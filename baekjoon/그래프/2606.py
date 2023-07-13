'''
[바이러스]
연결되어 있는 컴퓨터들은 바이러스에 걸린다.
1번 컴퓨터를 통해 바이러스에 걸린 컴퓨터의 수?

입력)
n = int(input())
m = int(input())

graph = [ [] for _ in range(n+1) ]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

주의)
양방향 노드임!!
'''

n = int(input())
m = int(input())

graph = [ [] for _ in range(n+1) ]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 감염여부
virus = [0] * (n+1)
virus[1] = 1

# 감염카운트
cnt = 0

from collections import deque

q = deque([1])
while q:
    now = q.popleft()
    for nxt in graph[now]:
        if virus[nxt] == 0:
            q.append(nxt)
            # 감염시키기
            virus[nxt] = 1
            cnt += 1

print(cnt)


