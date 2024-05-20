'''
[기상캐스터]
h by w, (i, j)로 표시
모든 구름은 1분당 1씩 동쪽으로 이동
각 구역에서 몇 분뒤 구름이 오는지 예측?
'''
h, w = map(int, input().split())
graph = [[s for s in input()] for _ in range(h)]

board = [[-1]*w for _ in range(h)]

def check():
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "c":
                return False
    return True

time = 0
while not check():
    # "c"마다 time 기록
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "c" and board[i][j] == -1:  # 첫 기록
                board[i][j] = time
    # "c" 옮기기
    for i in range(h):
        graph[i].pop()
        graph[i] = ["."] + graph[i]
    # 1초 증가
    time += 1

for i in range(h):
    print(" ".join([str(b) for b in board[i]]))