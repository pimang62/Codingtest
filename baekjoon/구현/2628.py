'''
[종이자르기]
종이 가로 세로 길이 <= 100
잘라야할 점선들

가장 큰 종이 조각의 넓이?
10 8
3
0 3
1 4
0 2
'''
m, n = map(int, input().split())  # 가로, 세로
k = int(input())

h, w = [0, n], [0, m]  # height, width
for _ in range(k):
    op, num = map(int, input().split())
    if op == 0:
        h.append(num)
    else:  # == 1
        w.append(num)

h.sort()  # [0, 3, 4, 8]
w.sort()  # [0, 4, 10]

max_h, max_w = 0, 0
for i in range(len(h)-1):
    max_h = max(max_h, h[i+1]-h[i])

for j in range(len(w)-1):
    max_w = max(max_w, w[j+1]-w[j])

print(max_h*max_w)