'''
[위상 정렬]
: 방향성에 거스르지 않도록 순서 나열
1. 진입차수(indegree)가 0인 것부터 큐에 추가
2. 노드에 연결된 간선 지움
3. 진입차수 -1
4. 진입차수 0인 것 다시 가져옴
반복) ...
'''

from collections import deque
import sys

input = sys.stdin.readline

# 노드 개수, 간선 개수
n, m = map(int, input().split())

# 간선 정보 초기화
graph = [[] for _ in range(n+1)]

# 진입차수(indegree) 초기화
indegree = [0] * (n+1)

# 간선 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입차수 : 특정 노드로 '들어오는' 간선 개수 -> a가 아니라 b !
    indegree[b] += 1

# -----------------------

# 위상 정렬 함수
def topology_sort():
    q = deque()
    result = [] 
    # 진입차수 0인 정보 추가
    for i in range(1, len(indegree)) :
        if indegree[i] == 0:
            # i번 노드 추가
            q.append((i))
    # 큐가 존재한다면
    while q:
        node = q.popleft()
        # 노드 원소 추가
        result.append(node)
        for i in graph[node]:
            # 간선 지우기
            indegree[i] -= 1
            # 다음 노드의 indegree가 새롭게 0이라면 
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()


