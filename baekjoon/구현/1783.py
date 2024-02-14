'''
[병든 나이트]
n by m 체스판의 가장 왼쪽 아래 칸에 위치
[(i-2, j+1), (i-1, j+2), (i+1, j+2), (i+2, j+1)]

2 4
0 0 - 0
0 0 0 0

17 5
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 - 0
0 - 0 0 -
0 0 - 0 0
0 0 0 0 0

20 4
0 0 0 0
0 0 0 0
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
0 0 0 0 
'''
n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    # 7 이하면 //2, 초과면 4가 최대
    print(min(4, (m+1)//2))
else:  # n >= 3
    if m <= 5:
        print(min(4, m))
    else:
        print(m-2)

