# it should have different heights in different places.
# compute the "minimum" number of blocks needed to build the wall.
# the function should return 7
# 내가 작으면 새로운 블럭이 필요할거에요~

def solution(H):
    stack = []
    cnt = 0  # 블럭 개수
    for i in range(len(H)):
        # 큰 원소들 먼저! 없앰
        while stack and stack[-1] > H[i]:
            stack.pop() 
        # 첫 원소이거나 내가 앞선 높이보다 크다면
        if not stack or stack[-1] < H[i]:
            cnt += 1
            stack.append(H[i])
        # 이전 값이랑 같은 값이면 넘어감감
    
    return cnt