'''
가로 길이가 n, 세로 길이가 2인 직사각형 바닥이 있다.
1 X 2, 2 X 1, 2 X 2인 덮개로 채우고자 한다.

1 X 2를 사용하고 싶다면 2 X 2의 공간에 2개를 채운다.
2 X 1을 사용하고 싶다면 2 X 1 공간에 1개를 채운다.
2 X 2를 사용하고 싶다면 2 X 2의 공간에 1개를 채운다.

가로의 길이가 1일 때 1 총 1가지
가로의 길이가 2일 때 1, 1 / 2 -> 1 X 2 2개, 2 X 1 1개, 2 X 2 1개 총 3가지
가로의 길이가 3일 때 1, 2 / 2, 1 
가로의 길이가 4일 때 .. / 2, 2 / 3, 1

중복되지 않는 경우의 수는 총 두 가지이다.
1. 2 X 1이 남았다면 2 X 1 하나를 채운 1가지 경우가 생긴다.
2. 2 X 2가 남았다면 1 X 2 2개, 2 X 2 1개를 채운 2가지 경우가 생긴다.

a_i = a_i-1 * 1 + a_i-2 * 2
'''

# 가로의 길이가 주어짐
n = int(input())    # 3

# DP 테이블
d = [0] * n     # 0~2

d[0] = 1
d[1] = 3
for i in range(2, n):
    d[i] = (d[i-1] * 1 + d[i-2] * 2) % 796796   # 값이 굉장히 커질 수 있기 때문

print(d[n-1])


