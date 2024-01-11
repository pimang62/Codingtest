'''
[참외밭]
임의의 한 꼭짓점에서 반시계 방향으로 둘레를 돌며,
1m^2에서 자라는 참외의 개수*넓이?

동1, 서2, 남3, 북4

ㄱ : [3, s(1, 3), 1, b(4, 2)]
┏  : [3), 1, s(4, 1), 4, b(2]
┗  : [b(3, 1), 4, s(2, 4), 2]
┛  : [3, b(1, 4), 2, s(3, 2)]
- 규칙 : 1/2 & 3/4 나머지 건너 뛰고 안쪽
'''

k = int(input())

maxi = [[0, 0], [0, 0]]  # 인덱스, 최댓값
nlist = []
for i in range(6):
    d, length = map(int, input().split())
    if d == 1 or d == 2:  # 동서 중 max
        if length > maxi[0][1]:
            maxi[0][0] = i  # index
            maxi[0][1] = length
    else:  # d == 2 or d == 3
        if length > maxi[1][1]:
            maxi[1][0] = i  # index
            maxi[1][1] = length
    nlist.append([i, length])

print(maxi)
# 두 bigger 인덱스 중에 작은 걸 고르기
idx = min(maxi[0][0], maxi[1][0])
mini = [0, 0]  # 인덱스 없이 값만 찾기

# in range에 있는 값 찾기
mini[0] = nlist[(idx+3)%6][1]
mini[1] = nlist[(idx+4)%6][1]

# 참외 개수 k * (바깥 넓이 - 안쪽 넓이)
print(k*(maxi[0][1]*maxi[1][1] - mini[0]*mini[1]))
            