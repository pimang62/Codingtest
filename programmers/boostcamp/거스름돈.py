'''
거스름돈 n원을 줄 방법의 경우의 수

거슬러 줘야 하는 금액 1 <= n <= 1000000
화폐 단위 1 <= money <= 100

answer % 1000000007 !!
'''

def solution(n, money):
    d = [0] * (n+1)
    for m in money:
        d[m] += 1
        for i in range(m, n+1):
            if i-m > 0:
                d[i] += d[i-m]
    return d[n] % 1000000007

print(solution(n=5, money=[1, 2, 5]))
print(solution(n=5, money=[1, 2]))