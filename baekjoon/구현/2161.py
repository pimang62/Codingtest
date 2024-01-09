'''
[카드1]
n장의 카드, 1~n번호
맨 위 하나를 버리고, 맨 위를 맨 뒤로 -> 반복
버린 카드 | 남은 카드 순서대로 출력

1 <= n <= 1000
시간 복잡도 : O(n**2) -> 1e6
'''
from collections import deque

n = int(input())
nlist = [i for i in range(1, n+1)]

answer = []
q = deque(nlist)
cnt = 1  # 시도 횟수
while True:
    if len(q) == 1:
        answer += list(q)
        print(*answer)
        break
    if cnt % 2 != 0:  # 홀수 횟수
        answer.append(q.popleft())
    else:  # cnt % 2 == 0  # 짝수 횟수
        q.rotate(-1)  # 왼쪽으로 한 칸
    cnt += 1
