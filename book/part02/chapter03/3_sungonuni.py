"""
입력으로 정수 N,K를 받는다. N이 1이 될 때까지 다음 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 
단, 2번 연산은 N이 K로 나누어 떨어질 때 만 선택할 수 있다. 

1. N에서 1을 뺀다.
2. N를 K로 나눈다.

N과 K가 주어질 때 N이 1이 될 때 까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.

예제: N = 17, K = 4 일때, 1번 과정을 1번, 2번 과정을 2번 실행하면 N은 1이 된다. 따라서 정답은 3이다.

"""

"""
아이디어:

N이 K의 배수가 될 때 까지 1을 반복한다.
N이 K의 배수가 된다면 

"""


n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)

    n = target

    if n < k:
        break

    n //= k
    result += 1

result += (n-1)
print(result)
