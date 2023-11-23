'''
[공 바꾸기]
1~n 번호의 공
m번 공을 바꿈
'''
n, m = map(int, input().split())
d = [i for i in range(n+1)]  # 0-indexed

for _ in range(m):
    i, j = map(int, input().split())
    d[j], d[i] = d[i], d[j]

print(*d[1:])
    
    