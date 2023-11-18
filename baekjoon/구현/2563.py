'''
[색종이]
100 by 100
가로, 세로 크기 10

00000
00000
00000
'''
n = int(input())

graph = [[0]*100 for _ in range(100)]
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(b, b+10):  # 7 ~ 16 : 10
        for j in range(a, a+10):  # 3 ~ 12 : 10
            graph[i][j] = 1

cnt = 0
for i in range(100):
    cnt += graph[i].count(1)
    
print(cnt)
