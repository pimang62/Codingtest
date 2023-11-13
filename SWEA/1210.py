'''
[Ladder1]
동, 남, 서 방향으로만
첫 위치는 첫 row에 1 적힌

1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 0 0 1
1 1 1 1 1 0 1 0 0 1
1 1 1 1 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 2
'''
# from collections import deque

for _ in range(10):
    t = int(input())  # 1
    # 1 + 100 by 100! + 1 : 충돌 방지 범퍼
    graph = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
    
    #     동 북 서
    dx = [0, -1, 0]  
    dy = [1, 0, -1]

    ex, ey = 0, 0  # 끝지점(2) 기록
    for j in range(102):
        if graph[-1][j] == 2:
            ex, ey = 99, j
            break

    # def in_range(nx, ny):
    #     if 0 <= nx < 13 and 0 <= ny < 10:
    #         return True
        
    k = 1  # 별일 없으면 북쪽
    nx, ny = ex, ey  # 초기화
    while True:
        if nx == 0:
            break
        
        if graph[nx][ny+1]:  # 동쪽
            k = 0
            while True:
                nx += dx[k]
                ny += dy[k]
                if graph[nx][ny+1] == 0:
                    break
        
        elif graph[nx][ny-1]:  # 서쪽
            k = 2
            while True:
                nx += dx[k]
                ny += dy[k]
                if graph[nx][ny-1] == 0:
                    break
        
        # 별일 없으면 북쪽
        k = 1
        nx += dx[k]
        ny += dy[k]
    
    print(f'#{t} ' + str(ny-1))  # 앞에 범퍼 [0]
        
    