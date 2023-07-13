''' DFS '''

import numpy as np

# 방문 기록 남기기
visited_array = np.zeros(9)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# DFS 매서드 정의
def dfs(graph, v, visited_array):
    # 현재 노드 방문 처리
    visited_array[v] = 1
    # 경로 첫 번째
    print(v, end=' ')
    for i in graph[v]:
        # 한 번도 방문한 적 없다면 수행
        if visited_array[i] == 0:
            dfs(graph, i, visited_array)

dfs(graph, 1, visited_array)



''' BFS '''

import numpy as np
from collections import deque

# 방문 기록 남기기
visited_array = np.zeros(9)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# BFS 매서드 정의
def bfs(graph, start, visited_array):
    queue = deque([start])      # deque 자료형 : deque([1, 2, ...])
    # 방문 처리
    visited_array[start] = 1
    # 큐가 빌 때까지 반복
    while queue:
        # 제일 왼쪽 뽑기
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            # 방문 안했다면 수행
            if visited_array[i] == 0:
                queue.append(i)
                # 방문 처리
                visited_array[i] = 1

bfs(graph, 1, visited_array)
