'''
[요세푸스 문제 0]
n명의 사람, k번째 사람을 제거

1 (2) (3) 4 (5) (6) (7)
1 2 4 5 6 7
'''
from collections import deque

n, k = map(int, input().split())

q = deque([i for i in range(1, n+1)])  # [1, 2, 3, 4, 5, 6, 7]

# 3개 이하로 남을 때까지
cnt = 0  # 횟수 세기
answer = []
while q:
    q.rotate(-1)
    cnt += 1
    if cnt == k:
        answer.append(q.pop())
        cnt = 0

for i in q:
    answer.append(i)

print('<'+', '.join(str(a) for a in answer)+'>')