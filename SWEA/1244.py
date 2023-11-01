'''
[최대 상금]

숫자판, 교환 횟수
10000 1000 100 10 1 

교환이 중복되어도 됨!

012
123 1 321

0123
2737 1 7732

01234
32888 2 

[(2, 1), (3, 0), (8, 2), (8, 3), (8, 4)]
[(8, 4), (8, 3), (8, 2), (3, 0), (2, 1)]

원래 리스트 = [3, 2, 8, 8, 8]
cnt == 1 : [3, 8, 8, 8, 2]

'''
t = int(input())

def dfs(cnt):
    global ans
    if cnt > trade:
        return
    if cnt == trade:
        ans = max(ans, int(''.join(map(str, nlist))))
        return
    for i in range(0, len(nlist)-1):
        for j in range(i+1, len(nlist)):  # i+1!!
            nlist[i], nlist[j] = nlist[j], nlist[i]
            
            check = int(''.join(map(str, nlist)))
            if (cnt, check) not in sets:
                dfs(cnt+1)
                sets.add((cnt, check))

            nlist[j], nlist[i] = nlist[i], nlist[j]
    return
    
for k in range(1, t+1):
    numbers, trade = input().split()  # str!
    trade = int(trade)  # int: 2
    nlist = [int(n) for n in numbers]  # [3, 2, 8, 8, 8]
    
    ans = 0  # 최댓값 저장
    sets = set()  # 중복 제거
    dfs(0)
    
    print(f'#{k}', ans)
    
