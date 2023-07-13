'''
[플로이스 워셜 알고리즘]
공중 미래 도시에는 1번부터 n번까지의 회사가 있다.
특정 회사끼리는 서로 도로를 통해 연결되어 있다.
1번 회사에서 출발하여 K번 회사를 방문하고 X번 회사로 간다.
'''

# 노드 개수, 간선 개수
n, m = map(int, input().split())

# 무한 수 지정
INF = int(1e9)

# 2차원 그래프
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신을 거칠 때에는 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b :
            graph[a][b] = 1

# 서로에게 가는 길 1로 업데이트
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b], graph[b][a] = 1, 1

# 목적지 X, 거쳐갈 노드 K
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과물
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print('-1')
else:
    print(distance)

