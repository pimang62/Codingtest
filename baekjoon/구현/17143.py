'''
[낚시왕]
r 행, c 열
칸에는 상어가 최대 한 마리
상어는 크기와 속도를 가짐

1. 낚시왕이 오른쪽으로 한 칸
2. 열에 있는 상어 중 땅과 제일 가까운 상어 잡음 -> 상어 사라짐
3. 상어 이동

상어가 이동하려는 칸이 경계를 넘으면 -> 방향 반대 속력 유지
한 칸에 상어가 두 마리 이상 있으면 -> 크기가 큰 상어만 남음

d: 1 북 2 남 3 동 4 서

  0 1 2 3 4 5
0 
1 
2 
3 

'''
r, c, m = map(int, input().split())  # r, c, 상어 수

shark = {}  # {(0, 0): (s, d, z), ...}
for _ in range(m):
    i, j, s, d, z = map(int, input().split())  # (위치, 속력, 방향, 크기)
    shark[(i-1, j-1)] = (s, d, z)

dx = [-1, 1, 0, 0]  # 북남동서
dy = [0, 0, 1, -1]

def in_range(a, b):
    if 0 <= a < r and 0 <= b < c:
        return True
    return False

def move():
    global shark
    new_shark = {}
    for (x, y), (v, k, l) in shark.items():
        if k <= 2:  # 상하 이동
            divider = (r - 1) * 2
        else:  # 좌우 이동
            divider = (c - 1) * 2
        
        v %= divider  # (이제) 움직일 값 / 제자리
        
        for _ in range(v):
            # 방향 전환
            """
            if not in_range(nx, ny):
                # 1<->2, 3<->4 (?)
                direction = 3 - direction if direction < 3 else 7 - direction
                nx, ny = x + dx[direction-1], y + dy[direction-1]
            x, y = nx, ny
            """
            if k == 1:
                if not in_range(x+dx[k-1], y+dy[k-1]):
                    k = 2  # 1 -> 2 
            elif k == 2:
                if not in_range(x+dx[k-1], y+dy[k-1]):
                    k = 1  # 2 -> 1
            elif k == 3:
                if not in_range(x+dx[k-1], y+dy[k-1]):
                    k = 4  # 3 -> 4
            else:  # k == 4
                if not in_range(x+dx[k-1], y+dy[k-1]):
                    k = 3  # 4 -> 3
            nx, ny = x+dx[k-1], y+dy[k-1]
            x, y = nx, ny  # 계속 움직임
        if (x, y) in new_shark and new_shark[(x, y)][-1] > l:
            continue
        new_shark[(x, y)] = (v, k, l)
        
    return new_shark

if __name__ == '__main__':
    answer = 0  # 잡은 상어 크기의 합
    for j in range(c):  # 사람 index
        # 열에서 가장 가까운 상어 찾기
        for i in range(r):  # 가장 가까운 index
            if (i, j) in shark:
                answer += shark[(i, j)][-1]  # 크기 더하기
                del shark[(i, j)]
                break
        shark = move()

    print(answer)