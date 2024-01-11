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

max_idx = [0, 0]  # 인덱스
max_length = [0, 0]  # 최댓값

nlist = []
for i in range(6):
    d, length = map(int, input().split())
    if d == 1 or d == 2:  # 동서 중 max
        if length > max_length[0]:
            max_idx[0] = i  # index
            max_length[0] = length  # max
    else:  # d == 2 or d == 3:
        if length > max_length[1]:
            max_idx[1] = i  # index
            max_length[1] = length  # max
    nlist.append(length)

# 두 bigger 인덱스 중에 작은 것, 큰 것 고르기
# idx = min(max_idx)  # b[0]의 인덱스가 클 때도 있음
# jdx = max(max_idx)  # 이렇게 하면 안됨!!

check = [0]*6
for j in max_idx:
    for jdx in j-1, j, (j+1)%6:  # j-1, j, j+1
        check[jdx] = 1

mini = []  # 인덱스 없이 값만 찾기
for l in range(6):
    if not check[l]:
        mini.append(nlist[l])

# 참외 개수 k * (바깥 넓이 - 안쪽 넓이)
print(k*(max_length[0]*max_length[1] - mini[0]*mini[1]))
