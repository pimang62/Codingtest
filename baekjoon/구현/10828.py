'''
[스택]
1. push X : 정수 X를 스택에 넣음
2. pop : 가장 위에 있는 정수를 빼고 그 수를 출력, 없으면 -1
3. size : 스택에 들어있는 정수의 개수
4. empty : 스택이 비어있으면 1 아니면 0
5. top : 스택 가장 위에 있는 정수 출력, 없으면 -1
'''

import sys

input = sys.stdin.readline
n = int(input())

stack = []
for _ in range(n):
    command = input().split()   # 이 자체로 list
    if len(command) == 2:   # push 
        stack.append(int(command[1]))
    if command[0] == 'pop':
        print(int(stack.pop())) if len(stack) != 0 else print(-1)
    if command[0] == 'size': print(len(stack))
    if command[0] == 'empty': print(1) if len(stack) == 0 else print(0)
    if command[0] == 'top': 
        print(int(stack[-1])) if len(stack) != 0 else print(-1)