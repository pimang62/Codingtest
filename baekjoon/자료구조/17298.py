'''
[오큰수] 모노톤 스택

오른쪽에 있으면서 나보다 큰 수 중 가장 왼쪽

     5  7  7  -1
A = [3, 5, 2, 7]
     6
      -1  8  8 -1
A = 5 [9, 5, 4, 8]
    13
A.pop() -> 9 = max_val
list = [-1  8  8  -1]

- A.pop() 원소가 max_val보다 크면 넘김(-1) max_val 갱신
- A.pop() 원소가 max_val보다 작으면 max_val


'''
n = int(input())
A = list(map(int, input().split()))

d = [-1]*n
stack = []

for i in range(n-1, -1, -1):
    if not stack:
        stack.append((A[i]))  # index 필요 없음
        continue
    while stack and stack[-1] <= A[i]:
        stack.pop()
    if stack:  # 큰 값이 남아 있으면
        d[i] = stack[-1]
    stack.append(A[i])  # 담기만 함

print(*d)