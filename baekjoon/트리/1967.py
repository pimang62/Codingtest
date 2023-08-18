'''
[트리의 지름]
어떤 두 노드를 선택해서 가장 길게 늘어나는 경우
이 두 노드를 지름의 끝 점으로 하는 원이 생김
루트(1)가 있는 트리, 가중치가 있는 간선

부모 노드가 작은 것이 먼저 입력 
부모 노드가 같으면 자식 노드가 작은 것이 먼저

입력)
n = int(input())
for _ in range(n-1):
    p, c, w = map(int, input().split())
'''

"""
from copy import deepcopy
from heapq import heapify, heappop

n = int(input())
tree = {}

for _ in range(n-1):
    p, c, w = map(int, input().split())
    if p not in tree:
        tree[p] = [(-w, c)]
    else:
        tree[p].append((-w, c))

for t in tree:
    tree[t].sort(key=lambda x: x[0])

answer = 0
for t in tree:
    result = 0
    tree_copy = deepcopy(tree)
    for _ in range(2):
        now = t
        while now in tree_copy and len(tree_copy[now]) > 0:
            weight, nxt = heappop(tree_copy[now])
            result += -1*weight
            now = nxt
    answer = max(result, answer)
            
print(answer)
"""
from heapq import heappush, heappop

def dijkstra(start):
    distance = [1e9]*(n+1)  # 최댓값에서 갱신해나가야 모두 없데이트!
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        now_weight, now = heappop(q)
        for nxt_weight, nxt in graph[now]:
            if -1*(now_weight + nxt_weight) < distance[nxt]:
                distance[nxt] = -1*(now_weight + nxt_weight)
                nxt_weight += now_weight
                heappush(q, (nxt_weight, nxt))
    return distance[1:]
                       
n = int(input())
graph = [ [] for _ in range(n+1) ]

for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append((-w, c))
    graph[c].append((-w, p))

dist1 = dijkstra(1)
nxt = dist1.index(max(dist1)) + 1 # index!
dist2 = dijkstra(nxt)
print(max(dist2))

