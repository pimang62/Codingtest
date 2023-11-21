'''
[공 넣기]
1~n까지 번호 매겨져 있음
가장 처음 바구니에는 공 x
바구니에는 공 1개만

m번 공을 넣으려고 함
공을 넣을 범위를 정함
모두 같은 번호가 적혀있는 공을 넣음

공이 이미 있으면 공을 빼고 넣음

'''
n, m = map(int, input().split())

d = [0]*(n+1)  # 1-indexed

for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i, j+1):
        d[l] = k
        
print(*d[1:])
    