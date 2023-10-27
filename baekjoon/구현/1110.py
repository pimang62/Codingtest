'''
26 = 2 + 6 = 8 = 68
68 = 6 + 8 = 14 = 84
01 = 0 + 1 = 1 = 11

'''
s = input()

target = s
if len(target) == 1:
    target = '0'+target

tmp = str(int(target[0])+int(target[1]))
target = target[1] + tmp[-1]
cnt = 1  # 횟수
while True:
    if int(target) == int(s):  # 01 == 1
        print(cnt)
        break
    tmp = str(int(target[0])+int(target[1]))
    target = target[1] + tmp[-1]
    cnt += 1

