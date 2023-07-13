'''
[1, 2, 3 더하기]
양수 n을 1, 2, 3의 합으로 만들 수 있는 경우의 수
n < 11

입력)
t = int(input())

for _ in range(t):
    n = int(input())

'''

t = int(input())

for _ in range(t):
    n = int(input())
    
    d = [0] * (n+4)  # +3 초기화
    d[1], d[2], d[3] = 1, 2, 4

    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]

    print(d[n])