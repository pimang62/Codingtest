'''
[아시아 정보 올림피아드]
성적 순대로 금, 은, 동 메달 수여
단, 동점자 없다고 가정

나라별 메달 수는 최대 2개
메달 수상자 결정하여 출력

9
1 1 230
1 2 210
1 3 205
2 1 100
2 2 150
3 1 175
3 2 190
3 3 180
3 4 195

1 1 금 (국가, 학생)
1 2 은
3 4 동
'''
from heapq import heappush, heappop

N = int(input())

q = []
for _ in range(N):
    nation, student, score = map(int, input().split())
    heappush(q, (-score, student, nation))

cnt = 3  # 3명 뽑아야
who = []
d = {}
while cnt > 0:
    score, student, nation = heappop(q)
    if d.get(nation, 0) >= 2:
        continue
    who.append((nation, student))
    d[nation] = d.get(nation, 0) + 1
    cnt -= 1

for res in who:
    print(*res)