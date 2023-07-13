# 도시 분할 계획
# 길을 없애고 남은 유지비의 최솟값
# MST
# MST를 찾고 가장 비용이 큰(마지막) edge 제거

import sys
input = sys.stdin.readline

def find(x): # x가 속한 팀 찾기
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]

def union_parent(a, b): # 팀 합치기
    a = find(a)
    b = find(b)
    if a<b: parent[b]=a
    else: parent[a]=b

V, E = map(int, input().split())
parent = [i for i in range(V+1)]
edges = [] # (cost, a, b)
mst = [] # mst로 선택된 edge cost list

for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort() # 비용 오름차순 정렬

for cost, a, b in edges:
    if find(a) != find(b): # 사이클이 아니면 MST에 포함
        union_parent(a, b)
        mst.append(cost)
mst.pop() # 마지막 제거
print(sum(mst))