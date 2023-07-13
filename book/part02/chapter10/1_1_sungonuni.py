"""
Union-Find 알고리즘을 사용한 크루스칼 알고리즘

1. 노드 개수, 간선 개수 입력받기
2. 인접리스트 정보 입력받기
3. 간선을 비용순으로 정렬
4. 모든 간선을 순회
5. 만약 간선 양 끝 노드가 사이클을 이루지 않는다면
6. 같은 부모 노드를 가지게 만들기

# 사이클 판별용 find 알고리즘
1. 만약 부모 노드가 아니라면
2. 부모 노드를 찾을 떄 까지 재귀적으로 호출

# 합치기 용 union 알고리즘
1. a의 부모 노드 찾기
2. b의 부모 노드 찾기
3. a와 b의 각 부모 노드 중 작은 것으로 통일

입력:
N, M
[인접 리스트]

예시:
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

답:
159
"""

# union 알고리즘
def union(parent, a, b):
    # a의 부모 찾아서 a에 저장
    a = find(parent, a)
    # b의 부모 찾아서 b에 저장
    b = find(parent, b)
    # a가 b보다 적다면 b 부모를 a에 저장
    if a < b:
        parent[b] = a
    # 아니면 a 부모를 b에 저장
    else:
        parent[a] = b

# find 알고리즘
def find(parent, x):
    # 만약 x가 부모 노드가 아니라면
    if parent[x] != x:    
        # x의 부모노드를 재귀로 찾기
        parent[x] = find(parent, parent[x])
    # x의 부모노드 리턴
    return parent[x]

# 노드 개수, 간선 개수 입력받기
n, m = map(int, input().split())
# 인접리스트를 3튜플로 입력받기
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))
# 부모노드 리스트 설정하기
parent = [i for i in range(n + 1)]

# 크루스칼 알고리즘 구현
# 간선을 기준으로 정렬
graph.sort()
result = 0
# 모든 간선을 순회
for e in graph:
    cost, a, b = e    
    # 만약 사이클이 만들어지지 않는다면 (a의 부모와 b의 부모가 다르다면)
    if find(parent, a) != find(parent, b):
        # a와 b 사이 union 알고리즘 실행
        union(parent, a, b)
        # 결과에 거리 누적하기
        result += cost

print(result)
