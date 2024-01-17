'''
[숫자 야구]
동일한 자리 1스트라이크, 다른 자리 1볼
3스트라이크면 끝

영수가 생각하고 있는 답의 개수?

4
123 1 1
356 1 0
327 2 0
489 0 1
'''
# from itertools import permutations

n = int(input())

target = []
for _ in range(n):
    s, a, b = input().split()
    target.append((s, int(a), int(b)))

nlist = [str(i) for i in range(1, 10)]  # 1~9
answer = 0  # 답의 개수
result = []  # just 결과 확인용

def dfs(cnt: int, num: list):
    global answer
    if cnt == 3:
        flag = True
        for (tar, a, b) in target:
            c, d = 0, 0
            for i in range(3):
                if tar[i] == num[i]:
                    c += 1
                elif num[i] in tar:
                    d += 1
            if (c, d) != (a, b):
                flag = False
                return 
        if flag:
            answer += 1
            result.append(''.join(num))  # 결과 확인용
        return 
    
    for x in range(9):  # index: 0~8
        if nlist[x] not in num:
            num.append(nlist[x])
            dfs(cnt+1, num)
            num.pop()
    return

dfs(0, [])
print(answer)
# print(result)  # ['324', '328']