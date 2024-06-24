'''
[NBA 농구]
https://www.acmicpc.net/problem/2852

골이 들어간 시간, 팀 적음
농구 경기는 48분 진행

각 팀이 몇 분동안 이기고 있었는지?

3
1 01:10 -> 1:0 
2 21:10 -> 1:1 20:00
2 31:30 -> 1:2 :30

5
1 01:10 -> 1:0
1 02:20 -> 2:0
2 45:30 -> 2:1
2 46:40 -> 2:2
2 47:50 -> 2:3
'''
from collections import defaultdict

# 입력받기
N = int(input())

score = defaultdict(int)
table = defaultdict(int)
total = defaultdict(int)

def time2int(time):
    m, s = map(int, time.split(":"))
    return 60 * m + s

def int2time(_int):
    m, s = _int // 60, _int % 60
    return f"{m:02d}:{s:02d}"

winner = None
last_time = 0

for _ in range(N):
    team, time = input().split()
    int_time = time2int(time)
    
    # 현재 이기고 있는 팀의 시간을 업데이트
    if winner is not None:
        total[winner] += int_time - last_time
    
    # 점수 업데이트
    score[team] += 1
    last_time = int_time
    
    # 현재 이기고 있는 팀 결정
    if score["1"] > score["2"]:
        winner = "1"
    elif score["2"] > score["1"]:
        winner = "2"
    else:
        winner = None

# 경기 종료 후 최종 승리팀 시간 추가
end_time = time2int("48:00")
if winner is not None:
    total[winner] += end_time - last_time

for team in ["1", "2"]:
    print(team, int2time(total[team]))
    


