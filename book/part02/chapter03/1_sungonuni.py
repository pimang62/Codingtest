

"""
배열 A는 정수 N개로 구성되어 있다. A의 정수들을 M번 더하여 가장 큰 수를 만들고 싶다. 단, 배열의 특정 인덱스에 해당하는 수를 연속해서 K번을 초과하여 더할 수 없다. 

입력으로 정수 N, M, K를 받는다. N은 입력 배열의 길이를 의미한다. 
M은 숫자가 더해지는 횟수를 의미한다. K는 연속해서 더할 수 있는 숫자의 개수를 의미한다.

예시:
N = 5, M = 8, K = 3
A = [2,4,5,4,6]

⇒ 6+6+6+5+6+6+6+5 = 46
"""

# 아이디어

# 가장 큰 수를 K번 곱한 것에 두번째로 큰 수를 1번 더한다.
# 이것을 반복한다.

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

first = a[0]
second = a[1]

first_count = (m // (k+1)) * k
second_count = m - first_count

result = first * first_count + second * second_count

print(result)