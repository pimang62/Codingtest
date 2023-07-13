"""
간단한 다익스트라 알고리즘

1. 모든 노드까지의 거리를 담은 최단거리 리스트가 존재한다. 
2. 시작점에서 다른 노드까지의 거리를 갱신한다.
3. 가장 적은 거리에 있는 노드로 이동한다 (방문처리)
4. 그 노드에서 다른 노드까지의 거리를 측정하여, 기존 거리와 누적한 거리의 크기를 비교한다. 만약 누적한 거리가 더 짧다면 그것으로 갱신한다.
5. 목적지 노드로 이동할때까지 2~5를 반복한다.

입력 예시:
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""

"""
INF = int(1e9)

# 입력받기
n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

visited = [False] * (n + 1)
distance = [INF] * (n + 1)


def get_nearest_node():
    # 가장 작은 거리의 노드 설정
    min_distance = INF
    index = 0
    # 모든 노드의 거리를 순회
    for i in range(1, n+1):
        # 만약 해당 노드의 거리가 현재까지의 최소 거리보다 작고, 아직 방문하지 않았다면
        if distance[i] < min_distance and not visited[i]:
            min_distance = distance[i]
            index = i
    return index

# 다익스트라 함수 구현
def dijkstra(start):
    # 최초 시작지점 방문처리 
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작지점을 제외한 모든 노드에 대해서 순회
    for i in range(n - 1):
        # 가장 가까운 노드 뽑아서 방문하기
        now = get_nearest_node()
        visited[now] = True
        # 그 노드에서 다른 노드까지 거리 순회
        for j in graph[now]:
            # 현재 노드를 거처서 가는 경로가 기존 경로보다 적다면 그것으로 갱신
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

print(distance)
"""

"""
개선된 다익스트라 알고리즘

BFS의 아이디어
1. 입력받기
2. 큐 선언 및 최초 노드 삽입, 최초 노드 방문처리
3. 큐 순회
4. 큐의 첫번째 요소를 뽑아서 연결된 모든 노드를 확인
5. 조건에 맞는 노드가 있다면 방문처리 후 큐에 재 삽입

힙큐 사용한 다익스트라의 아이디어
1. 입력받기
2. 힙큐 선언 및 최초 노드 삽입, 최초 노드 거리설정
3. 힙큐순회
4. 힙큐의 첫번째 요소를 뽑아서 연결된 모든 노드를 확인 (만약 기존 노드가 새 거리보다 작다면 무시)
5. 만약 경유 거리가 기존 거리보다 적다면, 기존 거리로 업데이트 후 힙큐에 재삽입
"""

"""
import heapq
# import sys
# input = sys.stdin.readline

INF = int(1e9)

# 입력 받기
n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
# 다익스트라 함수 작성
def dijkstra(start):
    # 최소힙 선언 및 시작노드 삽입
    q = []
    heapq.heappush(q, (0, start))
    # 시작노드 초기화
    distance[start] = 0
    # 큐가 비어있을 때 까지
    while q:
        # 큐에서 첫번쨰 요소 추출
        v = heapq.heappop(q)
        dist, now = v
        # 만약 첫번쨰 요소의 기존 거리가 새 거리보다 적다면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 인접 노드를 순회
        for i in graph[now]:
            cost = dist + i[1]
            # 해당 노드를 경유하는 거리가 기존 거리보다 짧다면, 기존 거리를 최산화
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 힙큐에 해당 노드 삽입
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance)
"""

"""
플로이드 워셜 알고리즘

2차원 거리행렬에서, 모든 노드를 경유하는 거리와 다이렉트 거리를 비교하기 위해 각 노드를 순회하여 검사

1. 입력받기
2. 자기 자신으로 가는 비용은 0으로 초기화
3. 각 간선에 대한 정보를 입력받아 그 값으로 초기화
4. 경유하는 노드를 설정하기 위해 모든 노드 순회
5. 출발 노드를 설정하기 위해 모든 노드 순회
6. 도착 노드를 설정하기 위해 모든 노드 순회
7. 점화식: min(직통거리, 출발-경유 거리 + 경유-도착 거리)
8. 수행된 경로 출력

입력 예시:
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""

INF = int(1e9)

# 노드 간선 개수 입력 받기
n = int(input())
m = int(input())

# 2차원 연결행렬 만들고 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 2차원 연결행렬 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 자기 자신으로 가는 거리 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 경유노드 설정용 모든 노드 순회
for k in range(1, n+1):
    # 출발노드 설정용 모든 노드 순회
    for a in range(1, n+1):
        # 도착노드 설정용 모든 노드 순회
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
print(graph)