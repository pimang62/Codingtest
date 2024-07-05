'''
[알파벳]
https://www.acmicpc.net/problem/1987

R by C, 대문자 알파벳이 하나씩, 1행 1열 말
새로 이동한 칸 not in 지나온 모든 칸 알파벳

말이 최대 몇 칸 지날 수 있는지? cnt 1부터
1 <= R, C <= 20
'''
R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input()))

answer = 0  # 최대 칸 수
path = set()  # 지나온 알파벳

dx = [0, 1, 0, -1]  # 동남서북
dy = [1, 0, -1, 0]

def in_range(a, b):
    """범위에 있는지 보는 함수"""
    return 0 <= a < R and 0 <= b < C

def _dfs(i, j, path: set):
    """Backtracking 함수"""
    global answer
    # 범위에 없거나 path에 있다면 return
    if not in_range(i, j) or graph[i][j] in path:
        answer = max(answer, len(path))
        return
    
    # 범위에 있고 path에 없다면 추가
    path.add(graph[i][j])
        
    for k in range(4):  # 방향 설정
        nx, ny = i+dx[k], j+dy[k]
        # dfs 탐색
        dfs(nx, ny, path)
    # dfs(i, j+1, path)
    # dfs(i+1, j, path)
    # dfs(i, j-1, path)
    # dfs(i-1, j, path)
    
    # 이번 값 내려놓기
    path.remove(graph[i][j])


def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 이걸 이렇게 해야 맞음.. in_range 사용 X
        if 0 <= nx and 0 <= ny and nx < R and ny < C and graph[nx][ny] not in path:
            path.add(graph[nx][ny])
            dfs(nx, ny, cnt+1)
            path.remove(graph[nx][ny])

path.add(graph[0][0])
dfs(0, 0, 1)
print(answer)