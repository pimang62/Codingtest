'''
전보를 보내고자 한다면 통로가 있어야 한다.
예를 들어 X에서 Y로 향하는 통로는 있지만, Y에서 X로 향하는 통로가 없다면 보낼 수 없다.
C라는 도시에서 메세지를 받는 도시는 총 몇 개이며, 모두 메시지를 받는데까지 걸린 시간은 얼마인지?

(입력)
N M C
X Y Z
'''

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 도시 개수, 통로 개수, 시작 위치
n, m, start = map(int, input().split())

# 간선 정보 저장
graph = [[] for i in range(n+1)]

# 간선 정보 입력받기
for _ in range(m):
    # 도시 x, 도시 y, 시간 z
    x, y, z = map(int, input().split())
    graph[x].append((z, y))

# 거리 정보 저장
distance = [INF] * (n+1)

# 다익스트라 알고리즘
def dijkstra(start):
    distance[start] = 0
    q = []
    # 첫 시작 지점
    heapq.heappush(q, (0, start))
    # 큐가 사라질 때까지
    while q:
        dist, now = heapq.heappop(q)
        # now의 시간이 이미 작다면
        if distance[now] < dist:
            continue
        # 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[0]
            # 만약 최단 시간이라면
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

dijkstra(start)

count = 0
max_time = 0
for d in distance:
    if d != INF:
        count += 1
        # INF와 비교하면 안 되므로!
        max_time = max(max_time, d)

# 자기 자신은 빼고, 최대 시간
print(count-1, max_time)




    
