# The fish are numbered from 0 to N - 1
# P < Q, Array A contains the sizes of the fish.
# Array B contains the directions of the fish. 0 up / 1 down
# Then only one fish can stay alive - the larger fish eats the smaller one.
# calculate the "number" of fish that will stay "alive".
# return 2
# the elements of A are all "distinct".

def solution(A, B):
    stack = []
    for a, b in zip(A, B):
        if not stack or stack[-1][1] == b:  # 같은 방향
            stack.append([a, b])
            continue
        elif stack[-1][1] == 1:  # 다른 방향인데 앞이 1일 때 : 나는 0
            while stack and (stack[-1][1] != b and stack[-1][0] < a):
                stack.pop()
            if stack and (stack[-1][1] != b and stack[-1][0] > a):
                continue
        # 마지막 붙이기 / 다른 방향인데 앞이 0일 때
        stack.append([a, b])

    return len(stack)