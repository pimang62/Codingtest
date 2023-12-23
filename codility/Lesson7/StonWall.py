# build a stone wall, N meters long, and its thickness should be constant
# different heights in different places.
# H[I] is the height of the wall, [0~N-1]
# cuboid stone blocks, compute the "minimum" number of blocks needed to build the wall.

# 100% : O(N)
def solution(H):
    N = len(H)  # [1..100,000]
    stack = []  # 값이 담길 공간
    cnt = 0  # 전체 블럭 개수
    for i in range(N):
        while stack and stack[-1] > H[i]:  # 내가 더 작다면
            stack.pop()  # 평탄화
        if not stack or stack[-1] < H[i]:  # 내가 더 크면
            stack.append(H[i])
            cnt += 1
        # 같은 경우 세지도 않고 넘어야 함!!
    return cnt