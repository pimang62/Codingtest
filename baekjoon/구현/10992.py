'''
[별 찍기 - 17]
3 1
2 1 1 1
1 1 3 1
2n-1

'''
n = int(input())

for i in range(n-1):
    if i == 0:
        print(' '*(n-1-i)+'*')
    else:
        print(' '*(n-1-i)+'*'+' '*(2*i-1)+'*')
print('*'*(2*n-1))
