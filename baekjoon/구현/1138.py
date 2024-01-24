'''
[한 줄로 서기]
1 2 3 4
0 0 1 0
0 2 1 0
0 2 1 3
4 2 1 3

1 2 3 4 5
0 0 0 0 0

'''
n = int(input())
info = list(map(int, input().split()))

answer = [0]*n  # [2, 1, 1, 0]

for i in range(n):  # 0~3
    cnt = 0  # 0의 개수가 몇 개인지
    for j in range(n):
        if cnt == info[i] and answer[j] == 0:
            answer[j] = i+1  # 0(index) -> 1
            break
        elif answer[j] == 0:
            cnt += 1
            
print(*answer)