'''
[농작물 수확하기]

012
132 0
254 1
021

01234
05023 0
33212 1
12511 2
23321 3 (5-1 -3)
24132 4 (5-1 -4)

'''
T = int(input())
for t in range(1, T+1):
    n = int(input())

    graph = []
    for _ in range(n):
        graph.append([int(r) for r in input()])

    mid = n // 2  # 2 = 5//2, 3 = 7//2
    answer = 0
    for i in range(n):
        if i <= mid:
            answer += sum(graph[i][mid-i:mid+i+1])
        else:
            answer += sum(graph[i][mid-(n-1-i):mid+(n-1-i)+1])

    print(f'#{t} ' + str(answer))