def solution(n, money):
    d = [1] + [0] * (n+1)
    for m in money:
        for i in range(m, n+1):
            if i-m >= 0:
                d[i] += d[i-m]
    return d[n] % 1000000007

solution(n=5, money=[1, 2, 5])

def solution(n, money):
    d = [0] * (n+1)
    for m in money:
        d[m] += 1
        for i in range(m, n+1):
            if i-m > 0:
                d[i] += d[i-m]
    return d

solution(n=5, money=[1, 2, 5])
