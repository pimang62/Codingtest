'''
[Base Conversion]

A진법을 B진법으로 바꿈

'''
A, B = map(int, input().split())

m = int(input())

mlist = list(map(int, input().split()))  # [2, 16]

def transfer(num, B):
    s = []
    while num != 0:
        num, b = divmod(num, B)
        s.append(str(b))
    return s[::-1]

aint = 0  # 2*A**1 + 16*A**0
for i in range(m):
    aint += mlist[i]*(A**(m-1-i))

print(' '.join(transfer(aint, B)))
