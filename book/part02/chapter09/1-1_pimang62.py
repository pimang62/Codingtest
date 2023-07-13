''' 
[다익스트라 알고리즘]

<방법 1 구현하기 쉽지만 느리게 동작하는 코드>
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 무한값(int(1e9))으로 초기화 한다.
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 3과 4를 반복한다.
'''

import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값 : 10억

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())

# 출발 노드 입력 받기
start = int(input())

# 각 노드에 연결되어 있는 정보
graph = [[] for i in range(n+1)]    #0~6

# 각 노드에 연결되어 있는 모든 정보 입력받기
for _ in range(m):
    # a번 노드에 b번 노드 연결, c distance
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

# 방문 노드 테이블
visited = [False] * (n+1)   # 0~6

# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n+1)

# 방문하지 않은 노드 중에서, 최단 거리가 짧은 노드 번호 반환
def get_smallest_node():
    for i in range(1, n+1):
        if distance[i] < INF and not visited[i]:
            return i
#
def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가는 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

