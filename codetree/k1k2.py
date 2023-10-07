'''
a1 ~ an
서로 다른 두 원소를 골라 더했을 때 
k1, k2가 되는 서로 다른 가짓수?
원소의 숫자가 같더라도 수열의 위치가 다르면 다른 가짓수
'''
from collections import defaultdict

n, k1, k2 = map(int, input().split())
n_list = list(map(int, input().split()))

def solve(target):  # 12
    n_dict = defaultdict(int)
    res = 0
    for i in n_list:
        res += n_dict[target-i]  # 12 - 4 / 12 - 8
        n_dict[i] += 1
    return n_dict, res

#print(solve(k1), solve(k2))
print(solve(k1)[0], solve(k2)[0])  # {6: 2, 8: 1, 4: 1, 3: 0, 9: 1})
print(solve(k1)[1], solve(k2)[1])