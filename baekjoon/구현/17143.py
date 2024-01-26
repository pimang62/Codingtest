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

# dx = [0, 1, 0, -1]  # 동남서북
# dy = [1, 0, -1, 0]
    
dx12, dy12 = [-1, 1], [0, 0]  # 북남동서
dx34, dy34 = [0, 0], [1, -1]

def in_range(a, b):
    if 0 <= a < r and 0 <= b < c:
        return True
    return False

def move():
    d = {}
    for (x, y) in shark.keys():
        v, k, l = shark[(x, y)]  # 속력, 방향, 크기
        for _ in range(v):
            if k == 1 or k == 2:
                # 방향 전환 : 전환이 틀린듯..?
                if not in_range(x+dx12[k-1], y+dy12[k-1]):
                  k = (k-1+1)%2
                nx, ny = x+dx12[k-1], y+dy12[k-1]
            elif k == 3 or k == 4:
                # 방향 전환
                if not in_range(x+dx34[k-3], y+dy34[k-3]):
                  k = (k-3+1)%2
                nx, ny = x+dx34[k-3], y+dy34[k-3]
        if (nx, ny) in d and d[(nx, ny)][-1] > l:
            continue
        d[(nx, ny)] = (v, k, l)
        x, y = nx, ny
    return d

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