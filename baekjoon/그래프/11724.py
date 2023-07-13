'''
[연결 요소의 개수]
방향 없는 그래프, 연결 요소의 개수?

입력)
n, m = map(int, input().split())
for _ in range(m):
    u, v = map(int, input().split())

풀이)
- 서로소 집합 알고리즘
- BFS

'''

'''
# pypy3 통과
# 서로소 집합 알고리즘 & set 구조
n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_find(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    u, v = map(int, input().split())
    union_find(parent, u, v)

# 인덱스가 자기 자신과 같을 경우가 root
root = 0
for i in range(1, len(parent)):
    if i == parent[i]:
        root += 1

print(root)  # 0은 제외
'''

# DFS
n, m = map(int, input().split())

graph = [ [] for _ in range(n+1) ] 
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 무방향 노드

# 방문 기록
visited = [0] * (n+1)

def dfs(visited, i):
    visited[i] = 1
    for j in graph[i]:
        if not visited[j]:
            dfs(visited, j)
    return 

cnt = 0
# 모든 노드들에 대하여
for i in range(1, n+1):
    if not visited[i]:
        dfs(visited, i)
        cnt += 1

print(cnt)

# 시간 초과
# BFS
from collections import deque 

def bfs(visited, i):
    q = deque([i])
    visited[i] = 1
    while q:
        for j in graph[i]:
            if not visited[j]:
                q.append(j)
                visited[j] = 1
    return

cnt = 0
# 모든 노드들에 대하여
for i in range(1, n+1):
    if not visited[i]:
        bfs(visited, i)
        cnt += 1

print(cnt)