'''
[과제는 끝나지 않아!]
https://www.acmicpc.net/problem/17952

분단위로 과제가 추가되고 있음

1. 가장 최근에 나온 순서대로, 바로 시작
2. 새로운 과제가 나오면 하던 과제 중단
3. 새로운 과제 끝나면 이전에 하던 부분부터 이어서

몇 분이 걸릴지 정확하게 알며, 무조건 만점
자기가 받을 과제 점수를 예상해보고 싶다!
'''
N = int(input())

stack = []
cnt = 0
for _ in range(N):
    row = list(map(int, input().split()))
    if row[0] == 1:
        _, score, time = row
        if time-1 == 0:
            cnt += score
            continue
        stack.append((score, time-1))                
    if row[0] == 0 and stack:
        prev_score, prev_time = stack.pop()
        prev_time -= 1
        if prev_time == 0:
            cnt += prev_score
        else:
            stack.append((prev_score, prev_time))

# for _ in stack:
#     s, t = _
#     if t == 0:
#         cnt += s

print(cnt)