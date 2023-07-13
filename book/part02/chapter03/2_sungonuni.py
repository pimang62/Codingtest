"""
정수로 구성된 N x M 행렬 A가 있다. 다음과 같은 과정을 거쳐 A에서 정수를 하나 뽑으려고 한다.
1. 임의의 행을 선택한다.
2. 선택한 행에서 가장 작은 수를 뽑는다.

이렇게 선택한 정수들 중에서 가장 큰 정수를 찾는 함수를 작성하시오.

입력은 첫번째 줄에 행의 개수 N과 열의 개수 M을 받는다.
두번째 줄에 N x M 행렬에 들어갈 숫자를 받는다. 각 숫자는 1 이상 10,000 이하의 자연수이다.
N = 3, M = 3
3 1 2
4 1 4 
2 2 1
"""

n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)