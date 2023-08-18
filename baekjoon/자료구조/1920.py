'''
[수 찾기]
N개의 정수, A[1] ... A[N]
이 안에 X라는 정수가 존재하는지

입력)
n = int(input()) <= 1e5
table = list(map(int, input().split()))
m = int(input()) <= 1e5
check = list(map(int, input().split()))
'''
from collections import Counter 

n = int(input()) # <= 1e5
table = set(map(int, input().split()))     # 180ms
#table = Counter(map(int, input().split()))  # 220ms

m = int(input()) # <= 1e5
check = list(map(int, input().split()))

for c in check:
    if c in table:
        print(1)
    else:
        print(0)