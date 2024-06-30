'''
[거북이]
https://www.acmicpc.net/problem/8911

2차원 평면 위에서 움직이는 거북이 로봇

1. F: 한 눈금 앞으로
2. B: 한 눈금 뒤로
3. L: 왼쪽으로 90도(방향만): -1
4. R: 오른쪽으로 90도(방향만): +1

거북이가 이동한 영역을 계산하려함
지나간 영역을 모두 포함하는 가장 작은 직사각형의 넓이?

직사각형을 만들지 않는 경우(y축 위로만 지나다니거나) 넓이는 0
'''
T = int(input())

dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}  # 동남서북

for _ in range(T):
    string = input()
    
    k = 0  # 북쪽
    x, y = 0, 0

    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    
    for i in range(len(string)):
        if string[i] == "F":
            dx, dy = dirs[k]
            x += dx; y += dy
            min_x, max_x = min(min_x, x), max(max_x, x)
            min_y, max_y = min(min_y, y), max(max_y, y)
        elif string[i] == "B":
            dx, dy = dirs[k]
            x -= dx; y -= dy
            min_x, max_x = min(min_x, x), max(max_x, x)
            min_y, max_y = min(min_y, y), max(max_y, y)
        elif string[i] == "L":
            k = (k-1) % 4
        elif string[i] == "R":
            k = (k+1) % 4

    print((max_x - min_x) * (max_y - min_y))
