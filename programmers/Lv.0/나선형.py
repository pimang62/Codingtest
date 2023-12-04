def solution(n):
    answer = [[0]*n for _ in range(n)]
    answer[0] = [i for i in range(1, n+1)]   # initialize

    x, y = 0, n-1  # start 
    
    dx = [1, 0, -1, 0]  # 남서북동
    dy = [0, -1, 0, 1]
    
    num += 1  # 5 / 6
    for d in range(n-1, 0, -2):  # 3, 1 / 4, 2
        for k in range(4):
            if k < 2:  # 남서: d
                for _ in range(d):
                    nx, ny = x+dx[k], y+dy[k]
                    answer[nx][ny] = num
                    num += 1
                    x, y = nx, ny
            elif k >= 2:  # 북동: d-1
                for _ in range(d-1):
                    nx, ny = x+dx[k], y+dy[k]
                    answer[nx][ny] = num
                    num += 1
                    x, y = nx, ny
    
    return answer

print(solution(4))