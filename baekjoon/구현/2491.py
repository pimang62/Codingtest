'''
[수열]

9
4 1 3 3 2 2 9 2 3

'''
n = int(input())
A = list(map(int, input().split()))

cnt = 1

acsen, tmp = [], 0  # 오름차순
for i in range(n):
    if not acsen or acsen[-1] <= A[i]:
        acsen.append(A[i])
        tmp += 1
    else:
        cnt = max(cnt, tmp)
        acsen, tmp = [A[i]], 1

# ex. 1 2 3 4 5
cnt = max(cnt, tmp)  # 한 번 더 확인

desen, tmp = [], 0  # 내림차순
for i in range(n):
    if not desen or desen[-1] >= A[i]:
        desen.append(A[i])
        tmp += 1
    else:
        cnt = max(cnt, tmp)
        desen, tmp = [A[i]], 1

cnt = max(cnt, tmp)  # 한 번 더 확인

print(cnt)