'''
[괄호]
'()' : VPS
if x and y is VPS, (x) & xy also

입력)
t = int(input())
for _ in range(t):

'''

t = int(input())

for _ in range(t):
    stack = []
    string = input()
    for s in string:
        if len(stack) == 0 or s == "(":
            stack.append(s)
        if s == ")" and stack[-1] == "(":
            stack.pop()
    if len(stack) > 0:
        print("NO")
    else:
        print("YES")  