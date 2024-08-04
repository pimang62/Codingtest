'''
[숫자 빈도수]
https://www.acmicpc.net/problem/14912

1부터 n까지 특정 숫자의 빈도수?

ex. n = 11
1 2 3 4 5 6 7 8 9 10 11
1은 1, 10, 11 -> 4번

1 <= n <= 1e5
0 <= d <= 9
'''
n, d = map(int, input().split())

answer = 0
for i in range(1, n+1):
    str_i, str_d = str(i), str(d)
    answer += str_i.count(str_d)

print(answer)