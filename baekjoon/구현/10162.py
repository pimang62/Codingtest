'''
[전자레인지]
A B C : 300 60 10
버튼을 적절히 눌러서 T가 되도록
누른 횟수의 합은 항상 최소!
'''
T = int(input())  # 초

A, B, C = 300, 60, 10
a, b, c = 0, 0, 0

a, t = divmod(T, A)  # 나머지
b, t = divmod(t, B)
c, t = divmod(t, C)

answer = [a, b, c]
if t == 0:
    print(*answer)
else:
    print(-1)
