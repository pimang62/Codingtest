'''
[사탕 게임]
인접한 다른 사탕 두 개를 행, 열도!! swap
먹을 수 있는 연결된 사탕 수 최대!

3
CCP
CCP
P(PC)

5
YCPZY
CYZZP
CCPPP
(YC)YZC
CPPZZ

- 시간 복잡도: O(N**4)
- (swap: 50 * check: 50+50)*2: 행, 열
- 총 10**6
'''
n = int(input())

graph = []
for _ in range(n):
    graph.append([i for i in input()])

answer = 0  # 전체 최댓값 
def check():
    global answer
    for i in range(n):
        cnt = 1  # 같은 횟수
        # 연속된 최대 구하기!
        for l in range(n-1):
            if graph[i][l] == graph[i][l+1]:
                cnt += 1
            else:  # !=
                cnt = 1
            answer = max(answer, cnt)
        
    for j in range(n):
        column = []
        for i in range(n):
            column += graph[i][j]
        cnt = 1  # 같은 횟수
        # 연속된 최대 구하기!
        for l in range(n-1):
            if column[l] == column[l+1]:
                cnt += 1
            else:  # !=
                cnt = 1
            answer = max(answer, cnt)

def swap(r1, c1, r2, c2):  # 좌표
    global graph
    graph[r1][c1], graph[r2][c2] = graph[r2][c2], graph[r1][c1]

for i in range(n):
    for j in range(n-1):
        if graph[i][j] != graph[i][j+1]:
            # 행 swap: swap(i, j, i, j+1) 대체 가능
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
            check()
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]

for j in range(n):
    for i in range(n-1):
        if graph[i][j] != graph[i+1][j]:
            # 열 swap: : swap(i, j, i+1, j) 대체 가능
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
            check()
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
         
print(answer)