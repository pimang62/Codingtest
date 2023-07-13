# 전보
# N은 최대 30000, M은 최대 200000이므로 Dijkstra
# O(MlogN)
# C에서 보낸 메시지를 받는 도시와 걸리는 시간

from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = sys.maxsize


N, M, C = map(int, input().split())
graph = [[] for _ in range(N+1)] # N+1 개 도시 edge
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((w,b)) # 가중치를 앞에하여 가중치 작은 순으로 정렬됨
d = [INF] * (N+1) # C에서 다른 도시까지의 거리

pq = []
d[C] = 0
heappush(pq, (0, C))  # (w, v)
while pq:
    w, v = heappop(pq)
    # 현재 정점에 대한 가중치가 다르면 넘어감
    if d[v] != w: continue
    for nxt_w, nxt_v in graph[v]:
        # 현재 정점을 거치는 것이 더 작으면 갱신
        if d[nxt_v] > d[v] + nxt_w:
            d[nxt_v] = d[v] + nxt_w
            heappush(pq, (d[nxt_v], nxt_v))  # (w, v)
count = []
for dist in d[1:]:
    if dist!=INF:
        count.append(dist)
print(len(count)-1, max(count)) # 자기자신 제외