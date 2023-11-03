'''
[음계]
c d e f g a b C -> 총 8개
1 2 3 4 5 6 7 8

'''

n = int(input())

nlist = [' '*(n-i)+'*'*(2*i-1) for i in range(1, n+1)]
nlist = nlist + list(reversed(nlist[:-1]))

for l in nlist:
    print(l)