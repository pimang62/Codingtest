n, m = map(int, input().split())

x, y, direction = map(int, input().split())

# 방문한 위치 저장
d = [[0] * m for _ in range(n)]     # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# 현재 위치 방문
d[x][y] = 1

# 한 줄씩 업데이트
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로(반시계 방향) 틀기
def turn_left():
    global direction
    direction -= 1
    # 3 -> 2, 2 -> 1, 1 -> 0, 0 -> 3 !
    if direction == -1:
        direction = 3
    
# 시뮬레이션
count = 1
turn_time = 0
while True :
    turn_left()
    nx = x + dx[direction]      # dx[3] 서쪽으로 1칸 준비
    ny = y + dy[direction]      # dy[3]
    
    # 방문한 위치 아닐 경우 & 육지일 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        # 방문 표시
        d[nx][ny] == 1
        # 좌표 이동
        x, y = nx, ny
        count += 1
        # turn_time == 4일 때를 대비하여
        turn_time = 0
        continue
   
    # 방문한 위치이거나 바다일 경우
    else :
        turn_time += 1

    # 어떠한 방향으로도 갈 수 없을 때
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 육지일 경우
        if array[nx][ny] == 0 :
            x, y = nx, ny
        # 바다일 경우
        else:
            break
        turn_time = 0

print(count)
