'''
[파일 합치기]
40 30 30 50

40 60 50 => 60
100 50 => 100
150 => 150
>>> 310

70 30 50 => 70
70 80 => 80
150 => 150
>>> 300 (min)

하나로 합칠 때 필요한 최소 비용?

2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32

>>>
300
864

sum_matrix
[[40, 70, 100, 150],
 [0, 30, 60, 110],
 [0, 0, 30, 80],
 [0, 0, 0, 50]

dp
[[0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]
'''
t = int(input())

for _ in range(t):
    n = int(input())
    nlist = list(map(int, input().split()))

    dp = [[0]*n for _ in range(n)]  # DP table: i~j 사이합 최솟값
    sum_matrix = [[0]*n for _ in range(n)]  # Cumulative matrix

    # 누적합 2D 배열 만들기
    for i in range(n):
        sum_matrix[i][i] = nlist[i]  # 대각 원소 초기화
        for j in range(i, n):
            sum_matrix[i][j] = sum_matrix[i][j-1] + nlist[j]
    
    # i~j 구간합 중 최솟값 판별
    for length in range(2, n+1):  # 구간의 길이
        for i in range(n-length+1):  # 4-2+1 = index 2까지는 해야
            j = i+length-1  # i: 0, j: 1(2-2+1)
            
            dp[i][j] = 1e9  # 최솟값 구해야 함
            for mid in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][mid]+dp[mid+1][j] + sum_matrix[i][j])

    print(dp[0][n-1])