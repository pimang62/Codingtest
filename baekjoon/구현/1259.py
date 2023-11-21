'''
[펠린드롬수]
숫자들이 주어짐
1 <= n <= 99999
마지막 줄에는 0
'''
def is_pelindrom(s):
    for i in range(len(s)//2):  # 01234 : 5//2
        if s[i] != s[len(s)-1-i]:
            return False
    return True

while True:
    test = input()
    if test == '0':
        break
    else: # if test != '0':
        if is_pelindrom(test):
            print('yes')
        else:
            print('no')
    