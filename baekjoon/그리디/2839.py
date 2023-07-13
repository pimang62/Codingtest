'''
[설탕 배달]
상근이는 설탕을 정확하게 nkg 배달해야 한다.
봉지는 3kg와 5kg이 있다.
최대한 적은 봉지를 들고 가는 수?

풀이)
그리디 : 
1. 5로 나누어 떨어지지 않으면 3을 뺌
2. n > 0인 n을 업데이트 하면서 최종 결과가 0이 아니면 -1

DP:
1. d = [1e9] * (n+1)
2. d[i] = 1 + min(d[i-3], d[i-5])
'''

n = int(input())

cnt = 0
while n > 0:
    # n이 5로 나누어 떨어지면
    if n % 5 == 0:
        cnt += n//5
        n %= 5
        break
    n -= 3
    cnt += 1

if n == 0:
    print(cnt)
else:
    print(-1)


n = int(input())

d = [1e9] * (n+1) * 5   # n = 1일 때 d[5] 초기화 하려면
d[3] = d[5] = 1         # 초기화

for i in range(6, n+1):
    d[i] = 1 + min(d[i-3], d[i-5])

if d[n] < n:
    print(d[n])
else:
    print(-1)