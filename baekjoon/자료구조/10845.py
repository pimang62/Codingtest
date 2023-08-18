'''
[큐]
1. push X : 정수 X를 큐에 넣음
2. pop : 가장 앞에 있는 정수 빼고 출력, 만약 없으면 -1
3. size : 큐의 개수 출력
4. empty : 큐가 비어있으면 1, 아니면 0
5. front : 가장 앞에 있는 정수 출력, 만약 없으면 -1
6. back : 큐의 가장 뒤에 있는 정수 출력, 만약 없으면 -1

입력)
n = int(input())
for _ in range(n):
    order = list(input().split())
    print(order)

'''
import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
q = deque()
for _ in range(n):
    order = list(map(str, input().split()))
    # X : int 변환
    if len(order) >= 2:
        order[-1] = int(order[-1])
    if order[0] == "push":
        q.append(order[1])
    elif order[0] == "pop":
        if len(q) > 0:
            p = q.popleft()
            print(p)
        else:
            print(-1)
    elif order[0] == "size":
        print(len(q))
    elif order[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif order[0] == "back":
        if len(q):
            print(q[-1])
        else:
            print(-1)



