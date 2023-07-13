'''
[부녀회장이 될테야]
a층 b호는 (a-1)층의 1호부터 b호까지 사람들의 수의 합
각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

k층 n호에는 몇 명이 살고 있는지?

입력)
t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
'''

for _ in range(t):
    k = int(input())    # 1층
    n = int(input())    # 3호
    
    d = [ [0]*(n+1) for _ in range(k+1) ]      # +1
    d[0] = [ i for i in range(n+1) ]    # 초기화
    
    for i in range(1, k+1):
        for j in range(n+1):
            d[i][j] = sum(d[i-1][:j+1])
    
    print(d[k][n])
