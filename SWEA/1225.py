'''
[암호생성기]
8개의 숫자

사이클 반복
1, 2, 3, ... 감소한 뒤 맨 뒤로
0이 되는 경우 맨 뒤로 -> break

10 6 12 8 9 4 1 3
16 18 20 34 17 29 18 24

'''
from collections import deque

T = 10
for _ in range(T):
    t = int(input())  # 테스트 케이스 번호
    nlist = list(map(int, input().split()))

    cleaned = []  # [10, 16, 10, 13, 18, 11, 11, 11]
    mini = min(nlist)
    for n in nlist:
        cleaned.append(n-15*(mini//15-1))
    print(cleaned)

    q = deque(cleaned)
    cnt = 1  # 시작 감소 카운트
    while True:
        a = q.popleft()
        if a-cnt <= 0:
            q.append(0)
            break
        else:
            q.append(a-cnt)

        cnt += 1
        if cnt > 5:
            cnt = 1  # reset

    print(f'#{t} ' + ' '.join([str(a) for a in list(q)]))