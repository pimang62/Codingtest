'''
[그룹 단어 체커]
한 스펠이 연속해서 나타나는 단어가 그룹 단어
ex. aabbbccb 안 됨!

'''

n = int(input())

'''
def check(w):
    stack = []
    log = []
    for i in w:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            continue
        elif stack[-1] != i:
            l = stack.pop()
            log.append(l)
            if i not in log:
                stack.append(i)
            else:   # log에 들어 있다면
                return False
    return True

    #return True if (len(stack) == 1 and stack[-1] not in log) else False
    #return log


cnt = 0
for _ in range(n):
    word = input()
    if check(word):
        cnt += 1

print(cnt)
'''

cnt = n
for _ in range(n):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            cnt -= 1
            break

print(cnt)
