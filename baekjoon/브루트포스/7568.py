'''
[덩치]
n명의 집단, 각 사람의 덩치 등수는 자신보다 더 "큰 덩치" 사람의 수
덩치 등수가 k이면 자신의 등수는 k+1
- 같은 덩치 등수를 가진 사람이 여러 명 가능!!

입력)
import sys
input = sys.stdin.readline

data = []
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    data.append((x, y))

출력)
입력에 나열된 사람의 덩치 등수 순서대로 출력!
'''
'''
import sys
input = sys.stdin.readline

from collections import deque

data = []
n = int(input())
for i in range(n):
    # 순서, 몸무게, 키
    x, y = map(int, input().split())
    data.append((i, x, y))

# 몸무게, 키 순서대로 정렬
data.sort(key=lambda x: (-x[1], -x[2]))

# n명의 순위 기록
ranking = [0] * n
'''

'''
q = deque(data)

# 초깃값 기록
i, x, y = q.popleft()
ranking[i] = 1  # 1위

rank = 1    # 1위부터 시작
tmp = 0     # 공동 순위 사람의 개수
while q:
    ni, nx, ny = q.popleft()
    if x > nx and y > ny:   # 이전 값이 크다면
        rank += tmp     # + 공동 순위 사람
    else:
        tmp += 1
    ranking[ni] = rank

    
    x, y = nx, ny

print(*ranking)
'''

'''
rank = 1    # 1위부터 시작
i, x, y = data[0]   # 초깃값
ranking[i] = rank   # 1등

tmp = 1     # 순위가 같은 사람의 수
for j in range(1, len(data)):
    ni, nx, ny = data[j]
    if x > nx and y > ny:
        rank += tmp
        ranking[ni] = rank
        tmp = 1     # 초기화
    else:
        tmp += 1
        ranking[ni] = rank
    
    i, x, y = ni, nx, ny

print(*ranking)
'''

import sys
input = sys.stdin.readline

from collections import deque

data = []
n = int(input())
for i in range(n):
    # 몸무게, 키
    x, y = map(int, input().split())
    data.append((x, y))

ranking = []
for now in data:
    x, y = now
    rank = 1
    for nxt in data:
        nx, ny = nxt
        # 자기보다 큰 사람의 숫자!
        if nx > x and ny > y:
            rank += 1
    ranking.append(rank)

print(*ranking)



