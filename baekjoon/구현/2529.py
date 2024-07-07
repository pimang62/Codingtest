'''
[부등호]
'<'와 '>'가 k개 나열된 수열 A
앞 뒤에 서로 다른 수를 넣어 관계 만족

0~9까지, 선택된 숫자는 모두 "달라야"
k개의 부등호, k+1자리의 정수 중 최대/최소

2 <= k <= 9
첫 자리가 0인 경우도 정수 포함
'''
k = int(input())
A = input().split()

min_ans, max_ans = 1e10, 0

def dfs(i, stack :list, cnt):
    global min_ans, max_ans
    if cnt >= 2:
        if A[i] == '<' and stack[i] > stack[i+1]:
            return
        elif A[i] == '>' and stack[i] < stack[i+1]:
            return
    if cnt == k+1:
        min_ans = min(min_ans, int(''.join([str(s) for s in stack])))
        max_ans = max(max_ans, int(''.join([str(s) for s in stack])))
        return
    
    for n in range(10):
        if n not in stack:
            stack.append(n)
            dfs(i+1, stack, cnt+1)
            stack.pop()

dfs(-2, [], 0)

min_str = str(min_ans)
max_str = str(max_ans)

print(max_str if len(max_str) == k+1 \
    else '0'*(k+1-len(max_str)) + max_str)
print(min_str if len(min_str) == k+1 \
    else '0'*(k+1-len(min_str)) + min_str)

