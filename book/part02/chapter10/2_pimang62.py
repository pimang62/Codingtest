'''
0~n번 까지의 번호를 부여한다.
처음에는 총 n+1개의 팀이 존재한다.
1. '팀 합치기' 연산은 두 팀을 합치는 연산이다.
2. '같은 팀 여부 확인' 연산은 서로소 연산이다.
m개의 연산 수행 시 '같은 팀 여부 확인'에 대한 연산 결과는?
'''

import sys
input = sys.stdin.readline

# 학생 0~n번, 수행하는 연산 개수
n, m = map(int, input().split())

# 팀 번호 초기화
team = [0] * (n+1)

# 초기 팀 자기 자신
for i in range(n+1):
    team[i] = i

# --------------------------

# 같은 팀인지 확인 함수
def find_team(team, x):
    if team[x] != x:
        team[x] = find_team(team, team[x])
    return team[x]

# 팀 합치기 함수
def union_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)
    if a < b:
        team[b] = a
    else:
        team[a] = b

# --------------------------

result = []

# 연산에 대한 정보
for _ in range(m):
    # 연산 번호, a번, b번
    k, a, b = map(int, input().split())
    # 팀 합치기
    if k == 0:
        union_team(team, a, b)
    # 같은 팀인지 확인
    elif k == 1:
        if find_team(team, a) != find_team(team, b):
            result.append("NO")
        else:
            result.append("YES")

# 결과 출력
for i in result:
    print(i, end='\n')

