from collections import deque

n, m = map(int, input().split())
graph = [[s for s in input()] for _ in range(n)]

q = deque()
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

def init():
    rx, ry, bx, by = 0, 0, 0, 0 # 초기화 
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'R':
                rx, ry = i, j
            elif graph[i][j] == 'B':
                bx, by = i, j
    q.append((rx, ry, bx, by, 1)) # 위치 정보와 depth
    visited[rx][ry][bx][by] = True

dx = [0, 1, 0, -1]  # 동남서북
dy = [1, 0, -1, 0]

def move(x, y, dx, dy):
    dist = 0 # 이동한 칸 수 ('R'과 'B'가 겹칠 때 활용할 것임)
    # 다음 이동이 벽이거나 구멍일 때까지
    while graph[x+dx][y+dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        dist += 1
    return x, y, dist
    
def bfs():
    init()
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10: # 10 이하여야 한다.
            return -1
        for k in range(4): # 4방향으로 시도한다.
            nrx, nry, dr = move(rx, ry, dx[k], dy[k]) # RED
            nbx, nby, db = move(bx, by, dx[k], dy[k]) # BLUE
            if graph[nbx][nby] == 'O': # 파란 구슬이 구멍에 떨어지면(실패)
                continue
            if graph[nrx][nry] == 'O': # 빨간 구슬이 구멍에 떨어진다면(성공)
                return depth
            if nrx == nbx and nry == nby : 
                if dr > db: # 이동 거리가 많은 구슬을 한칸 뒤로
                    nrx -= dx[k]
                    nry -= dy[k]
                else:
                    nbx -= dx[k]
                    nby -= dy[k]
            # BFS 탐색을 마치고, 방문 여부 확인
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, depth+1))
     
    return -1  # 실패
     
print(bfs())