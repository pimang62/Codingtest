'''
[숫자 정사각형]
꼭짓점에 쓰여있는 수가 모두 같은 정사각형의 크기(넓이)!
'''
n, m = map(int, input().split())
graph = [[r for r in input()] for _ in range(n)]

def solution():
    for k in range(min(n, m), 0, -1):  # n~1
        for i in range(0, n-k+1):
            for j in range(0, m-k+1):
                if graph[i][j] == graph[i][j+k-1] == graph[i+k-1][j] == graph[i+k-1][j+k-1]:
                    return k  # 바로 break

answer = solution()
print(answer*answer)