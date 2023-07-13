""" 동빈이네 전자 매장에는 부품이 N개가 있다. 
    각 부품은 정수 형태의 고유 번호가 존재한다.

    손님이 M개의 부품을 구매하겠다는 요청을 했다.
    매장에 부품이 있다면 yes, 아니면 or을 출력하라."""

""" 
n
n_list
m
m_list
"""
"""
5 
8 3 7 9 2
3
5 7 9
"""

# 계수 정렬
n = int(input())
array = [0] * 100001

n_list = list(map(int, input().split()))
for i in n_list:
    array[i] = 1

m = int(input())
m_list = list(map(int, input().split()))

for j in m_list:
    if array[j] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

