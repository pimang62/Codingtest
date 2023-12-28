'''
[삼각형과 세 변]
'''

from collections import Counter

while True:
    nlist = list(map(int, input().split()))
    d = Counter(nlist)
    
    nlist.sort()
    another = nlist[:-1]
    
    maxi = max(nlist)

    if sum(nlist) == 0:
        break
    elif sum(another) <= max(d):
        print("Invalid")
    elif len(d) == 1:
        print("Equilateral")
    elif len(d) == 2:
        print("Isosceles")
    elif len(d) == 3:
        print("Scalene")