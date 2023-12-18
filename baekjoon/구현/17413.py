'''
[단어 뒤집기2]
<open>tag<close>: '<' 만나면 털기, '>' 만나면 털기
<ab cd>fe hg<ij kl>: '<'에 아직 있다는거 알려야 함
   
'''
s = input()

answer = ''  # 최종 문자열

word = []
flag = True  # masking 아님: rev 가능
for i in range(len(s)):
    if s[i] == '<':
        flag = False
        answer += ''.join(reversed(word)).lstrip().rstrip()
        word = []

    word.append(s[i])
    if s[i] == '>':
        flag = True
        answer += ''.join(word)
        word = []
    if flag and s[i] == ' ':
        answer += ''.join(reversed(word)).lstrip().rstrip() + ' '
        word = []
        
print(answer if not word else answer + ''.join(reversed(word)))
