'''
n명의 사람이 일렬로
1~n번까지의 번호

사람 수 n, 자연수 k
사람 나열하는 방법 사전 순!!
k번째 방법은?

1 <= n <= 20
- factorial(20) : 2432902008176640000

k < factorial(20)
'''
import sys
sys.setrecursionlimit(10000000)

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

def solution(n, k):   # ex.  k : 5
    n_list = [ i+1 for i in range(n) ]
    result = []
    k -= 1    # 나누어 떨어져서 인덱스 1되면 안 됨
    while n != 0:
        i, k = divmod(k, factorial(n-1))  # 2, 1 : 인덱스, 남은 값
        result.append(n_list.pop(i))    # n_list[2]
        n -= 1
    return result

print(solution(3, 5))
print(solution(4, 6))   # 첫 index가 1이 되지 않아야!
print(solution(4, 9))
