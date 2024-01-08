'''
[행렬 곱셈]
'''
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]

C = [[0]*k for _ in range(n)]

for i in range(n):  # 0
    for j in range(k):  # 0, 1, 2
        value = 0
        for l in range(m):
            value += A[i][l]*B[l][j]
        C[i][j] = value

for i in range(n):
    print(*C[i])