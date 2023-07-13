'''
[숨바꼭질]
수빈이는 n에 동생은 k에 있다.
수빈이의 위치에서 1초 후에 n-1 또는 n+1로 이동한다.
순간이동을 하는 경우에는 1초 후에 2*n의 위치로 이동한다.

수빈이가 동생을 찾을 수 있는 가장 빠른 시간은?

입력)
n, k = map(int, input().split())


풀이)
d = [1e9 for i in range(k*2)]

'''
from collections import deque

n, k = map(int, input().split())

'''
d = [1e9 for _ in range(k*3)]
d[n] = 0  # 거리 초기화

v = [0] * 100001
v[n] = 1

def update(d, now):
    for nxt in [now-1, now+1, now*2]:
        d[nxt] = min(d[nxt], d[now]+1) 
        if v[nxt] == 0:
            q.append(nxt)
            v[nxt] = 1
    return (d, q)

q = deque([n])
while q[0] != k:
    now = q.popleft()
    if 1 <= now <= k+1 :
        (d, q) = update(d, now)

print(d[k])
'''

# 최단 거리이므로 처음 기록할 때가 가장 최소!
d = [0] * 100001

q = deque([n])
while q:
    now = q.popleft()
    if now == k:
        print(d[now])
        break
    for nxt in (now-1, now+1, now*2):
        if 0 <= nxt <= 100000 and d[nxt] == 0:
            d[nxt] = d[now] + 1
            q.append(nxt)
