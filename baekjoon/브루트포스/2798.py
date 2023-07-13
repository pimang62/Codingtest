'''
[블랙잭]
카드의 합 <= 21 최대한 크게 만들기

n장의 카드, 딜러 m 외침
n장의 카드 중 3장의 카드를 고른다
카드의 합은 m을 넘지 않으면서 m의 최대한 가깝도록!

입력)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))

출력)
m을 넘지 않으면서 m에 최대한 가까운 카드의 합?
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))

from itertools import combinations

answer = 1e9
cnt = 1e9
for num_list in list(combinations(card, 3)):
    tmp = m-sum(num_list)
    #if cnt == 1e9 : 
    #    cnt = tmp   # 초깃값
    if tmp <= cnt and not tmp < 0: 
        cnt = tmp   # 업데이트
        answer = sum(num_list)

print(answer)
