import math

n = int(input())  # 26

# 모두 소수(True)로 초기화 : 0, 1 제외
array = [True for _ in range(n+1)] 

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        # i의 배수 모두 False
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1

for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')

        # 2 3 5 7 11 13 17 19 23
