'''
[크루스칼 알고리즘]
<최소 신장 트리>
1. 모든 간선에 대해 오름차순 정렬 수행
2. 간선을 하나씩 확인하며 사이클을 발생시키는지 확인한다.
 - 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
 - 사이클이 발생하는 경우 최소 신장 트리에 포함 X
3. 모든 간선에 대하여 반복
'''

import sys

input = sys.stdin.readline

# 노드 개수, 간선 개수
n, m = map(int, input().split())

# 간선을 담을 리스트 선언 
edges = []

# 간선 개수에 대해 입력 받기
for _ in range(m):
    # 노드, 간선, 비용
    x, y, c = map(int, input().split())
    # 비용 순으로 정렬하기 위해
    edges.append((c, x, y))

# 간선 정렬
edges.sort()

# --------------------------------------

# 부모 테이블 초기화
parent = [0] * (n+1)

# 1~n 까지 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# 특정 원소 집합 찾기
def find_parent(parent, x):
    # 루트 노드 아니라면
    if parent[x] != x:
        # 루트 노드 찾기 위해 재귀 호출
        parent[x] = find_parent(parent, parent[x])
    # 루트 노드 반환 -> 부모 노드이므로 parent[x] !!
    return parent[x]

# 서로소 집합 만들기
def union_parent(parent, x, y):
    x = find_parent(parent, x)      # 루트 노드 찾기
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x   # 더 작은 값으로
    else:
        parent[x] = y

# --------------------------------------

# 비용 초기화 -> 다 더해서 출력
cost = 0

for edge in edges:
    # (7, 3, 4) : 작은 비용부터
    c, x, y = edge
    # 사이클이 발생하지 않을 경우에만 ex. (6, 3) & (7, 3) 수행 안함
    if find_parent(parent, x) != find_parent(parent, y):
        # 서로소 합집합 만들고
        union_parent(parent, x, y)
        # 비용 추가
        cost += c

print(cost)
