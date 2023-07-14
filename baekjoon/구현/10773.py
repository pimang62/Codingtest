'''
[제로]
잘못된 수를 부르면 0을 외침 -> 지움
모든 수를 받아 적은 후 그 합?

정수가 0일 경우 가장 최근 수 지우고 아니면 그 수를 쓴다
단, 0일 경우 지울 수 있는 수가 반드시 있음!

스택 활용?

입력)
k = int(input())    # 1 <= k < 1e5

for _ in range(k):
    n = int(input())    # 0 <= n <= 1e6

'''

k = int(input())    # 1 <= k < 1e5

array = []
for _ in range(k):
    n = int(input())    # 0 <= n <= 1e6
    if n == 0:
        array.pop()
    else:
        array.append(n)

print(sum(array))
