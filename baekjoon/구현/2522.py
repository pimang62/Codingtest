'''
[별 찍기 - 12]
  *
 **
***
 **
  *
'''

n = int(input())

cnt = 1  
for i in range(2*n-1):
    if i < n:
        print(' '*(n-cnt) + '*'*cnt)
        cnt = cnt + 1 if i < n-1 else cnt - 1
    else:
        print(' '*(n-cnt) + '*'*cnt)
        cnt -= 1