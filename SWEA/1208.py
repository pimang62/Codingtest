'''
[Flatten]
가장 높은 곳 - 가장 낮은 곳 <= 1
제한 횟수만큼 옮김

0 1 2 3 4 5 6 7 8 9 10
5 8 3 1 5 6 9 9 2 2 4

q = [1 2 2 3 4 5 5 6 8 9 9]
q = [2 2 2 3 4 5 5 6 8 8 9]

{1: 1, 2:2, 3:1, 4: 1, ... 9:2}
{1: 0, 2:3, 3:1, 4: 1, ... 9:1}

'''
from collections import defaultdict

for t in range(1, 11):  # test case
    k = int(input())  # dump
    nlist = list(map(int, input().split()))
    
    d = defaultdict(int)
    for n in nlist:
        d[n] += 1
        
    while k:  # k != 0
        maxi = max(d.keys())  # 9
        mini = min(d.keys())  # 1
        
        d[maxi-1] += 1
        d[mini+1] += 1
        d[maxi] -= 1
        d[mini] -= 1
        
        if not d[maxi]:  # == 0
            del d[maxi]
        if not d[mini]:
            del d[mini]
        k -= 1
    
    print(f'#{t} ' + str(max(d.keys())-min(d.keys())))

