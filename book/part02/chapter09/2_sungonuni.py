"""
미래도시

N개의 도시에 M개의 도로가 깔려있다. 모든 도로의 거리는 1로 동일하다.
1번 도시에서 출발해서 K 도시를 거쳐 X 도시로 가는 최소 거리를 구하시오

입력:
N M
[연결 도로]
X K

예시:
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

출력:
3
"""

INF = int(1e9)

# 입력받기
n, m = map(int, input().split())

# 2차원 연결행렬 INF 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 2차원 연결행렬 동일 노드 거리 0 초기화
for a in range(n + 1):
    for b in range(n + 1):
        if a == b:
            graph[a][b] = 0

# 2차원 연결행렬 입력받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# X, K 입력받기
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 구현
# K 순회
for k in range(1, n + 1):
    # A 순회
    for a in range(1, n + 1):
        # B 순회
        for b in range(1, n + 1):
            # 경유 거리가 직통 거리보다 그것을 거리로 채택
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 출력
print(graph[1][k] + graph[k][x])