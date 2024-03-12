'''
[비밀번호 발음하기]
1. 모음(a, e, i, o, u) 하나를 반드시 포함
2. 모듬이 3개 혹은 자음이 3개 연속오면 안됨
3. 같은 글자가 연속적으로 두번 오면 안되나, ee와 oo는 허용
'''
aeiou = 'aeiou'

while True:
    password = input()
    if password == "end":
        break
    cnt = 0  # count
    flag = True
    for i in range(len(password)):
        if password[i] in aeiou:
            cnt += 1
        if 1 < i:  # 모음만 잔뜩, 자음만 잔뜩
            if (password[i] in aeiou and password[i-1] in aeiou and password[i-2] in aeiou) or \
               (password[i] not in aeiou and password[i-1] not in aeiou and password[i-2] not in aeiou):
                flag = False
                break
        if 0 < i and password[i-1] == password[i] and password[i] not in ['e', 'o']:
            flag = False
            break

    if cnt > 0 and flag:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')