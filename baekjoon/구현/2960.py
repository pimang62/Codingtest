'''
[에라토스테네스의 체]
'''
# 44ms
n, k = map(int, input().split())

d = [0]*(n+1)  # 1-indexed
d[0], d[1] = 1, 1

cnt = 0
while any(x < 1 for x in d):
    for i in range(2, n+1):
        if not d[i]:
            for l in range(1, 1000):
                j = i*l  # 1, 2, 3, ...
                if j > n:
                    break
                if not d[j]:
                    d[j] = 1
                    cnt += 1
                    if cnt == k:
                        print(j)
                        exit(0)  

# 56ms
n, k = map(int, input().split())

answer = []
for i in range(2, n+1):
    for j in range(i, n+1, i):
        if j not in answer:
            answer.append(j)
            if len(answer) == k:
                print(answer[-1])
                exit(0)
