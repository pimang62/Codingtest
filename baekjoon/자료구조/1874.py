'''
[스택 수열]

입력)
n = int(input())  # <= 1e5

table = []
for _ in range(n):
    table.append(int(input()))
'''

# 나의 풀이 : 232ms
import sys
input = sys.stdin.readline

n = int(input())  # <= 1e5

table = []
for _ in range(n):
    table.append(int(input()))

idx = 0     # target
i = 1   # number
num = []
answer = []

while i != n+1:
    if len(num) == 0 or table[idx] != num[-1]:
        num.append(i)
        answer.append('+')
        i += 1
    if table[idx] == num[-1]:
        num.pop()
        answer.append('-')
        idx += 1

while idx < n:
    if table[idx] == num[-1]:
        num.pop()
        answer.append('-')
        idx += 1
    else:
        print("NO")
        exit(0)

for a in answer:
    print(a)


# 다른 사람의 풀이 : 192ms
import sys
input = sys.stdin.readline

# 입력값
N = int(input())

# 스택
stack = []

# 스택에 넣는 값
cnt = 1

# 결과 리스트
result = []

for _ in range(N):
    
    # 값 : 4
    val = int(input())  
    
    while cnt <= val:
        stack.append(cnt)
        result.append("+")
        cnt += 1
    
    if stack[-1] == val:
        stack.pop()
        result.append("-")
    
    else:
        print("NO")
        exit(0)

for r in result:
    print(r)