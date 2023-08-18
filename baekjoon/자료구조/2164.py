'''
[카드2]
1~n의 카드

1234 -> 234 -> 342
342 -> 43 -> 24
24 -> 4 -> 4

n이 주어졌을 때 제일 마지막에 남는 카드?

'''
from collections import deque

n = int(input())
q = deque([i for i in range(1, n+1)])

while len(q) != 1:
    q.popleft()             # 버리고
    q.append(q.popleft())   # 뒤에 넣음

print(q[0])
