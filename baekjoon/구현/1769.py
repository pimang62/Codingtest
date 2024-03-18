'''
[3의 배수]
양의 정수 x는 3의 배수인가?
>>> y는 3의 배수인가?

"1234567"
>>> 28
'''

X = input()
cnt = 0  # 몇 번 거쳤는지?

while len(X) > 1:
    new_X = 0
    for i in range(len(X)):
        new_X += int(X[i])
    X = str(new_X)
    cnt += 1

print(cnt)
if int(X) % 3 == 0:
    print("YES")
else:
    print("NO")

