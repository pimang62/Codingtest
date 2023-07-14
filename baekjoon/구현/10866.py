'''
[덱]
push_front x : 앞에 넣기
push_back x : 뒤에 넣기
pop_front : 앞에 있는 수 빼고 출력, 만약 없으면 -1
pop_back : 뒤에 있는 수 빼고 출력, 만약 없으면 -1
size : 들어있는 정수의 개수
empty : 비어있으면 1 or 0
front : 앞에 있는 수 출력, 없으면 -1
back : 뒤에 있는 수 출력, 없으면 -1

입력)
n = int(input())    # 1 <= n <= 1e4
for _ in range(n):
    order = input()     # 1 <= x <= 1e5

'''
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())    # 1 <= n <= 1e4

q = deque()
for _ in range(n):
    order = input().strip().split()     # 1 <= x <= 1e5
    if order[0] == 'size': 
        print(len(q))   # print(len(q) if len(q) > 0 else -1) 해서 틀렸다..
    elif order[0] == 'empty':
        print(1 if len(q) == 0 else 0)
    elif order[0] == 'front':
        print(q[0] if len(q) > 0 else -1)
    elif order[0] == 'back':
        print(q[-1] if len(q) > 0 else -1)
    elif order[0] == 'pop_front':
        print(q.popleft() if len(q) > 0 else -1)
    elif order[0] == 'pop_back':
        print(q.pop() if len(q) > 0 else -1)  
    elif order[0] == 'push_front':
        q.appendleft(int(order[1]))
    else:   # 'push_back x'
        q.append(int(order[1]))
    

