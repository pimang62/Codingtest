'''
[트럭]
다리를 n개의 트럭이 건너려고 함
다리 위에는 w대의 트럭만 동시에 올라갈 수 있음

다리 위에 올라가 있는 트럭들의 무게의 합은 L보다 작거나 같아야 함

ex. w=2, L=10, [7, 4, 5, 6] -> 최단 시간은 8임

0 0 [7, 4, 5, 6]
0 7 [4, 5, 6]
7 0 [4, 5, 6]
0 4 [5, 6]
4 5 [6]
5 0 [6]
0 0 [6]
0 6 []
6 0 []
'''
from collections import deque

n, w, L = map(int, input().split())
nqueue = deque(map(int, input().split()))

q = deque([0]*w)  # [0, 0]
time = 0  # 모든 트럭이 다리를 건너는 시간
while True:
    if (sum(q) == 0) and (not nqueue):
        break
    q.popleft()  # 맨 앞 원소 빼기
    if nqueue and sum(q)+nqueue[0] <= L:
        q.append(nqueue.popleft())
    else:
        q.append(0)
    print(list(q), list(nqueue))
    time += 1

print(time)