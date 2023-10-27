'''
알파벳에 해당하는 숫자?
UNUCIC : 

ABC 1
DEF 2
GHI 4
...

1은 2초, 2는 3초, 3은 4초 ... 각 1초씩 +1
'''
numdict = {'ABC':2, 'DEF':3, 'GHI':4,
           'JKL':5, 'MNO':6, 'PQRS':7,
           'TUV':8, 'WXYZ':9}

string = list(map(str, input()))  # list(input())

ans = 0
for s in string:
    for k in numdict.keys():
        if s in k:
            ans += numdict[k]+1

print(ans)
