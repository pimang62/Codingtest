'''
[성 지키기]
https://www.acmicpc.net/problem/1236

모든 행과 모든 열에 한 명 이상의 경비원
print(max(row, col))

>>> 교차되는 지점에 분산해서 넣으면 됨!
'''

n, m = map(int, input().split())
graph = [input() for _ in range(n)]

row, col = 0, 0
for i in range(n):
    if graph[i] == "."*m:
        row += 1

for j in range(m):
    flag = True
    for i in range(n):
        if graph[i][j] != ".":
            flag = False
            break
    if flag:
        col += 1

print(max(row, col))
