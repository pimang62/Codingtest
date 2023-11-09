'''
[프린터 큐]
중요도가 높은 순으로 인쇄
한 문서가 몇 번째로 인쇄되는지?

단, 중요도가 같은 문서가 여러 개 있을 수도!!

0 1 2 3 4 5
1 1 9 1 1 1
'''
from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())  # 문서 개수, 궁금한 문서 인덱스
    nlist = list(map(int, input().split())) # [1, 1, 9, 1, ...]
    
    doc = []  # [(1, 0), (1, 1), (9, 2), (1, 3), ...]
    for i, num in enumerate(nlist):
        doc.append((num, i))
    
    q = deque(doc) 
    cnt = 0  # 뽑힌 횟수
    while True:
        # max(q): (9, 2), (9, 3) 있을 때 (9, 3) 꺼내버림!
        maxi, _ = max(q, key=lambda x: x[0])
        if q[0][0] == maxi:
            (w, idx) = q.popleft()
            cnt += 1  # 뽑힌 횟수
            if idx == m:
                break
        else:  # 찾는 maxi가 아니라면
            q.rotate(-1)
        
    print(cnt)