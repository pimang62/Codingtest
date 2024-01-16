'''
[직사각형 네개의 합집합의 면적 구하기]
0 0 0 0 0 0 0
0 0 1 1 0 0 0
0 0 1 2 1 1 1
0 0 1 2 1 1 1
0 0 0 1 1 1 1

x: 1~3, y: 2~3
x: 2~4, y: 3~6
'''
graph = [[0]*100 for _ in range(100)]  # 0~99
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] += 1

answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] > 0:
            answer += 1

print(answer)