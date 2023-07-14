'''
[요세푸스 문제]
1번~n번, n명
양의 정수 k(<= n)
순서대로 k번째 사람 제거

원에서 사람들이 제거되는 순서 (n, k)

입력)
n, k = map(int, input())

'''
from collections import deque

n, k = map(int, input().split())    # 7 3
result = []

q = deque([i for i in range(1, n+1)])
while q:
    for _ in range(k-1):    # 2
        x = q.popleft()
        q.append(x)
    result.append(q.popleft())

string = ', '.join(str(r) for r in result)
print("<" + string + ">")
