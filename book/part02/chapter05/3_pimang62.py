n, m = map(int, input().split())

# mapping하기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정 노드를 방문한 뒤에 연결된 모든 노드들 방문
def dfs(x, y):
    # 주어진 범위 벗어나는 경우 불가
    if x<=-1 or x>=n or y<=-1 or y>=m :    # 0~14, 0~13 까지 일테니
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)     # 상
        dfs(x+1, y)     # 하
        dfs(x, y-1)     # 좌
        dfs(x, y+1)     # 우
        return True
    # default
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

