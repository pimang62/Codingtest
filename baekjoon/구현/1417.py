'''
[국회의원 선거]

다솜이는 기호 1번이다.
다른 모든 사람의 득표수보다 "많은" 득표수를 가질 때

다솜이가 매수해야하는 사람의 최솟값?
한 사람당 한표
'''
import heapq

n = int(input())

target = int(input())

q = []
for _ in range(n-1):
    heapq.heappush(q, -int(input()))

cnt = 0  # 몇 명?
while True:
    if not q or target > -q[0]:
        break
    tmp = heapq.heappop(q)
    heapq.heappush(q, tmp+1)  # -*+1
    target += 1
    cnt += 1

print(cnt)