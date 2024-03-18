'''
[뿌요뿌요]
중력의 영향을 받아 떨어짐
바닥이나 다른 뿌요가 나올 때까지

같은 색 뿌요가 4개 이상 상하좌우 => 1연쇄
뿌요들이 없어진 뒤 중력의 영향 다시

또 같은 색 뿌요 4개 이상이면 => 1연쇄
여러 그룹이라면 동시에 터짐

연쇄가 몇 번 연속으로 일어날지 계산!
R 빨강, G 초록, B 파랑, P 보라, Y 노랑

......
......
......
......
......
......
......
......
.Y....
..G...
RRYG..
R.YGG.
'''
from collections import deque

graph = []
for _ in range(12):
    graph.append(list(map(str, input())))

n, m = 12, len(graph[0])  # 행, 열

cnt = 0  # 몇 번 연쇄?

def pull():
    for j in range(m):
        flag = 1
        while True:
            if not flag:
                break
            flag = 0
            for i in range(n-1):
                if graph[i+1][j] == '.' and graph[i][j] != '.':
                    flag += 1
                    graph[i+1][j], graph[i][j] \
                        = graph[i][j], '.'
    """
    [['.', '.', '.', '.', '.', '.'], 
     ['.', '.', '.', '.', '.', '.'], 
     ['.', '.', '.', '.', '.', '.'], 
     ['.', '.', '.', '.', '.', '.'], 
     ['.', '.', '.', '.', '.', '.'], 
     ['.', '.', '.', '.', '.', '.'], 
     ['.', '.', '.', '.', '.', '.'], 
     ['.', '.', '.', '.', '.', '.'], 
     ['.', '.', '.', '.', '.', '.'], 
     ['.', '.', 'G', '.', '.', '.'], 
     ['R', 'Y', 'Y', 'G', '.', '.'], 
     ['R', 'R', 'Y', 'G', 'G', '.']]
    """

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(a, b):
    return 0 <= a < n and 0 <= b < m

def bfs(i, j, typ):
    path = [(i, j)]
    q = deque([(i, j)])
    
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if not in_range(nx, ny):
                continue
            if (nx, ny) not in path and graph[nx][ny] == typ:
                path.append((nx, ny))
                q.append((nx, ny))
    
    flag = False
    if len(path) >= 4:
        flag = True
        for (px, py) in path:
            graph[px][py] = '.'
    
    return flag

glob = 1
while True:
    if not glob:
        break
    glob = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != '.':
                typ = graph[i][j]
                if bfs(i, j, typ):  # 동시에 터트리기!
                    glob += 1
    if glob:
        pull()
        cnt += 1

print(cnt)