'''
[동전0]
동전 가치 n개로 k원을 만들고자 할 때,
필요한 최소 동전 갯수
'''

n, k = map(int, input().split())

coins = []
for i in range(n):
    money = int(input())
    coins.append(money)

coins.sort(reverse=True)

count = 0
for coin in coins:
    if k // coin == 0:
        continue
    else:
        count += (k//coin)
        k %= coin

print(count)

