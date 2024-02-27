'''
[solved.ac]
아무 의견이 없다면 0
의견이 하나 이상이면, 모든 사람의 난이도 의견의 30% 절사 평균

절사 평균이란 가장 큰 값, 가장 작은 값 제외 후 평균
위에서 15%, 아래서 15%를 제외하고 평균 계산
ex. 20명이면 위 3명, 아래 3명 제외
ex. 25명이면 위 3.75 -> 4명, 아래 "

평균도 반올림

오사오입 : 0.5 초과 -> 올림, 0.5 이하 -> 내림
'''
import sys
input = sys.stdin.readline

n = int(input())

nlist = []
for _ in range(n):
    nlist.append(int(input()))

nlist.sort()  # 오름차순

def round2(num):  # 파이썬 오사오입 때문 -> 직접 정의
    if num - int(num) >= 0.5:
        return int(num)+1
    else:
        return int(num)

s = round2(n*0.15)  
slices = nlist[s:n-s]  # not -s !

if not slices:
    print(0)
else:
    print(round2(sum(slices)/len(slices)))