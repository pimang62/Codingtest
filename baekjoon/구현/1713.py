'''
[후보 추천하기]
1. 모든 사진틀은 비어있다
2. 특정 학생을 추천하면 반드시 게시
3. 비어있는 공간이 없는 경우 추천 횟수가 가장 적은 학생을 뺌
    - 그 자리에 새로 추천받은 학생 게시
    - 두 명 이상일 경우 가장 오래된 사진 삭제
4. 이미 추천 되어 있다면 추천 횟수만 추가
5. 삭제되는 경우 추천 횟수는 0으로 바뀜

최종 후보 오름차순으로 출력

(cnt, idx, num)
'''
from heapq import heappush, heappop

n = int(input())
k = int(input())
klist = list(map(int, input().split()))

q = []
for i, stud in enumerate(klist):
    new_q = []
    flag = False
    
    while q: # 이미 stud가 포함되었는지 확인
        cnt, idx, num = heappop(q)
        if num == stud:
            cnt += 1
            flag = True
        heappush(new_q, (cnt, idx, num))
    
    # 원소 새로 추가 timing & 범위 벗어나면
    if not flag and len(new_q) >= n:
        heappop(new_q)
    if not flag:
        heappush(new_q, (1, i, stud))
    
    q = new_q
    
answer = [x[-1] for x in q]
answer.sort()

print(*answer)
