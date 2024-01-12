'''
[펠린드롬 만들기]
알파벳 대문자로만 된 최대 50글자
AA B CC D A 
ZZAA -> AZ''ZA : middle 없음!
'''
from collections import Counter

string = input()
str_dict = Counter(string)

middle = ''  # 짝수일 때는 기록 안됨!
candidate = []
cnt = 0  # 홀수 개수 cnt 
for k, v in str_dict.items():
    if v % 2 != 0:
        cnt += 1
        middle = k
    candidate.append(k*(v//2))

candidate.sort()

if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    print(''.join(candidate) + middle + ''.join(reversed(candidate)))