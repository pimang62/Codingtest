'''
[2018 KAKAO BLIND RECRUITMENT]

"9시"부터 총 n회 t분 간격 도착
하나의 셔틀에는 최대 m명

어떤 크루가 몇 시에 셔틀 대기열에 도착하는지 알고있음
게으른 콘이 갈 수 있는 도착 시각 중 제일 늦은 시각?

다음날 셔틀 타는 일은 없음

00:00 ~ 23:59
9:00 : 540min

1. now 시간을 만든다.
2. timetable에 집어넣고 sort
3. m 이하로 순회 cnt & idx가 범위 안 & 현재 time이 bus 시간보다 작은 경우
    idx += 1
    cnt += 1
4. cnt가 m보다 작다면 자리가 있는 경우임
    버스 시간과 동일하게 도착
5. cnt가 m보다 크거나 같다면 내가 못탐
    한 사람 앞보다 1분 일찍

'''

def transfer(timetable):
    new_table = []
    for time in timetable:
        h, m = time.split(':')
        new_table.append(int(h)*60 + int(m))
    return new_table

def solution(n, t, m, timetable):
    answer = 0  # minite으로 저장
    timetable = transfer(timetable)  # 변환
    timetable.sort()

    bustime = [9*60+t*i for i in range(n)]  # 9*60+t*0~
    
    idx = 0  # timetable의 index
    for bus in bustime:  # 	[550, 560] / [600, 660, 720, 780, 840, 900, 960, 1020, 1080, 1140]
        cnt = 0  # 자리 남았는지 확인
        while cnt < m and idx < len(timetable) and timetable[idx] <= bus:
            idx += 1
            cnt += 1

        if cnt < m:  # 자리가 남았다는 소리이므로
            answer = bus  # 버스 도착 시간
        else:  # cnt >= m: 자리가 남지 않았다는 소리니까
            answer = timetable[idx-1]-1
    
    h, m = str(answer//60), str(answer%60)
    if len(str(h)) == 1: 
        h = '0'+h
    if len(str(m)) == 1:
        m = '0'+m
    
    return ':'.join([h, m])