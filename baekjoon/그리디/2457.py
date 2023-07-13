'''
[공주님의 정원]
총 n개의 꽃, 꽃은 모두 같은 해에 피어서 같은 해에 진다.
하나의 꽃은 피는 날과 지는 날이 정해져 있다.
ex. 5/8 ~ 6/13 : 6/12일까지는 피어 있음

조건)
1. 3/1 ~ 11/30까지 매일 꽃이 한 가지 이상 피어있도록
2. 정원에 심는 꽃들의 수를 가능한 적게

선택한 꽃들의 최소 개수?

채점)
https://www.acmicpc.net/problem/2457
'''
from collections import deque

n = int(input())

data = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    data.append((a*100+b, c*100+d))

data.sort()

# 업데이트 될 마지막 날짜
pre_end = 301
# 심은 꽃의 개수
cnt = 0

q = deque(data)

while q:
    
    # 첫 시작 지점
    cur_start = q[0][0]

    # 첫 시작 지점이 301보다 클 때 수행 안 함
    # 업데이트 된 마지막 날짜가 1130을 넘어서면 더 이상 심지 않아도 됨!
    if cur_start > pre_end or pre_end > 1130:
        break

    # 저장된 마지막 날짜보다 빠르게 시작하며 지는 날짜 중 가장 큰 것 찾기
    temp = -1
    while q:
        temp_start, temp_end = q[0]
        # 시작 날짜가 저장된 마지막 날짜보다 작으며
        if temp_start <= pre_end:
            # 마지막 날짜가 더 큰 값 업데이트
            temp = max(temp, temp_end)
            q.popleft()
        # 시작 날짜가 저장된 마지막 날짜보다 커지면
        else:
            break

    # 최근 지는 꽃의 날짜 업데이트
    pre_end = temp
    # 현재 심은 꽃 count
    cnt += 1

# 저장된 마지막 날짜가 1201보다 작다면 조건 1에 부합하지 않으므로 0
print(0 if pre_end < 1201 else cnt)





'''
cnt = 0
for i in range(len(flower)):
    # 현재 피울 꽃 지정
    if flower[i][0] > 301 :
        break
    val = 0
    # 다음 꽃들 중
    for j in range(i+1, len(flower)):
        # 다음 꽃의 피는 시간이 현재 피운 꽃의 지는 시간보다 클 때 
        if flower[j][0] > flower[i][1]:
            break
'''



            




        





