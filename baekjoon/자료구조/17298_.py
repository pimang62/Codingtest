'''
[오큰수]
https://www.acmicpc.net/problem/17298

A_i의 오큰수: 오른쪽, A_i보다 큰 수 중 가장 왼쪽

stack = []
거꾸로 넣기!

stack = []
answer = []
for i in range(N-1, -1, -1):
    if stack and stack[-1] > A[i]:
        answer.append(stack[-1])
        continue
    # if not stack or stack[-1] <= A[i]
    stack.append(A[i])
'''
N = int(input())
A = list(map(int, input().split()))

stack = []
answer = []
for i in range(N-1, -1, -1):
    # print(stack, answer)
    while stack and stack[-1] <= A[i]:
        stack.pop()
    if stack and stack[-1] > A[i]:
        answer.append(stack[-1])
    else:
        answer.append(-1)
    stack.append(A[i])

print(*answer[::-1])