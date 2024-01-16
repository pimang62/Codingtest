'''
[올림픽]

'''
n, k = map(int, input().split())

q = []
for _ in range(n):
    num, g, s, b = map(int, input().split())
    if num == k:
        target = (g, s, b)
    q.append((g, s, b))

q.sort(key=lambda x : (-x[0], -x[1], -x[2])) 

for i in range(len(q)):  # 0~
    if q[i] == target:
        print(i+1)
        break


