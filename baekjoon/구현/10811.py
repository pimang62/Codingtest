'''
[바구니 뒤집기]
1~n번, n개의 바구니
m번 바구니의 순서를 역순으로
범위를 정하고 -> 역순
'''
n, m = map(int, input().split())
d = [k for k in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())  # 1-indexed
    d = d[:i-1]+[k for k in reversed(d[i-1:j])]+d[j:]

print(*d)
    