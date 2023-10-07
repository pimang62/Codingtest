'''
빗변 가장 끝 부분으로 이동했을 때 
얻을 수 있는 최대합?
오른쪽 or 아래로만 이동
'''

n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(len(d[i])):
        if i == 0 and j == 0: continue
        if i == 0 :  # 왼쪽에서만
            d[i][j] += d[i][j-1]
        elif j == 0: # 위쪽에서만
            d[i][j] += d[i-1][j]
        else:
            d[i][j] += max(d[i][j-1], d[i-1][j])

ans = 0
for i in range(n):
    ans = max(ans, d[i][-1])

print(ans)
