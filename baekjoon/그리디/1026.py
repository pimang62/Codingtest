'''
[보물]
길이가 n인 정수 배열 A와 B가 있다.
S = A[0] * B[0] + ... + A[n-1] * A[n-1]
S의 값을 가장 작게 만들기 위해 A의 수를 재배열
단, B의 수는 재배열하면 안 된다.
S의 최솟값은?
'''

n = int(input())

# 집합 A는 오름차순, B는 내림차순
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

S = 0
for i in range(n):
    S += A[i] * B[i]

print(S)