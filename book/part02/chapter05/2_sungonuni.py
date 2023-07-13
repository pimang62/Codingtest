from collections import deque

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 첫번째 노드 방문처리 및 출력
    visited[v] = True
    print(v, end=" ")

    # 첫번째 노드와 연결된 모든 노드 순회
    for i in graph[v]:
        # 만약 방문 안 했다면 dfs
        if visited[i] == False:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    # 큐 선언, 첫번째 노드 삽입, 방문처리
    queue = deque()
    queue.append(start)
    visited[start] = True

    # 큐 순회 시작
    while queue:
        # 첫번째 노드 뽑아서 출력
        v = queue.popleft()
        print(v, end=" ")
        # 첫번쨰 노드와 연결된 모든 노드 순회
        for i in graph[v]:
            # 만약 방문 안 했다면 큐에 추가 후 방문처리
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

# 2차원 연결리스트
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 1차원 방문리스트
visited = [False for _ in range(len(graph))]

# DFS 함수 호출
dfs(graph, 1, visited)
print()

# 2차원 방문리스트
visited = [False for _ in range(len(graph))]
bfs(graph, 1, visited)
print()