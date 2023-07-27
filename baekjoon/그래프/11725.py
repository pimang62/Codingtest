'''
[트리의 부모 찾기]
루트 없는 트리
트리의 루트 1 각 노드의 부모?

나를 선사하노라~!

입력)
import sys
input = sys.stdin.readline

n = int(input())
graph = [ [] for _ in range(n) ]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b)
    graph[b-1].append(a)

'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)    # !!

from collections import deque

n = int(input())
graph = [ [] for _ in range(n) ]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b)
    graph[b-1].append(a)

node = [0]*(n+1)   # 1-indexed

def bfs():
    q = deque([1])
    node[1] = 1
    while q:
        now = q.popleft()
        for nxt in graph[now-1]:  # 1-indexed
            if node[nxt] == 0:
                node[nxt] = now     # 4에 1 넣기
                q.append(nxt)

def dfs(now):
    for nxt in graph[now-1]:
        if node[nxt] == 0:
            node[nxt] = now
            dfs(nxt)

dfs(1)

for i in range(2, n+1):
    print(node[i])

