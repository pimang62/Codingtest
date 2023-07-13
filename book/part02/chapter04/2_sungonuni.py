"""
N x M의 크기를 가진 게임 맵이 있다. (단, N과 M은 1 이상 10000 이하의 자연수)
이 게임 맵은 육지와 바다로 이루어져 있으며, 캐릭터는 바다로 갈 수 없다.
사용자의 캐릭터는 게임 맵의 한 곳에 위치하며, 동서남북 중 한 곳을 바라본다.
캐릭터는 다음의 절차를 자동으로 이행하여 움직인다.

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향 (반시계방향으로 90도 회전)부터 갈 곳을 정한다.
2. 캐릭터의 왼쪽 방향에 가보지 않은 공간이 있다면 그곳으로 한 칸 이동한다. 없다면 그 다음 왼쪽 방향으로 회전하고 1번으로 돌아간다.
3. 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
4. 뒤쪽이 바다라서 이동할 수 없는 경우에는 움직임을 멈춘다.

다음 절차를 따라 캐릭터가 움직이다가 움직임을 멈췄을 때, 이동한 총 칸 수를 출력하는 프로그램을 작성하시오.

예시:
4 4
1 1 0
1 1 1 1
1 0 0 1 
1 1 0 1
1 1 1 1
"""



# 맵 크기 입력 받기
n, m = map(int, input().split())

# 방문한 지역 d 설정
d = [[0] * m for _ in range(n)]

# 현재 위치, 바라보는 방향 입력 받기
x, y, direction = map(int, input().split())
d[x][y] = 1

# 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 움직임 정의, 반시계방향으로 북-동-남-서
dx = [-1, 0, 1, 0]
dy = [0 , -1, 0, 1]

# 좌회전 함수 작성
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
turn_count = 0
visit_count = 0
while True:
    turn_left()
    turn_count += 1

    # 움직여보기 (커서 설정)
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 만약 가보지 않았고 육지라면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 1:
        x = nx
        y = ny
        d[nx][ny] = 1
        visit_count += 1
    # 그렇지 않다면 한번 더 회전
    else:
        continue
    # 만약 360도 돌았다면 뒤로가기
    if turn_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_count = 0

print(visit_count)