'''
[집합]
add x : S에 x를 추가, x가 있는 경우 무시
remove x : S에 x를 제거, x가 없는 경우 무시
check x : S에 x가 있으면 1, 없으면 0
toggle x : S에 x가 있으면 제거, 없으면 추가
all : S를 {1, 2, ... , 20}으로 바꿈
empty : S를 공집합으로 바꿈
'''

import sys
input = sys.stdin.readline

m = int(input().rstrip())
S = set()
# replace_S = set([i for i in range(1, 21)])

for _ in range(m):
    order = input().split()  # 리스트 형태임!
    op = order[0]
    if len(order) == 1:
        if op == 'all':  # just order == 'all' -> False!!
            S = set(i for i in range(1, 21))
        else:  #if op == 'empty':
            S = set()
        continue
    num = int(order[1])  # 새로 할당!
    if op == 'add':
        S.add(num)
    elif op == 'remove':
        S.discard(num)  # 없어도 error 발생 X!
    elif op == 'check':
        print(1 if num in S else 0)
    elif op == 'toggle':
        if num in S:
            S.discard(num)
        else:
            S.add(num)
            
# -------------------------------------

import sys
input = sys.stdin.readline

m = int(input().rstrip())
bit = 0  # 0b: 이진수 연산

for _ in range(m):
    order = input().rstrip().split()
    op = order[0]
    if op == 'all':
        bit = (1 << 21) - 1  # 01111111...
    elif op == 'empty':
        bit = 0
    else:
        num = int(order[1])
        if op == 'add':
            bit |= (1 << num)
        elif op == 'remove':
            bit &= ~(1 << num)  # num 자리에 0, 나머지 1, and 연산
        elif op == 'check':
            if bit & (1 << num) == 0:
                print(0)
            else:
                print(1)
        elif op == 'toggle':
            bit ^= (1 << num)
        
