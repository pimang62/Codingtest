'''
[View]

양쪽 모두 거리 2 이상의 공간 확보될 때
조망권이 확보된 세대의 수? 

ex.
14
0 1 2                  -2 -1
0 0 3 5 2 4 9 0 6 4 0 6 0 0 

'''
# 10개의 테스트 케이스
for k in range(1, 11):
    n = int(input())
    height = list(map(int, input().split()))
    cnt = 0  # 조망권 확보된 세대 수
    for i in range(2, len(height)-2):
        left = max(height[i-2], height[i-1])
        right = max(height[i+1], height[i+2])
        if left >= height[i] or right >= height[i]:
            continue
        cnt += height[i] - max(left, right)

    print(f'#{k}', cnt) 
    
