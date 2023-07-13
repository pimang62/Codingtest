# 팀 결성
# 같은 팀 여부 확인: YES/NO
# union_find()

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


N, M = map(int, input().split())
parent = [i for i in range(N+1)]

for _ in range(M):
    n, a, b = map(int, input().split())
    if n == 0: # 팀 합치기
       union_parent(a, b)
    else: # 같은 팀 여부
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')