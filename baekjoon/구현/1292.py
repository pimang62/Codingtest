'''
[쉽게 푸는 문제]
1 22 333 4444 55555
n(n+1)/2 = 1000
49*50
...
45*46 = 2070
'''
nlist = []
for i in range(1, 46):  # 1~45
    nlist += [i]*i
    
A, B = map(int, input().split())
print(sum(nlist[A-1:B]))  # B-1+1