'''
[명령 프롬프트]
a?b.exe
n <= 50, len(s) <= 50
'''
n = int(input())

s = []
for _ in range(n):
    tmp = [s for s in input()]
    if not s:
        s = tmp
    else:
        for i in range(len(tmp)):
            if tmp[i] == '?':
                continue
            if s[i] != tmp[i]:
                s[i] = '?'

print(''.join(s))