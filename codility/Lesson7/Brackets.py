# string S consisting of N characters, properly nested
# given a string S, returns "1" if S is properly nested and "0" otherwise.

# 70% : S is empty; return 1, 100% : O(N)
def solution(S):
    N = len(S)  # [0..200,000]
    # if N < 2:  # 0 or 1
    #     return 0  # None or '('
    
    pair = {')':'(', '}':'{', ']':'['}

    stack = []
    for i in range(N):
        # stack에 아무것도 없거나 내 짝이 아니라면 
        if (not stack) or (S[i] not in pair) or (stack[-1] != pair[S[i]]):
            stack.append(S[i])
        elif stack[-1] == pair[S[i]]:
            stack.pop()

    return 1 if not stack else 0  # S is empty; return 1