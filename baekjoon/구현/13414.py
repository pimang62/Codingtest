'''
[수강신청]
1. 버튼을 빨리 누른 사람이 대기목록 먼저
2. 대기열에서 다시 수강신청 -> 맨 뒤로 밀려남
3. 앞에 있는 학생부터 자동으로 완료, 꽉찰 경우 나머지 무시

- 중복 목록 삭제
- 맨 앞에서 최대 가능 인원 선정

최종적으로 성공한 인원?

1 <= k <= 1e6
1 <= l <= 5e6
'''
k, l = map(int, input().split())  # 가능 인원, 대기목록 길이

d = {}
for i in range(l):
    student = input()
    d[student] = i

# ['20103324', '20133221', '20093778', '20140101', '20103325', '01234567']
dlist = sorted(d, key=lambda x: d[x])

idx = 0
for o in range(len(dlist)):
    if idx >= k:
        break
    print(dlist[o])
    idx += 1
   