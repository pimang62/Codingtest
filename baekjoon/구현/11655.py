'''
[ROT13]
'''
# [A-Z, a-z]
upper = [chr(i) for i in range(65, 91)]
lower = [chr(j) for j in range(97, 123)]

s = input()
answer = []
for i in s:
    if i in upper:
        idx = upper.index(i)
        answer.append(upper[(idx+13)%26])
    elif i in lower:
        idx = lower.index(i)
        answer.append(lower[(idx+13)%26])
    else:  # ' ', '1'
        answer.append(i)

print(''.join(answer))