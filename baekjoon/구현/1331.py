'''
[나이트 투어]
https://www.acmicpc.net/problem/1331

체스판에서 나이트가 모든 칸을 정확히 한 번
마지막 방문 칸에서 시작점으로 돌아오는 경로

6 by 6 체스판, 또 다른 나이트 투어 경로
A-F, 1-6 / 올바르면 Valid, 아니면 Invalid
'''

graph_map = {
    'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5,
    '6':0, '5':1, '4':2, '3':3, '2':4, '1':5
}

dx = [-1, -2, -2, -1, +1, +2, +2, +1]
dy = [-2, -1, +1, +2, -2, -1, +1, +2]

def transform(i):
    return graph_map[i]

x, y = None, None  # 앞 지점
lx, ly = 0, 0  # 처음이자 마지막 지점
visited = [[0]*6 for _ in range(6)]

answer = True

for _ in range(36):
    inp = input()
    if not answer:
        continue
    tx, ty = transform(inp[0]), transform(inp[1])
    if (x, y) == (None, None):
        x, y = tx, ty  # 첫 지점
        lx, ly = tx, ty
        continue
    flag = False
    for k in range(8):
        nx, ny = x+dx[k], y+dy[k]
        if (tx, ty) == (nx, ny):
            flag = True
    if not flag or visited[tx][ty]:
        answer = False
    x, y = tx, ty
    visited[tx][ty] = 1

def last_pang():
    for k in range(8):
        nx, ny = x+dx[k], y+dy[k]
        if (nx, ny) == (lx, ly) and not visited[nx][ny]:
            return 'Valid'
    return 'Invalid'

if not answer:
    print('Invalid')
else:
    print(last_pang())
