'''
[분해합]
자연수 n, 1 <= n < 1000000
n의 분해합은 n과 n을 이루는 각 자리수의 합

245는 256(245+2+4+5)의 생성자
생성자가 없을수도, 여러 개일수도 있음!

n의 가장 작은 생성자는?

'''
import sys
input = sys.stdin.readline

target = int(input())

result = 0
for i in range(1, target+1):
    # 자기 자신 + 각 자리수의 합
    tmp = i + sum([int(s) for s in str(i)])
    if tmp == target:
        result = i  # 해당 생성자
        break   # 가장 작은 값!

print(result)

