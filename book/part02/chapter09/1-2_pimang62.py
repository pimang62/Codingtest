''' 
[다익스트라 알고리즘]

<방법 2 개선된 다익스트라 알고리즘>
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 무한값(int(1e9))으로 초기화 한다.
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 3과 4를 반복한다.
'''

import heapq    # 우선순위 큐 : (거리 : 4, 노드 : 2) -> 첫 번째 원소 우선순위
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
# visited = [0] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # (거리, 노드)로 저장
    graph[a].append((c, b))

def dijkstra(start):
    q = []
    # q에다 뒤로 밀어넣기
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # q가 비어있지 않다면
    while q:
        # 최단 경로 힙큐 꺼내기
        dist, now = heapq.heappop(q)
        # 해당 경로가 이미 최단 경로면 무시
        if distance[now] < dist :
            continue
        # 현재 노드와 연결된 다른 인접 노드들 확인
        for i in graph[now]:
            cost = dist + i[0]
            # 새로 갱신한 거리가 최단 거리면
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

dijkstra(start)

# 모든 노드로 가는 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])



