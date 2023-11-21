'''
[피보나치 수]
n이 주어졌을 때 n번째 피보나치 수?
'''
n = int(input())

d = [0]*46  # <= 45
d[0], d[1] = 0, 1

for i in range(2, 46):
    d[i] = d[i-2] + d[i-1]

print(d[n])