# two "non-empty" arrays A and B consisting of N
# fish are numbered from 0 to N - 1
# P < Q, fish P is initially upstream of fish Q
# A contains the "sizes" of the fish : unique
# B contains the "directions" of the fish : 0 up /1 down
# two fish move in opposite directions, no living fish between them
# the "larger" fish eats the smaller one
# fish moving in the "same" direction "never meet"
# calculate the "number" of fish that will "stay alive".

# 30% : not "while"!, 100% : O(N)
def solution(A, B):
    N = len(A)  # same as len(B) : [1..100,000]
    stack = []
    for i in range(N):  # A[i], B[i]
        if not stack:
            stack.append((A[i], B[i]))
            continue
        while stack and (stack[-1][1] == 1 and B[i] == 0) and stack[-1][0] < A[i]:  # 내가 더 크다면 
            stack.pop()
        if stack and (stack[-1][1] == 1 and B[i] == 0) and (stack[-1][0] > A[i]):  # 나보다 이전 값이 더 크다면
            continue
        # (1, 1), (0, 0), (0, 1)의 경우 그냥 붙여주기
        # or (1, 0)인데 내가 크면 붙여주기
        stack.append((A[i], B[i]))
    
    return len(stack)