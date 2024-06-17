'''
[로마 숫자 만들기]
I, V, X, L: 1, 5, 10, 50
문자열의 값은 문자의 수를 모두 합한 값

문자의 순서는 신경쓰지 않는다
로마 숫자 N개 사용, 만들 수 있는 서로 다른 수의 개수?
'''
from itertools import combinations_with_replacement

N = int(input())

number = set()
for tmp in combinations_with_replacement([1, 5, 10, 50], N):
    number.add(sum(tmp))

print(len(number))
