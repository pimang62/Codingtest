'''
[이전 순열]
12345
12354
12435
12453
13245
13425
13452
13524
13542
14235

다음 순열 : 13 542 -> 3 4 swap -> 352 sort
이전 순열 : 135 24 -> 4
'''
n = int(input())
nlist = list(map(int, input().split()))

def solution():
    global nlist
    answer = []
    for i in range(n-1, 0, -1):
        if nlist[i-1] > nlist[i]:  # 앞쪽에 큰 값, 뒤쪽에 작은 값
            for j in range(n-1, 0, -1):
                if nlist[i-1] > nlist[j]:  # 큰, 작은
                    nlist[i-1], nlist[j] = nlist[j], nlist[i-1]
                    answer += nlist[:i]
                    answer += sorted(nlist[i:], reverse=True)
                    return ' '.join([str(s) for s in answer])
    return -1
    
print(solution())