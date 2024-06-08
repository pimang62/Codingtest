'''
[숫자 게임]
n명, 1~10 사이 5장 카드

그 중 3장을 골라 합을 구함
일의 자리가 "큰" 사람이 이김

가장 큰 수가 2명 이상일 경우
번호가 큰 사람의 번호를 출력
'''
from itertools import combinations

n = int(input())

who = 0
maxi = 0
for i in range(1, n+1):
    five = list(map(int, input().split()))
    
    tmp = 0  # 가장 큰 1의자리 후보
    for three in combinations(five, 3):
        tmp = max(tmp, int(str(sum(three))[-1]))

    if int(tmp) >= maxi:  # 제일 큰 놈
        maxi = tmp
        who = i  # index

print(who)
