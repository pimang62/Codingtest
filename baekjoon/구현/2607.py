'''
[비슷한 단어]
알파벳 대문자, 2가지 조건
1. 같은 종류의 문자
2. 같은 개수만큼 있음

한 단어에서 한 문자 +, -, 바꿈
=> 같은 구성이면 비슷한 단어!

첫 번째 단어와 비슷한 단어 몇 개?

ex. {D:1, O:1, G:1}
    {G:1, O:1, D:1}
    {G:1, O:1} ok
    {G:1, O:2, D:1}
    {D:1, O:1, L:2}
'''
from collections import Counter

n = int(input())
tag = input()
target = Counter(tag)

cnt = 0
for _ in range(n-1):       
    tmp = Counter(input())
    # 문자 구성이 같은 경우: 각 문자의 개수 차이가 1 이내
    if sum((target - tmp).values()) <= 1 and sum((tmp - target).values()) <= 1:
        cnt += 1
    # 문자 구성이 하나 차이나는 경우: 추가된 문자 또는 제거된 문자가 하나, 그 외 문자의 개수 차이가 1 이내
    elif sum((target - tmp).values()) + sum((tmp - target).values()) == 2 and (len(target - tmp) == 1 or len(tmp - target) == 1):
        cnt += 1

print(cnt)