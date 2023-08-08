def solution(arr, k):
    for _ in range(k):
        
        n = len(arr)
        m = len(arr[0])
        
        row_arr = [ [] for _ in range(n) ]
        col_arr = [ [] for _ in range(n//2) ]
        
        # 가로(열)가 세로(행)보다 길면
        if m >= n:
            if n == m == 1:
                return arr
            for i in range(n):
                if m == 2:
                    row_arr[i].append(max(arr[i]))
                else:
                    for j in range(0, m, m//2):
                        row_arr[i].append(max(arr[i][j], arr[i][j+1]))
            arr = row_arr
            
        # 세로(행)이 가로(열)보다 길면
        elif n > m:
            k = 0
            while k <= n-2:
                for i in range(n//2):
                    for j in range(m):
                        col_arr[i].append(min(arr[k][j], arr[k+1][j]))
                    k += 2
            arr = col_arr
            
    return arr

print(solution(arr=[[5, 4, 8, 7], [7, 3, 1, 2], [3, 8, 12, 6], [11, 4, 5, 4]], k=4))
