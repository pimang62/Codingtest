'''
[빗물]
고이는 빗물의 총량?
전혀 고이지 않을 경우 0

0 0 0 1
1 0 0 1
1 0 0 1 
1 0 1 1

3 0 1 4

3 1 2 3 4 1 1 2

ans, prev_max,  
- 처음 기록된 값 <= 현재 값:
    처음 기록된 값 = 현재값
    ans += tmp
    tmp = 0
- 처음 기록된 값 > 현재 값:
    tmp += (첫 - 현)

'''
h, w = map(int, input().split())

A = list(map(int, input().split()))

ans, prev, tmp = 0, 0, 0
for i in range(w):
    if prev <= A[i]:
        

    else:  # prev > A[i]
        tmp = max(tmp, A[i])

print(ans)