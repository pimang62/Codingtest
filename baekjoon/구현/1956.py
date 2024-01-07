'''
[운동]
V개(1~V)의 마을 E개의 도로, 일방 통행
사이클을 이루는 도로 길이의 합이 최소!

3 4
1 2 1
3 2 1
1 3 5
2 3 2
'''
# 플로이드 워셜
v, e = map(int, input().split())

d = [[1e9]*(v+1) for _ in range(v+1)]  # 0-indexed

for _ in range(e):
    a, b, c = map(int, input().split())
    d[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            d[i][j] = min(d[i][j], d[i][k]+d[k][j])

answer = 1e9
for i in range(1, v+1):
    answer = min(answer, d[i][i])

print(answer if answer < 1e9 else -1) 

'''
4 5
1 2 1
2 3 1
3 4 1
4 2 2
4 1 5

[[1000000000.0, 1000000000.0, 1000000000.0, 1000000000.0, 1000000000.0], 
 [1000000000.0, 8, 1, 2, 3], 
 [1000000000.0, 7, 4, 1, 2], 
 [1000000000.0, 6, 3, 4, 1], 
 [1000000000.0, 5, 2, 3, 4]]
'''

# 다익스트라 -> 메모리 초과 [실패]
import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())

graph = [{} for n in range(v+1)]  # 1-indexed

d = [[INF]*(v+1) for _ in range(v+1)] # 0-indexed

q = []  # [(1, 1, 2), (1, 3, 2), (5, 1, 3), (2, 2, 3)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c  # [{}, {2: 1}, {3: 1}, {4: 1}, {2: 2, 1: 5}]
    d[a][b] = c  # 최초 distance 기록
    heappush(q, (c, a, b))

print(graph)

# answer = INF  # 사이클 최솟값
def dijkstra():
    while q:
        new_cost, now, nxt = heappop(q)  # 1, 1, 2
        
        if now == nxt:  # 첫 번째로 break 걸면 최소!
            return new_cost
            
        for pos, prev_cost in graph[nxt].items():  # {pos: prev_cost} in graph[2]
            tmp = new_cost + prev_cost  # 1 -> 2 -> 3 거쳐가는게 빠른지
            if d[now][pos] > tmp:  # (1 -> 3) > (1 -> 2 -> 3)
                d[now][pos] = tmp
                heappush(q, (tmp, now, pos))
    return -1

print(dijkstra())

'''
[[1000000000.0, 1000000000.0, 1000000000.0, 1000000000.0, 1000000000.0], 
 [1000000000.0, 8, 1, 2, 3], 
 [1000000000.0, 7, 4, 1, 2], 
 [1000000000.0, 6, 3, 4, 1], 
 [1000000000.0, 5, 2, 3, 4]]
'''
    