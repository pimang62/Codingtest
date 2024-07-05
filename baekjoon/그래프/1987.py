'''
[알파벳]
https://www.acmicpc.net/problem/1987

R by C, 대문자 알파벳이 하나씩, 1행 1열 말
새로 이동한 칸 not in 지나온 모든 칸 알파벳

말이 최대 몇 칸 지날 수 있는지? cnt 1부터
1 <= R, C <= 20
'''
R, C = map(int, input().split())
graph = [input() for _ in range(R)]

x, y = 0, 0  # 1행 1열
answer = 0  # 최대 칸 수
path = []  # 지나온 알파벳

dx = [0, 1, 0, -1]  # 동남서북
dy = [1, 0, -1, 0]

def in_range(a, b):
    """범위에 있는지 보는 함수"""
    return 0 <= a < R and 0 <= b < C


def dfs(i, j, path: set):
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
    
    # 이번 값 내려놓기
    path.remove(graph[i][j])

dfs(0, 0, set())  # (0, 0)에서 시작, no path
print(answer)