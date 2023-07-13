'''
[피보나치 함수]
0이 출력되는 횟수, 1이 출력되는 횟수

'''

'''
t = int(input())

zero, one = 0, 0

def fibo(n):
    global zero, one
    if n == 0: 
        zero += 1
        return 
    if n == 1: 
        one += 1
        return 
    return fibo(n-2), fibo(n-1)

for _ in range(t):
    n = int(input())
    zero, one = 0, 0
    fibo(n)
    print(zero, one)
'''

t = int(input())

for _ in range(t):
    n = int(input())
    d = [ [0, 0] for _ in range(n+2) ]    # 초기값 +2
    d[0][0] = d[1][1] = 1   # [ [1, 0], [0, 1], ...]
    
    for i in range(2, n+1):
        d[i][0] = d[i-2][0] + d[i-1][0]
        d[i][1] = d[i-2][1] + d[i-1][1]
    
    print(d[n][0], d[n][1])
