'''
[폴리오미노]
AAAA BB
. X -> X를 덮음
사전 순으로 가장 앞서는 답

4 6 8 10
'''
S = []
word = ''
for i in input():
    if i == 'X':
        word += i
    else:  # '.'
        S.append(word)
        S.append(i)
        word = ''
S.append(word)  # 마지막 단어 붙이기
        
answer = []
for s in S:
    if len(s) == 2:
        answer.append('BB')
    else:
        if s == '.' or s == '':
            answer.append(s)
            continue
        
        a, b = divmod(len(s), 4)
        answer.append('AAAA'*a)
        if b % 2 != 0:  #1, 3
            print(-1)
            exit()
        if b == 2:
            answer.append('BB')

print(''.join(answer))