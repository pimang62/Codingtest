"""
여행가 A는 크기가 N X N인 공간에서 명령을 받아 움직이려 한다. 
명령으로 L, R, U, D를 받을 수 있다. L은 왼쪽으로 한 칸, R은 오른쪽으로 한 칸, U는 위쪽으로 한 칸, D는 아래쪽으로 한 칸을 의미한다.
단, 명령으로 인해 N x N 공간에서 벗어나게 된다면 그 명령은 무효처리 된다.
이때 명령을 모두 이행했을 때 사용자가 위치할 좌표를 출력하는 프로그램을 작성하시오.

예시:
5
R R R U D D

출력:
3 4
"""

# 시뮬레이션 문제의 프레임을 외워둘 것


# n을 입력받기
n = int(input())
x,y = 1,1
plans = list(map(str, input().split()))

# L, R, U, D에 따른 이동방향 설정
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동계획을 하나씩 확인
for plan in plans:
    
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    # 공간을 벗어나는 경우는 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    # 이동 수행
    x = nx
    y = ny

print(x, y) 




# N 입력 받기

# 이동할 수 있는 방향 정의

# 이동계획 하나씩 확인

# 이동 후 좌표 도출

# 이동 후 좌표가 범위를 벗어나면 무시

# 이동 이행