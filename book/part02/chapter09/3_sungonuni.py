"""
전보

N개의 도시에는 서로 연결된 M개의 통로가 존재한다. 이중 한 개의 도시 C에서 전보를 발송하면, 연결된 모든 도시로 전보가 발송되게 된다.
전보를 받는 도시는 몇 개이며, 총 얼마나 걸리는지 계산하는 프로그램을 작성하시오.

입력:
N M C
[인접 리스트와 시간]

예시:
3 2 1
1 2 4
1 3 2
"""

# 입력받기
import heapq

INF = int(1e9)

n, m, start = map(int, input().split())
distance = [[INF] * (n + 1)]
graph = [[] for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라 알고리즘 함수
def dijkstra(start):
    # 힙큐 선언, 최초 노드 삽입, 거리 설정
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # 힙큐 순회
    while q:
        # 첫번째 노드 뽑기
        dist, now = heapq.heappop(q)
        # 만약 기존 거리가 새로운 거리보다 적다면 무시
        if distance[now] < dist:
            continue
        # 연결된 모든 노드 순회
        for j in graph[now]:
            cost = dist + j[1]
            # 만약 경유 거리가 기존 거리보다 적다면
            if cost < distance[j[0]]:
                # 기존 거리에 경유 거리를 업데이트
                distance[now] = cost
                # 힙큐에 삽입
                heapq.heappush((cost, j[0]))

dijkstra(start)

count = 0
max_dist = 0
for d in distance:
    if d != INF:
        count += 1
        max_dist = max(max_dist, d)

print(count - 1, max_dist)
