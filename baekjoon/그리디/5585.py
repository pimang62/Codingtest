'''
[거스름돈]
잔돈 = [500, 100, 50, 10, 5, 1]
1000엔 지폐 한 장을 냈을 때, 가장 적은 거스름돈 개수?
'''

n = int(input())   # 380

target = 1000 - n  # 620
coin = [500, 100, 50, 10, 5, 1]

cnt = 0
for c in coin:
    while target >= c:
        cnt += target // c
        target %= c

print(cnt)