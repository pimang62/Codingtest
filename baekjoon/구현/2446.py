'''
[별 찍기 - 9]
0 9 : 0 + 2*n-1 - 2*i
1 7 : 1 + 2*
2 5 : 2
3 3 : 3
4 1 : 4 + 2*n-1 - 2*i
3 3 : 3 + 2
2 5 : 2
1 7 : 1
0 9 : 0
'''
n = int(input())

blank = -1
for i in range(2*n-1):
    if i >= n:
        blank -= 1
    else:  # blank < n
        blank += 1
    print(' '*blank + '*'*(2*(n-blank)-1))