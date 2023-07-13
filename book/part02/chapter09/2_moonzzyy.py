# 최단 경로
# N은 최대 100이므로 Floyd-Warshall 가능
# O(N^3)
# 1에서 시작하여 K 회사를 거쳐 X 회사로 가는 최소 이동 시간
# 모든 가중치=1, 무방향 그래프

import sys
input = sys.stdin.readline
INF = sys.maxsize


N, M = map(int, input().split())
d = [[INF]*(N+1) for _ in range(N+1)] # N+1 개 회사
for _ in range(M):
    a, b = map(int, input().split())
    d[a][b]=1
    d[b][a]=1
X, K = map(int, input().split())

for k in range(1,N+1):
    d[k][k]=0 # 자기자신은 0

for k in range(1,N+1): # 거쳐갈 정점
    for i in range(1,N+1):
        for j in range(1,N+1):
            # 현재 정점을 거치는 것이 더 짧으면 갱신
            if d[i][j] > d[i][k]+d[k][j]:
                d[i][j] = d[i][k]+d[k][j]

answer = d[1][K]+d[K][X]
print(-1 if answer>=INF else answer)