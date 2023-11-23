'''
[최댓값]
9 by 9, 81개
0 포함 자연수
최댓값이 몇행 몇열
'''
maxi = -1
mi, mj = 0, 0

for i in range(9):
    row = list(map(int, input().split()))
    for j in range(9):
        if row[j] > maxi:
            maxi = row[j]
            mi, mj = i+1, j+1
            
print(maxi)
print(mi, mj, end=' ')
        