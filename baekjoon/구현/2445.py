'''
[별 찍기 - 8]
1 8 1
2 6 2
3 4 3
4 2 4
5 0 5
4 2 4

'''
n = int(input())

i = 0
for k in range(2*n-1):
    if k >= n:
        i -= 1
    else:
        i += 1
    print('*'*i + ' '*(2*(n-i)) + '*'*i)