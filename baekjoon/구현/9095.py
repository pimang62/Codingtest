'''
[1, 2, 3 더하기]
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수?

n은 양수이며 11보다 작다.

입력)
t = int(input())

for _ in range(t):
    n = int(input())
    d = [0] * (n+1)
    d[1], d[2], d[3] = 1, 2, 4
    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[n])

'''

t = int(input())
answer = []

for _ in range(t):
    n = int(input())
    d = [0] * (n+3)   # n = 1, 2, 3
    d[1], d[2], d[3] = 1, 2, 4
    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[n])
