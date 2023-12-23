# string S consisting of N, properly nested
# given a string S, returns "1" if string S is "properly nested" and "0" otherwise.

# 70% : S is empty; return 1, 100% : O(N)
def solution(S):
    N = len(S)  # [0..1,000,000]
    # if N == 0:  # stack이 빌 때 1이 될 수 있으므로
    #     return 0

    stack = []
    for i in range(N):
        if stack and stack[-1] == '(' and S[i] == ')':
            stack.pop()
            continue
        stack.append(S[i])

    return 1 if not stack else 0  # S is empty; return 1