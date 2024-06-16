'''
[추월]
대근이는 터널 입구, 영식이는 터널 출구 잠복
들어가는 순서대로, 나오는 순서대로 적어둠

n대가 지나간 후, 반드시 추월한 차들의 수?
1 <= n <= 1000
'''
n = int(input())

cars = {}
for i in range(n):
    in_num = input()
    cars[in_num] = cars.get(in_num, i)

cnt = 0
stack = []
for j in range(n):
    out_num = input()
    while stack and stack[-1] > cars[out_num]:
        stack.pop()
        cnt += 1
    stack.append(cars[out_num])

print(cnt)