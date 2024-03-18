'''
[사과 담기 게임]
스크린은 N칸, M칸 바구니
가장 처음에 왼쪽 M칸 차지

s, e = 0, 1
0 1 2 3 4 5
| | | | | |
1 -> 0 포함 -> 0, 1
5 -> 4 미포함 -> [4], 4 -> 4, 5
3 -> 2 미포함 -> [-2], -2 -> 2, 3

s, e = 0, 2
0 1 2 3 4 5
| | | | | |
1 -> 0 포함 -> 0, 2
5 -> 4 미포함 -> 4, [3] -> 3, 5
3 -> 2 미포함 -> [-1], -3 -> 2, 4
'''
n, m = map(int, input().split())
j = int(input())

cnt = 0  # 이동 거리 sum
s, e = 0, m
for _ in range(j):
    d = int(input())
    if s <= d-1 <= e and s <= d <= e:
        continue
    ns, ne = d-1-s, d-e
    cnt += min(abs(ns), abs(ne))
    if ns < 0 or ne < 0:
        tmp = max(ns, ne)
    else:
        tmp = min(ns, ne)
    s += tmp; e += tmp

print(cnt)