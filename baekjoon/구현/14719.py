'''
[빗물]
고이는 빗물의 총량?
전혀 고이지 않을 경우 0

0 0 0 1
1 0 0 1
1 0 0 1 
1 0 1 1

3 0 1 | 4 |
3 3 3
3 0 1
  3 2 

3 1 2 3 | 4 | 1 1 2
3 3 3 3       2 2 2 
3 1 2 3       1 1 2
  2 1 0       1 1 0

- max값을 기준으로 왼쪽, 오른쪽에서 훑음
- 각 구간에서의 (두 번째임을 보장할 수 있는 곳에서) max와 현재값을 비교

'''
h, w = map(int, input().split())

A = list(map(int, input().split()))

# maxi, idx = max(A), A.index(maxi)
idx, maxi = 0, 0
for i in range(len(A)):
    if A[i] > maxi:
        maxi = A[i]
        idx = i

# 투 포인터
answer = 0
left_max = 0
for i in range(idx):
    if A[i] > left_max:
        left_max = A[i]
    answer += left_max - A[i]

right_max = 0
for j in range(w-1, idx-1, -1):
    if A[j] > right_max:
        right_max = A[j]
    answer += right_max - A[j]

print(answer)

# 스택
result = 0
left_stack = []
for i in range(idx):
    if not left_stack:
        left_stack.append(A[i])
        continue
    if left_stack[-1] < A[i]:
        left_stack.pop()
        left_stack.append(A[i])
    result += left_stack[-1] - A[i]

right_stack = []
for j in range(w-1, idx-1, -1):
    if not right_stack:
        right_stack.append(A[j])
        continue
    if right_stack[-1] < A[j]:
        right_stack.pop()
        right_stack.append(A[j])
    result += right_stack[-1] - A[j]

print(result)
