'''
[회의실 배정]
한 개의 회의실을 사용하고자 하는 n개의 회의
시작시간, 끝나는 시간 
겹치지 않게 하는 최대 개수
끝나는 것과 동시에 다음 회의가 시작될 수 있다.
시작시간과 끝나는 시간이 같을 수도 있다.
'''

n = int(input())

conference = []
for _ in range(n):
    a, b = map(int, input().split())
    # 끝나는 시간 기준 정렬
    conference.append((b, a))

conference.sort()

count = 0
f = 0
for conf in conference:
    end, start = conf
    if start >= f:
        count += 1
        f = end
    else:
        continue

print(count)