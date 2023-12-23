# binary gap within a positive integer N, "surrounded" by ones at both ends
# given a positive integer "N"
# returns the length of its "longest" binary gap
# return "0" if N doesn't contain a binary gap.
# stack = [ 1 0 start, 0 1 update]

# 100%
def solution(N):
    string = bin(N)[2:]  # str type!
    stack = []
    answer = 0  # 최댓값 기록
    cnt = 0  # 구간값 기록
    for i in range(len(string)):
        if not stack:  # 첫 값
            stack.append(string[i])
            continue
        # 앞선 값이 1이고 내가 0이면 : cnt
        elif stack[-1] == '1':
            if string[i] == '0':
                cnt += 1
                stack.append(string[i])
        # 앞선 값이 0이고 내가 1이면 : update
        elif stack[-1] == '0':
            if string[i] == '1':
                answer = max(answer, cnt)
                cnt = 0  # reset
                stack.append(string[i])
            else:  # string[i] == '0'
                cnt += 1

    return answer
