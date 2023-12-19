'''
[괄호의 값]
1. 올바른 괄호열인지 확인
  - ()[] ok, ([)] not ok
2. 계산값 출력
  - () : 2 [] : 3
  - ()[[]] : 2+3*3
  - ([]) : 2*3

stack = [ (() [[]] ) ([]) ]  # ( 2 + 3*3 ) * 2 + 3*2

'''
# 다른 사람의 풀이
stack = [] # 스택
res = 1 # result에 더해주기 전 임시 변수
result = 0 # 결과 변수
p = list(input()) # 입력값

# 1~4번째 과정 시작
for i in range(len(p)):
  if p[i]=='(':
    res *= 2
    stack.append(p[i])
    
  elif p[i]=='[':
    res *= 3
    stack.append(p[i])
    
  elif p[i]==')':
    if not stack or stack[-1]!='(':
      result = 0
      break
    if p[i-1]=='(': result += res
    res //= 2
    stack.pop()
    
  elif p[i]==']':
    if not stack or stack[-1]!='[':
      result = 0
      break
    if p[i-1]=='[': result += res
    res //= 3
    stack.pop()

if stack:
  print(0)
else:
  print(result)

# ---------------------------
pair = {')':'(', ']':'['}
score = {'(':2, '[':3}

s = input()

stack = []
mommy = 0  # 더해지는 지점
baby = 1  # 곱해지는 지점
for i in range(len(s)):
    if s[i] in score:  # '(' or '['
        baby *= score[s[i]]
        stack.append(s[i])
    if s[i] in pair:  # ')' or ']'
        # [] <- ')' or ']' / '(' <- ']'
        if not stack or stack[-1] != pair[s[i]]:
            mommy = 0  # 짝이 맞지 않음
            break
        if s[i-1] == pair[s[i]]:  # 원래 문자열 바로 앞이 pair여야 mommy한테 갈 수 있음!
            mommy += baby
        baby //= score[pair[s[i]]]  # 2 or 3: default
        stack.pop()  # ['[', ('[', ']'), ']']
        
print(mommy if not stack else 0)
        