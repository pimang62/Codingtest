'''
[RGB 거리]
집을 R, G, B 중 하나의 색으로 칠해야
각각의 집을 칠하는 비용이 주어졌을 때
규칙을 만족하며 모든 집을 칠하는 최소 비용?

- 1번 집의 색은 2번 집의 색과 같지 않아야  
- n번 집의 색은 n-1번 집의 색과 같지 않아야
- 2 <= i <= n-1번 집의 색은 i-1, i+1번 집의 색과 같지 않아야

입력)
n = int(input())
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))
'''
n = int(input())
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

for i in range(1, n):
    # 0 : r, 1 : g, 2 : b
    table[i][0] += min(table[i-1][1], table[i-1][2])
    table[i][1] += min(table[i-1][0], table[i-1][2])
    table[i][2] += min(table[i-1][0], table[i-1][1])

print(min(table[n-1]))