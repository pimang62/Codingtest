'''
[별 찍기 - 6]
0 2n-1
1 2n-3
  ...
4 1
'''
n = int(input())

for i in range(n):
    print(" "*i + "*"*(2*(n-i)-1))