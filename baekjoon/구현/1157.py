"""
from collections import Counter

string = input().strip().lower()
sdict = Counter(string)

value = max(sdict.values())
sdict = dict(sorted(sdict.items(), key=lambda x: -x[1]))

# {'i':4, 's':4, ...}
ans, cnt = '', 0  # 중복 횟수?
for k, v in sdict.items():
    if v == value:
        ans = k
        cnt += 1
    if value > v:
        break

print(ans.upper() if cnt == 1 else '?')
"""

'''
1. 같은 눈 3개 : 10000 + ()*1000
2. 같은 눈 2개 : 1000 + ()*100
3. 모두 다른 눈 : 가장 큰 눈 * 100
'''
from collections import Counter
dice_dict = Counter(map(int, input().split()))

dice_dict = dict(sorted(dice_dict.items(), key=lambda x: (-x[1], -x[0])))

for k, v in dice_dict.items():
    if len(dice_dict) == 1:
        print(10000+k*1000)
    elif len(dice_dict) == 2:
        print(1000+k*100)
    else:  # len() == 3
        print(k*100)
    break

